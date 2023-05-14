import 'dart:async';

import 'package:client/features/display/models/display_state.dart';
import 'package:client/features/object_detection/manager.dart';
import 'package:client/features/selected_files/state_holder.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';
import 'package:rxdart/rxdart.dart';

import '../../utils/images/manager.dart';
import '../object_detection/models/detection_state.dart';

final displayControllerProvider =
    StateNotifierProvider<DisplayController, DisplayState>((ref) {
  final controller = DisplayController(
    ref.watch(selectedFilesStateHolderProvider.notifier),
    ref.watch(objectDetectionManagerProvider),
    ref.watch(imageManagerProvider),
  )..init();
  return controller;
});

class DisplayController extends StateNotifier<DisplayState> {
  DisplayController(
    this._selectedFilesStateHolder,
    this._objectDetectionManager,
    this._imagesManager,
  ) : super(DisplayState(
            displayTitle: 'Выберете файл для определния основного объекта'));

  final SelectedFilesStateHolder _selectedFilesStateHolder;
  final ObjectDetectionManager _objectDetectionManager;
  final ImageTransformationsManager _imagesManager;

  CompositeSubscription? _subscription;

  Future<void> init() async {
    _subscription ??= CompositeSubscription()
      ..add(_selectedFilesStateHolder.stream.listen((files) {
        final image = _imagesManager.fromPlatformFileToImage(files.first);
        if (image != null) {
          state = DisplayState(images: [
            LabeledImage(
              image: image,
              label: "Выбранное изображение",
            )
          ]);
        }
      }))
      ..add(
        _objectDetectionManager.stream
            .listen((event) => handleDetectionState(event)),
      );
  }

  void handleDetectionState(DetectionState? event) {
    if (event is DetectionStateSuccess) {
      state = DisplayState(
          images: [
            ...state.images,
            LabeledImage(
              image: _imagesManager.matrixToImage(event.predMask, scale: 255),
              label: 'Маска объекта',
            ),
            LabeledImage(
              image: _imagesManager.matrixToImage(_imagesManager
                  .mergeRGBMatrixWithMask(event.sourceImage, event.predMask)),
              label: 'Вырезанный объект',
            ),
          ],
          displayTitle:
              'Выберете другое изображение для определения основного объекта');

    } else if (event is DetectionStateLoading) {
      state = DisplayState(
        images: [state.images.first],
        isFetching: true,
        displayTitle: 'Загрузка...',
      );

    } else if (event is DetectionStateError) {
      state = DisplayState(images: state.images, displayTitle: event.message);
    }
  }

  List<LabeledImage> get images => state.images;

  DisplayState get currentState => state;

  @override
  Future<void> dispose() async {
    super.dispose();
    _subscription?.cancel();
    _subscription = null;
  }
}
