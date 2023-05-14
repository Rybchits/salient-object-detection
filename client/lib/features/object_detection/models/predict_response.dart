import 'package:freezed_annotation/freezed_annotation.dart';

import '../../../utils/images/manager.dart';

part 'predict_response.freezed.dart';

part 'predict_response.g.dart';

@freezed
class PredictResponse with _$PredictResponse {
  factory PredictResponse({
    @Default([])
    @JsonKey(defaultValue: [], name: 'predictions')
        ImageMatrix predictions,
  }) = _PredictResponse;

  factory PredictResponse.fromJson(Map<String, Object?> json) =>
      _$PredictResponseFromJson(json);
}
