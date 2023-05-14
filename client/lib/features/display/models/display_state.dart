import 'package:freezed_annotation/freezed_annotation.dart';
import 'package:image/image.dart';

part 'display_state.freezed.dart';

@freezed
class LabeledImage with _$LabeledImage {
  factory LabeledImage({
    Image? image,
    @Default('') String? label
  }) = _LabeledImage;
}

@freezed
class DisplayState with _$DisplayState {
  factory DisplayState({
    @Default([]) List<LabeledImage> images,
    @Default(false) bool isFetching,
    @Default('') String? displayTitle,
  }) = _DisplayState;
}