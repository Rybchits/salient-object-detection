// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'predict_request.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$_PredictRequest _$$_PredictRequestFromJson(Map<String, dynamic> json) =>
    _$_PredictRequest(
      signatureName: json['signature_name'] as String? ?? 'serving_default',
      instances: json['instances'] as List<dynamic>? ?? [],
    );

Map<String, dynamic> _$$_PredictRequestToJson(_$_PredictRequest instance) =>
    <String, dynamic>{
      'signature_name': instance.signatureName,
      'instances': instance.instances,
    };
