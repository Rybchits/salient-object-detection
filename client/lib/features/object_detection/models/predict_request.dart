import 'package:freezed_annotation/freezed_annotation.dart';

part 'predict_request.freezed.dart';

part 'predict_request.g.dart';

@freezed
class PredictRequest with _$PredictRequest {
  factory PredictRequest({
    @Default('serving_default')
    @JsonKey(defaultValue: 'serving_default', name: 'signature_name')
        String signatureName,
    @Default([]) @JsonKey(defaultValue: [], name: 'instances') List instances,
  }) = _PredictRequest;

  factory PredictRequest.fromJson(Map<String, Object?> json) =>
      _$PredictRequestFromJson(json);
}
