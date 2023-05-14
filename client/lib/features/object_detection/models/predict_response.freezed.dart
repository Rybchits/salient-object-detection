// coverage:ignore-file
// GENERATED CODE - DO NOT MODIFY BY HAND
// ignore_for_file: type=lint
// ignore_for_file: unused_element, deprecated_member_use, deprecated_member_use_from_same_package, use_function_type_syntax_for_parameters, unnecessary_const, avoid_init_to_null, invalid_override_different_default_values_named, prefer_expression_function_bodies, annotate_overrides, invalid_annotation_target, unnecessary_question_mark

part of 'predict_response.dart';

// **************************************************************************
// FreezedGenerator
// **************************************************************************

T _$identity<T>(T value) => value;

final _privateConstructorUsedError = UnsupportedError(
    'It seems like you constructed your class using `MyClass._()`. This constructor is only meant to be used by freezed and you are not supposed to need it nor use it.\nPlease check the documentation here for more information: https://github.com/rrousselGit/freezed#custom-getters-and-methods');

PredictResponse _$PredictResponseFromJson(Map<String, dynamic> json) {
  return _PredictResponse.fromJson(json);
}

/// @nodoc
mixin _$PredictResponse {
  @JsonKey(defaultValue: [], name: 'predictions')
  List<List<List<int>>> get predictions => throw _privateConstructorUsedError;

  Map<String, dynamic> toJson() => throw _privateConstructorUsedError;
  @JsonKey(ignore: true)
  $PredictResponseCopyWith<PredictResponse> get copyWith =>
      throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $PredictResponseCopyWith<$Res> {
  factory $PredictResponseCopyWith(
          PredictResponse value, $Res Function(PredictResponse) then) =
      _$PredictResponseCopyWithImpl<$Res, PredictResponse>;
  @useResult
  $Res call(
      {@JsonKey(defaultValue: [], name: 'predictions')
          List<List<List<int>>> predictions});
}

/// @nodoc
class _$PredictResponseCopyWithImpl<$Res, $Val extends PredictResponse>
    implements $PredictResponseCopyWith<$Res> {
  _$PredictResponseCopyWithImpl(this._value, this._then);

  // ignore: unused_field
  final $Val _value;
  // ignore: unused_field
  final $Res Function($Val) _then;

  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? predictions = null,
  }) {
    return _then(_value.copyWith(
      predictions: null == predictions
          ? _value.predictions
          : predictions // ignore: cast_nullable_to_non_nullable
              as List<List<List<int>>>,
    ) as $Val);
  }
}

/// @nodoc
abstract class _$$_PredictResponseCopyWith<$Res>
    implements $PredictResponseCopyWith<$Res> {
  factory _$$_PredictResponseCopyWith(
          _$_PredictResponse value, $Res Function(_$_PredictResponse) then) =
      __$$_PredictResponseCopyWithImpl<$Res>;
  @override
  @useResult
  $Res call(
      {@JsonKey(defaultValue: [], name: 'predictions')
          List<List<List<int>>> predictions});
}

/// @nodoc
class __$$_PredictResponseCopyWithImpl<$Res>
    extends _$PredictResponseCopyWithImpl<$Res, _$_PredictResponse>
    implements _$$_PredictResponseCopyWith<$Res> {
  __$$_PredictResponseCopyWithImpl(
      _$_PredictResponse _value, $Res Function(_$_PredictResponse) _then)
      : super(_value, _then);

  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? predictions = null,
  }) {
    return _then(_$_PredictResponse(
      predictions: null == predictions
          ? _value._predictions
          : predictions // ignore: cast_nullable_to_non_nullable
              as List<List<List<int>>>,
    ));
  }
}

/// @nodoc
@JsonSerializable()
class _$_PredictResponse implements _PredictResponse {
  _$_PredictResponse(
      {@JsonKey(defaultValue: [], name: 'predictions')
          final List<List<List<int>>> predictions = const []})
      : _predictions = predictions;

  factory _$_PredictResponse.fromJson(Map<String, dynamic> json) =>
      _$$_PredictResponseFromJson(json);

  final List<List<List<int>>> _predictions;
  @override
  @JsonKey(defaultValue: [], name: 'predictions')
  List<List<List<int>>> get predictions {
    if (_predictions is EqualUnmodifiableListView) return _predictions;
    // ignore: implicit_dynamic_type
    return EqualUnmodifiableListView(_predictions);
  }

  @override
  String toString() {
    return 'PredictResponse(predictions: $predictions)';
  }

  @override
  bool operator ==(dynamic other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$_PredictResponse &&
            const DeepCollectionEquality()
                .equals(other._predictions, _predictions));
  }

  @JsonKey(ignore: true)
  @override
  int get hashCode => Object.hash(
      runtimeType, const DeepCollectionEquality().hash(_predictions));

  @JsonKey(ignore: true)
  @override
  @pragma('vm:prefer-inline')
  _$$_PredictResponseCopyWith<_$_PredictResponse> get copyWith =>
      __$$_PredictResponseCopyWithImpl<_$_PredictResponse>(this, _$identity);

  @override
  Map<String, dynamic> toJson() {
    return _$$_PredictResponseToJson(
      this,
    );
  }
}

abstract class _PredictResponse implements PredictResponse {
  factory _PredictResponse(
      {@JsonKey(defaultValue: [], name: 'predictions')
          final List<List<List<int>>> predictions}) = _$_PredictResponse;

  factory _PredictResponse.fromJson(Map<String, dynamic> json) =
      _$_PredictResponse.fromJson;

  @override
  @JsonKey(defaultValue: [], name: 'predictions')
  List<List<List<int>>> get predictions;
  @override
  @JsonKey(ignore: true)
  _$$_PredictResponseCopyWith<_$_PredictResponse> get copyWith =>
      throw _privateConstructorUsedError;
}
