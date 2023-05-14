// coverage:ignore-file
// GENERATED CODE - DO NOT MODIFY BY HAND
// ignore_for_file: type=lint
// ignore_for_file: unused_element, deprecated_member_use, deprecated_member_use_from_same_package, use_function_type_syntax_for_parameters, unnecessary_const, avoid_init_to_null, invalid_override_different_default_values_named, prefer_expression_function_bodies, annotate_overrides, invalid_annotation_target, unnecessary_question_mark

part of 'predict_request.dart';

// **************************************************************************
// FreezedGenerator
// **************************************************************************

T _$identity<T>(T value) => value;

final _privateConstructorUsedError = UnsupportedError(
    'It seems like you constructed your class using `MyClass._()`. This constructor is only meant to be used by freezed and you are not supposed to need it nor use it.\nPlease check the documentation here for more information: https://github.com/rrousselGit/freezed#custom-getters-and-methods');

PredictRequest _$PredictRequestFromJson(Map<String, dynamic> json) {
  return _PredictRequest.fromJson(json);
}

/// @nodoc
mixin _$PredictRequest {
  @JsonKey(defaultValue: 'serving_default', name: 'signature_name')
  String get signatureName => throw _privateConstructorUsedError;
  @JsonKey(defaultValue: [], name: 'instances')
  List<dynamic> get instances => throw _privateConstructorUsedError;

  Map<String, dynamic> toJson() => throw _privateConstructorUsedError;
  @JsonKey(ignore: true)
  $PredictRequestCopyWith<PredictRequest> get copyWith =>
      throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $PredictRequestCopyWith<$Res> {
  factory $PredictRequestCopyWith(
          PredictRequest value, $Res Function(PredictRequest) then) =
      _$PredictRequestCopyWithImpl<$Res, PredictRequest>;
  @useResult
  $Res call(
      {@JsonKey(defaultValue: 'serving_default', name: 'signature_name')
          String signatureName,
      @JsonKey(defaultValue: [], name: 'instances')
          List<dynamic> instances});
}

/// @nodoc
class _$PredictRequestCopyWithImpl<$Res, $Val extends PredictRequest>
    implements $PredictRequestCopyWith<$Res> {
  _$PredictRequestCopyWithImpl(this._value, this._then);

  // ignore: unused_field
  final $Val _value;
  // ignore: unused_field
  final $Res Function($Val) _then;

  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? signatureName = null,
    Object? instances = null,
  }) {
    return _then(_value.copyWith(
      signatureName: null == signatureName
          ? _value.signatureName
          : signatureName // ignore: cast_nullable_to_non_nullable
              as String,
      instances: null == instances
          ? _value.instances
          : instances // ignore: cast_nullable_to_non_nullable
              as List<dynamic>,
    ) as $Val);
  }
}

/// @nodoc
abstract class _$$_PredictRequestCopyWith<$Res>
    implements $PredictRequestCopyWith<$Res> {
  factory _$$_PredictRequestCopyWith(
          _$_PredictRequest value, $Res Function(_$_PredictRequest) then) =
      __$$_PredictRequestCopyWithImpl<$Res>;
  @override
  @useResult
  $Res call(
      {@JsonKey(defaultValue: 'serving_default', name: 'signature_name')
          String signatureName,
      @JsonKey(defaultValue: [], name: 'instances')
          List<dynamic> instances});
}

/// @nodoc
class __$$_PredictRequestCopyWithImpl<$Res>
    extends _$PredictRequestCopyWithImpl<$Res, _$_PredictRequest>
    implements _$$_PredictRequestCopyWith<$Res> {
  __$$_PredictRequestCopyWithImpl(
      _$_PredictRequest _value, $Res Function(_$_PredictRequest) _then)
      : super(_value, _then);

  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? signatureName = null,
    Object? instances = null,
  }) {
    return _then(_$_PredictRequest(
      signatureName: null == signatureName
          ? _value.signatureName
          : signatureName // ignore: cast_nullable_to_non_nullable
              as String,
      instances: null == instances
          ? _value._instances
          : instances // ignore: cast_nullable_to_non_nullable
              as List<dynamic>,
    ));
  }
}

/// @nodoc
@JsonSerializable()
class _$_PredictRequest implements _PredictRequest {
  _$_PredictRequest(
      {@JsonKey(defaultValue: 'serving_default', name: 'signature_name')
          this.signatureName = 'serving_default',
      @JsonKey(defaultValue: [], name: 'instances')
          final List<dynamic> instances = const []})
      : _instances = instances;

  factory _$_PredictRequest.fromJson(Map<String, dynamic> json) =>
      _$$_PredictRequestFromJson(json);

  @override
  @JsonKey(defaultValue: 'serving_default', name: 'signature_name')
  final String signatureName;
  final List<dynamic> _instances;
  @override
  @JsonKey(defaultValue: [], name: 'instances')
  List<dynamic> get instances {
    if (_instances is EqualUnmodifiableListView) return _instances;
    // ignore: implicit_dynamic_type
    return EqualUnmodifiableListView(_instances);
  }

  @override
  String toString() {
    return 'PredictRequest(signatureName: $signatureName, instances: $instances)';
  }

  @override
  bool operator ==(dynamic other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$_PredictRequest &&
            (identical(other.signatureName, signatureName) ||
                other.signatureName == signatureName) &&
            const DeepCollectionEquality()
                .equals(other._instances, _instances));
  }

  @JsonKey(ignore: true)
  @override
  int get hashCode => Object.hash(runtimeType, signatureName,
      const DeepCollectionEquality().hash(_instances));

  @JsonKey(ignore: true)
  @override
  @pragma('vm:prefer-inline')
  _$$_PredictRequestCopyWith<_$_PredictRequest> get copyWith =>
      __$$_PredictRequestCopyWithImpl<_$_PredictRequest>(this, _$identity);

  @override
  Map<String, dynamic> toJson() {
    return _$$_PredictRequestToJson(
      this,
    );
  }
}

abstract class _PredictRequest implements PredictRequest {
  factory _PredictRequest(
      {@JsonKey(defaultValue: 'serving_default', name: 'signature_name')
          final String signatureName,
      @JsonKey(defaultValue: [], name: 'instances')
          final List<dynamic> instances}) = _$_PredictRequest;

  factory _PredictRequest.fromJson(Map<String, dynamic> json) =
      _$_PredictRequest.fromJson;

  @override
  @JsonKey(defaultValue: 'serving_default', name: 'signature_name')
  String get signatureName;
  @override
  @JsonKey(defaultValue: [], name: 'instances')
  List<dynamic> get instances;
  @override
  @JsonKey(ignore: true)
  _$$_PredictRequestCopyWith<_$_PredictRequest> get copyWith =>
      throw _privateConstructorUsedError;
}
