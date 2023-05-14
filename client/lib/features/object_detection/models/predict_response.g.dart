// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'predict_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$_PredictResponse _$$_PredictResponseFromJson(Map<String, dynamic> json) =>
    _$_PredictResponse(
      predictions: (json['predictions'] as List<dynamic>?)
              ?.map((e) => (e as List<dynamic>)
                  .map(
                      (e) => (e as List<dynamic>).map((e) => e as int).toList())
                  .toList())
              .toList() ??
          [],
    );

Map<String, dynamic> _$$_PredictResponseToJson(_$_PredictResponse instance) =>
    <String, dynamic>{
      'predictions': instance.predictions,
    };
