// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'detection_state.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$DetectionStateSuccess _$$DetectionStateSuccessFromJson(
        Map<String, dynamic> json) =>
    _$DetectionStateSuccess(
      (json['sourceImage'] as List<dynamic>)
          .map((e) => (e as List<dynamic>)
              .map((e) => (e as List<dynamic>).map((e) => e as int).toList())
              .toList())
          .toList(),
      (json['predMask'] as List<dynamic>)
          .map((e) => (e as List<dynamic>)
              .map((e) => (e as List<dynamic>).map((e) => e as int).toList())
              .toList())
          .toList(),
      $type: json['type'] as String?,
    );

Map<String, dynamic> _$$DetectionStateSuccessToJson(
        _$DetectionStateSuccess instance) =>
    <String, dynamic>{
      'sourceImage': instance.sourceImage,
      'predMask': instance.predMask,
      'type': instance.$type,
    };

_$DetectionStateError _$$DetectionStateErrorFromJson(
        Map<String, dynamic> json) =>
    _$DetectionStateError(
      json['message'] as String,
      $type: json['type'] as String?,
    );

Map<String, dynamic> _$$DetectionStateErrorToJson(
        _$DetectionStateError instance) =>
    <String, dynamic>{
      'message': instance.message,
      'type': instance.$type,
    };

_$DetectionStateLoading _$$DetectionStateLoadingFromJson(
        Map<String, dynamic> json) =>
    _$DetectionStateLoading(
      $type: json['type'] as String?,
    );

Map<String, dynamic> _$$DetectionStateLoadingToJson(
        _$DetectionStateLoading instance) =>
    <String, dynamic>{
      'type': instance.$type,
    };
