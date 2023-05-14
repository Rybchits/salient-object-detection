import 'dart:async';

import 'package:client/features/object_detection/models/detection_state.dart';
import 'package:client/features/object_detection/network/api.dart';
import 'package:client/features/selected_files/state_holder.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';
import 'package:image/image.dart';
import 'package:rxdart/rxdart.dart';

import '../../utils/images/manager.dart';

final objectDetectionManagerProvider = Provider(
  (ref) => ObjectDetectionManager(
    ref.watch(selectedFilesStateHolderProvider.notifier),
    ref.watch(objectDetectionApiProvider),
    ref.watch(imageManagerProvider),
  ),
);

class ObjectDetectionManager {
  final SelectedFilesStateHolder _selectedFilesStateHolder;
  final ObjectDetectionApi _api;
  final ImageTransformationsManager _imagesManager;

  final _streamController = BehaviorSubject<DetectionState>();

  static const heightImage = 320;
  static const widthImage = 320;

  ObjectDetectionManager(
    this._selectedFilesStateHolder,
    this._api,
    this._imagesManager,
  );

  Stream<DetectionState> get stream => _streamController.stream;

  Future<bool> predictOnSelectedFile() async {
    final file = _selectedFilesStateHolder.first;
    if (file == null) {
      return false;
    }

    Image? image = _imagesManager.fromPlatformFileToImage(file);
    if (image == null) {
      return false;
    }

    final matrix = _imagesManager.imageMatrixFromBytes(
      image.getBytes(order: ChannelOrder.rgb),
      width: image.width,
      height: image.height,
    );

    _streamController.add(const DetectionStateLoading());

    try {
      await _api.predictSalientObject(matrix).then((value) {
        _streamController
            .add(DetectionStateSuccess(matrix, value?.predictions ?? []));
      });
    } catch (e) {
      _streamController.add(const DetectionStateError(
          'Что-то пошло не так: попробуйте позже...'));
    }

    return true;
  }
}
