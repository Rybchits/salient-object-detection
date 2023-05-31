import 'dart:math';
import 'dart:typed_data';

import 'package:file_picker/file_picker.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';
import 'package:image/image.dart' as img;
import 'dart:ui' as ui;

typedef ImageMatrix = List<List<List<int>>>;

final imageManagerProvider = Provider(
  (ref) => ImageTransformationsManager(),
);

class ImageTransformationsManager {
  /// Преобразование файла в объект класса Image
  img.Image? fromPlatformFileToImage(PlatformFile file) {
    if (file.bytes == null || file.bytes?.buffer == null) {
      return null;
    }
    switch (file.extension) {
      case 'jpg':
        return img.decodeJpg(file.bytes!);
      case 'png':
        return img.decodePng(file.bytes!);
    }
    return null;
  }

  /// Преобразование набора байт в матрицу пикселей
  ImageMatrix imageMatrixFromBytes(
    Uint8List imageBytes, {
    required int width,
    required int height,
    int channels = 3,
  }) {
    assert(imageBytes.length == width * height * channels);

    List<List<int>> pixels = [];
    assert(imageBytes.length % channels == 0);
    for (int i = 0; i < imageBytes.length; i += channels) {
      pixels.add(imageBytes.getRange(i, i + channels).toList());
    }

    ImageMatrix reshapedImage = [];
    assert(pixels.length % width == 0);
    for (int i = 0; i < pixels.length; i += width) {
      reshapedImage.add(pixels.getRange(i, i + width).toList());
    }
    return reshapedImage;
  }

  /// Преобразование матрицы пикселей в объект класса Image
  img.Image matrixToImage(
    ImageMatrix matrix, {
    int? scale,
  }) {
    final width = matrix[0].length;
    final height = matrix.length;
    final numChannels = matrix[0][0].length;

    List<int> bytes = [];
    for (final row in matrix) {
      for (final pixel in row) {
        bytes.addAll(pixel.map((e) => e.toInt()));
      }
    }

    if (scale != null) {
      bytes = bytes.map((e) => e * scale).toList();
    }

    return img.Image.fromBytes(
      width: width,
      height: height,
      numChannels: numChannels,
      bytes: Uint8List.fromList(bytes).buffer,
    );
  }

  /// Преобразование объекта класса Image в widget для отображения
  Future<ui.Image> convertImageToFlutterUi(img.Image? image) async {
    if (image == null) {
      return Future.error('Null image');
    }

    if (image.format != img.Format.uint8 || image.numChannels != 4) {
      final cmd = img.Command()
        ..image(image)
        ..convert(format: img.Format.uint8, numChannels: 4);
      final rgba8 = await cmd.getImageThread();
      if (rgba8 != null) {
        image = rgba8;
      }
    }

    ui.ImmutableBuffer buffer =
        await ui.ImmutableBuffer.fromUint8List(image.toUint8List());

    ui.ImageDescriptor id = ui.ImageDescriptor.raw(buffer,
        height: image.height,
        width: image.width,
        pixelFormat: ui.PixelFormat.rgba8888);

    ui.Codec codec = await id.instantiateCodec(
        targetHeight: image.height, targetWidth: image.width);

    ui.FrameInfo fi = await codec.getNextFrame();
    ui.Image uiImage = fi.image;

    return uiImage;
  }

  ImageMatrix mergeRGBMatrixWithMask(
    ImageMatrix image,
    ImageMatrix mask, [
    List<int> replacedPixel = const [0, 0, 0],
  ]) {
    assert(image.length == mask.length);
    assert(image[0].length == mask[0].length);
    assert(image[0][0].length == 3 && mask[0][0].length == 1);

    for (var i = 0; i < image.length; i++) {
      for (var j = 0; j < image[i].length; j++) {
        if (mask[i][j][0] == 0) {
          image[i][j] = replacedPixel;
        }
      }
    }
    return image;
  }

  img.Image resizeToTargetSide(img.Image image, int targetSide) {
    final maxSide = max(image.width, image.height);
    final scaleSide = targetSide / maxSide;

    return img.copyResize(
      image,
      width: (image.width * scaleSide).round(),
      height: (image.height * scaleSide).round(),
    );
  }
}
