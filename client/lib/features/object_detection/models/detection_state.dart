import 'package:freezed_annotation/freezed_annotation.dart';

import '../../../utils/images/manager.dart';

part 'detection_state.freezed.dart';

part 'detection_state.g.dart';

@Freezed(unionKey: 'type')
class DetectionState with _$DetectionState {
  const factory DetectionState.success(
      ImageMatrix sourceImage, ImageMatrix predMask) = DetectionStateSuccess;

  const factory DetectionState.error(String message) = DetectionStateError;

  const factory DetectionState.loading() = DetectionStateLoading;

  factory DetectionState.fromJson(Map<String, dynamic> json) =>
      _$DetectionStateFromJson(json);
}
