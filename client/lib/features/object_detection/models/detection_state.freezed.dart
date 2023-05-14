// coverage:ignore-file
// GENERATED CODE - DO NOT MODIFY BY HAND
// ignore_for_file: type=lint
// ignore_for_file: unused_element, deprecated_member_use, deprecated_member_use_from_same_package, use_function_type_syntax_for_parameters, unnecessary_const, avoid_init_to_null, invalid_override_different_default_values_named, prefer_expression_function_bodies, annotate_overrides, invalid_annotation_target, unnecessary_question_mark

part of 'detection_state.dart';

// **************************************************************************
// FreezedGenerator
// **************************************************************************

T _$identity<T>(T value) => value;

final _privateConstructorUsedError = UnsupportedError(
    'It seems like you constructed your class using `MyClass._()`. This constructor is only meant to be used by freezed and you are not supposed to need it nor use it.\nPlease check the documentation here for more information: https://github.com/rrousselGit/freezed#custom-getters-and-methods');

DetectionState _$DetectionStateFromJson(Map<String, dynamic> json) {
  switch (json['type']) {
    case 'success':
      return DetectionStateSuccess.fromJson(json);
    case 'error':
      return DetectionStateError.fromJson(json);
    case 'loading':
      return DetectionStateLoading.fromJson(json);

    default:
      throw CheckedFromJsonException(json, 'type', 'DetectionState',
          'Invalid union type "${json['type']}"!');
  }
}

/// @nodoc
mixin _$DetectionState {
  @optionalTypeArgs
  TResult when<TResult extends Object?>({
    required TResult Function(
            List<List<List<int>>> sourceImage, List<List<List<int>>> predMask)
        success,
    required TResult Function(String message) error,
    required TResult Function() loading,
  }) =>
      throw _privateConstructorUsedError;
  @optionalTypeArgs
  TResult? whenOrNull<TResult extends Object?>({
    TResult? Function(
            List<List<List<int>>> sourceImage, List<List<List<int>>> predMask)?
        success,
    TResult? Function(String message)? error,
    TResult? Function()? loading,
  }) =>
      throw _privateConstructorUsedError;
  @optionalTypeArgs
  TResult maybeWhen<TResult extends Object?>({
    TResult Function(
            List<List<List<int>>> sourceImage, List<List<List<int>>> predMask)?
        success,
    TResult Function(String message)? error,
    TResult Function()? loading,
    required TResult orElse(),
  }) =>
      throw _privateConstructorUsedError;
  @optionalTypeArgs
  TResult map<TResult extends Object?>({
    required TResult Function(DetectionStateSuccess value) success,
    required TResult Function(DetectionStateError value) error,
    required TResult Function(DetectionStateLoading value) loading,
  }) =>
      throw _privateConstructorUsedError;
  @optionalTypeArgs
  TResult? mapOrNull<TResult extends Object?>({
    TResult? Function(DetectionStateSuccess value)? success,
    TResult? Function(DetectionStateError value)? error,
    TResult? Function(DetectionStateLoading value)? loading,
  }) =>
      throw _privateConstructorUsedError;
  @optionalTypeArgs
  TResult maybeMap<TResult extends Object?>({
    TResult Function(DetectionStateSuccess value)? success,
    TResult Function(DetectionStateError value)? error,
    TResult Function(DetectionStateLoading value)? loading,
    required TResult orElse(),
  }) =>
      throw _privateConstructorUsedError;
  Map<String, dynamic> toJson() => throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $DetectionStateCopyWith<$Res> {
  factory $DetectionStateCopyWith(
          DetectionState value, $Res Function(DetectionState) then) =
      _$DetectionStateCopyWithImpl<$Res, DetectionState>;
}

/// @nodoc
class _$DetectionStateCopyWithImpl<$Res, $Val extends DetectionState>
    implements $DetectionStateCopyWith<$Res> {
  _$DetectionStateCopyWithImpl(this._value, this._then);

  // ignore: unused_field
  final $Val _value;
  // ignore: unused_field
  final $Res Function($Val) _then;
}

/// @nodoc
abstract class _$$DetectionStateSuccessCopyWith<$Res> {
  factory _$$DetectionStateSuccessCopyWith(_$DetectionStateSuccess value,
          $Res Function(_$DetectionStateSuccess) then) =
      __$$DetectionStateSuccessCopyWithImpl<$Res>;
  @useResult
  $Res call(
      {List<List<List<int>>> sourceImage, List<List<List<int>>> predMask});
}

/// @nodoc
class __$$DetectionStateSuccessCopyWithImpl<$Res>
    extends _$DetectionStateCopyWithImpl<$Res, _$DetectionStateSuccess>
    implements _$$DetectionStateSuccessCopyWith<$Res> {
  __$$DetectionStateSuccessCopyWithImpl(_$DetectionStateSuccess _value,
      $Res Function(_$DetectionStateSuccess) _then)
      : super(_value, _then);

  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? sourceImage = null,
    Object? predMask = null,
  }) {
    return _then(_$DetectionStateSuccess(
      null == sourceImage
          ? _value._sourceImage
          : sourceImage // ignore: cast_nullable_to_non_nullable
              as List<List<List<int>>>,
      null == predMask
          ? _value._predMask
          : predMask // ignore: cast_nullable_to_non_nullable
              as List<List<List<int>>>,
    ));
  }
}

/// @nodoc
@JsonSerializable()
class _$DetectionStateSuccess implements DetectionStateSuccess {
  const _$DetectionStateSuccess(final List<List<List<int>>> sourceImage,
      final List<List<List<int>>> predMask,
      {final String? $type})
      : _sourceImage = sourceImage,
        _predMask = predMask,
        $type = $type ?? 'success';

  factory _$DetectionStateSuccess.fromJson(Map<String, dynamic> json) =>
      _$$DetectionStateSuccessFromJson(json);

  final List<List<List<int>>> _sourceImage;
  @override
  List<List<List<int>>> get sourceImage {
    if (_sourceImage is EqualUnmodifiableListView) return _sourceImage;
    // ignore: implicit_dynamic_type
    return EqualUnmodifiableListView(_sourceImage);
  }

  final List<List<List<int>>> _predMask;
  @override
  List<List<List<int>>> get predMask {
    if (_predMask is EqualUnmodifiableListView) return _predMask;
    // ignore: implicit_dynamic_type
    return EqualUnmodifiableListView(_predMask);
  }

  @JsonKey(name: 'type')
  final String $type;

  @override
  String toString() {
    return 'DetectionState.success(sourceImage: $sourceImage, predMask: $predMask)';
  }

  @override
  bool operator ==(dynamic other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$DetectionStateSuccess &&
            const DeepCollectionEquality()
                .equals(other._sourceImage, _sourceImage) &&
            const DeepCollectionEquality().equals(other._predMask, _predMask));
  }

  @JsonKey(ignore: true)
  @override
  int get hashCode => Object.hash(
      runtimeType,
      const DeepCollectionEquality().hash(_sourceImage),
      const DeepCollectionEquality().hash(_predMask));

  @JsonKey(ignore: true)
  @override
  @pragma('vm:prefer-inline')
  _$$DetectionStateSuccessCopyWith<_$DetectionStateSuccess> get copyWith =>
      __$$DetectionStateSuccessCopyWithImpl<_$DetectionStateSuccess>(
          this, _$identity);

  @override
  @optionalTypeArgs
  TResult when<TResult extends Object?>({
    required TResult Function(
            List<List<List<int>>> sourceImage, List<List<List<int>>> predMask)
        success,
    required TResult Function(String message) error,
    required TResult Function() loading,
  }) {
    return success(sourceImage, predMask);
  }

  @override
  @optionalTypeArgs
  TResult? whenOrNull<TResult extends Object?>({
    TResult? Function(
            List<List<List<int>>> sourceImage, List<List<List<int>>> predMask)?
        success,
    TResult? Function(String message)? error,
    TResult? Function()? loading,
  }) {
    return success?.call(sourceImage, predMask);
  }

  @override
  @optionalTypeArgs
  TResult maybeWhen<TResult extends Object?>({
    TResult Function(
            List<List<List<int>>> sourceImage, List<List<List<int>>> predMask)?
        success,
    TResult Function(String message)? error,
    TResult Function()? loading,
    required TResult orElse(),
  }) {
    if (success != null) {
      return success(sourceImage, predMask);
    }
    return orElse();
  }

  @override
  @optionalTypeArgs
  TResult map<TResult extends Object?>({
    required TResult Function(DetectionStateSuccess value) success,
    required TResult Function(DetectionStateError value) error,
    required TResult Function(DetectionStateLoading value) loading,
  }) {
    return success(this);
  }

  @override
  @optionalTypeArgs
  TResult? mapOrNull<TResult extends Object?>({
    TResult? Function(DetectionStateSuccess value)? success,
    TResult? Function(DetectionStateError value)? error,
    TResult? Function(DetectionStateLoading value)? loading,
  }) {
    return success?.call(this);
  }

  @override
  @optionalTypeArgs
  TResult maybeMap<TResult extends Object?>({
    TResult Function(DetectionStateSuccess value)? success,
    TResult Function(DetectionStateError value)? error,
    TResult Function(DetectionStateLoading value)? loading,
    required TResult orElse(),
  }) {
    if (success != null) {
      return success(this);
    }
    return orElse();
  }

  @override
  Map<String, dynamic> toJson() {
    return _$$DetectionStateSuccessToJson(
      this,
    );
  }
}

abstract class DetectionStateSuccess implements DetectionState {
  const factory DetectionStateSuccess(final List<List<List<int>>> sourceImage,
      final List<List<List<int>>> predMask) = _$DetectionStateSuccess;

  factory DetectionStateSuccess.fromJson(Map<String, dynamic> json) =
      _$DetectionStateSuccess.fromJson;

  List<List<List<int>>> get sourceImage;
  List<List<List<int>>> get predMask;
  @JsonKey(ignore: true)
  _$$DetectionStateSuccessCopyWith<_$DetectionStateSuccess> get copyWith =>
      throw _privateConstructorUsedError;
}

/// @nodoc
abstract class _$$DetectionStateErrorCopyWith<$Res> {
  factory _$$DetectionStateErrorCopyWith(_$DetectionStateError value,
          $Res Function(_$DetectionStateError) then) =
      __$$DetectionStateErrorCopyWithImpl<$Res>;
  @useResult
  $Res call({String message});
}

/// @nodoc
class __$$DetectionStateErrorCopyWithImpl<$Res>
    extends _$DetectionStateCopyWithImpl<$Res, _$DetectionStateError>
    implements _$$DetectionStateErrorCopyWith<$Res> {
  __$$DetectionStateErrorCopyWithImpl(
      _$DetectionStateError _value, $Res Function(_$DetectionStateError) _then)
      : super(_value, _then);

  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? message = null,
  }) {
    return _then(_$DetectionStateError(
      null == message
          ? _value.message
          : message // ignore: cast_nullable_to_non_nullable
              as String,
    ));
  }
}

/// @nodoc
@JsonSerializable()
class _$DetectionStateError implements DetectionStateError {
  const _$DetectionStateError(this.message, {final String? $type})
      : $type = $type ?? 'error';

  factory _$DetectionStateError.fromJson(Map<String, dynamic> json) =>
      _$$DetectionStateErrorFromJson(json);

  @override
  final String message;

  @JsonKey(name: 'type')
  final String $type;

  @override
  String toString() {
    return 'DetectionState.error(message: $message)';
  }

  @override
  bool operator ==(dynamic other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$DetectionStateError &&
            (identical(other.message, message) || other.message == message));
  }

  @JsonKey(ignore: true)
  @override
  int get hashCode => Object.hash(runtimeType, message);

  @JsonKey(ignore: true)
  @override
  @pragma('vm:prefer-inline')
  _$$DetectionStateErrorCopyWith<_$DetectionStateError> get copyWith =>
      __$$DetectionStateErrorCopyWithImpl<_$DetectionStateError>(
          this, _$identity);

  @override
  @optionalTypeArgs
  TResult when<TResult extends Object?>({
    required TResult Function(
            List<List<List<int>>> sourceImage, List<List<List<int>>> predMask)
        success,
    required TResult Function(String message) error,
    required TResult Function() loading,
  }) {
    return error(message);
  }

  @override
  @optionalTypeArgs
  TResult? whenOrNull<TResult extends Object?>({
    TResult? Function(
            List<List<List<int>>> sourceImage, List<List<List<int>>> predMask)?
        success,
    TResult? Function(String message)? error,
    TResult? Function()? loading,
  }) {
    return error?.call(message);
  }

  @override
  @optionalTypeArgs
  TResult maybeWhen<TResult extends Object?>({
    TResult Function(
            List<List<List<int>>> sourceImage, List<List<List<int>>> predMask)?
        success,
    TResult Function(String message)? error,
    TResult Function()? loading,
    required TResult orElse(),
  }) {
    if (error != null) {
      return error(message);
    }
    return orElse();
  }

  @override
  @optionalTypeArgs
  TResult map<TResult extends Object?>({
    required TResult Function(DetectionStateSuccess value) success,
    required TResult Function(DetectionStateError value) error,
    required TResult Function(DetectionStateLoading value) loading,
  }) {
    return error(this);
  }

  @override
  @optionalTypeArgs
  TResult? mapOrNull<TResult extends Object?>({
    TResult? Function(DetectionStateSuccess value)? success,
    TResult? Function(DetectionStateError value)? error,
    TResult? Function(DetectionStateLoading value)? loading,
  }) {
    return error?.call(this);
  }

  @override
  @optionalTypeArgs
  TResult maybeMap<TResult extends Object?>({
    TResult Function(DetectionStateSuccess value)? success,
    TResult Function(DetectionStateError value)? error,
    TResult Function(DetectionStateLoading value)? loading,
    required TResult orElse(),
  }) {
    if (error != null) {
      return error(this);
    }
    return orElse();
  }

  @override
  Map<String, dynamic> toJson() {
    return _$$DetectionStateErrorToJson(
      this,
    );
  }
}

abstract class DetectionStateError implements DetectionState {
  const factory DetectionStateError(final String message) =
      _$DetectionStateError;

  factory DetectionStateError.fromJson(Map<String, dynamic> json) =
      _$DetectionStateError.fromJson;

  String get message;
  @JsonKey(ignore: true)
  _$$DetectionStateErrorCopyWith<_$DetectionStateError> get copyWith =>
      throw _privateConstructorUsedError;
}

/// @nodoc
abstract class _$$DetectionStateLoadingCopyWith<$Res> {
  factory _$$DetectionStateLoadingCopyWith(_$DetectionStateLoading value,
          $Res Function(_$DetectionStateLoading) then) =
      __$$DetectionStateLoadingCopyWithImpl<$Res>;
}

/// @nodoc
class __$$DetectionStateLoadingCopyWithImpl<$Res>
    extends _$DetectionStateCopyWithImpl<$Res, _$DetectionStateLoading>
    implements _$$DetectionStateLoadingCopyWith<$Res> {
  __$$DetectionStateLoadingCopyWithImpl(_$DetectionStateLoading _value,
      $Res Function(_$DetectionStateLoading) _then)
      : super(_value, _then);
}

/// @nodoc
@JsonSerializable()
class _$DetectionStateLoading implements DetectionStateLoading {
  const _$DetectionStateLoading({final String? $type})
      : $type = $type ?? 'loading';

  factory _$DetectionStateLoading.fromJson(Map<String, dynamic> json) =>
      _$$DetectionStateLoadingFromJson(json);

  @JsonKey(name: 'type')
  final String $type;

  @override
  String toString() {
    return 'DetectionState.loading()';
  }

  @override
  bool operator ==(dynamic other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType && other is _$DetectionStateLoading);
  }

  @JsonKey(ignore: true)
  @override
  int get hashCode => runtimeType.hashCode;

  @override
  @optionalTypeArgs
  TResult when<TResult extends Object?>({
    required TResult Function(
            List<List<List<int>>> sourceImage, List<List<List<int>>> predMask)
        success,
    required TResult Function(String message) error,
    required TResult Function() loading,
  }) {
    return loading();
  }

  @override
  @optionalTypeArgs
  TResult? whenOrNull<TResult extends Object?>({
    TResult? Function(
            List<List<List<int>>> sourceImage, List<List<List<int>>> predMask)?
        success,
    TResult? Function(String message)? error,
    TResult? Function()? loading,
  }) {
    return loading?.call();
  }

  @override
  @optionalTypeArgs
  TResult maybeWhen<TResult extends Object?>({
    TResult Function(
            List<List<List<int>>> sourceImage, List<List<List<int>>> predMask)?
        success,
    TResult Function(String message)? error,
    TResult Function()? loading,
    required TResult orElse(),
  }) {
    if (loading != null) {
      return loading();
    }
    return orElse();
  }

  @override
  @optionalTypeArgs
  TResult map<TResult extends Object?>({
    required TResult Function(DetectionStateSuccess value) success,
    required TResult Function(DetectionStateError value) error,
    required TResult Function(DetectionStateLoading value) loading,
  }) {
    return loading(this);
  }

  @override
  @optionalTypeArgs
  TResult? mapOrNull<TResult extends Object?>({
    TResult? Function(DetectionStateSuccess value)? success,
    TResult? Function(DetectionStateError value)? error,
    TResult? Function(DetectionStateLoading value)? loading,
  }) {
    return loading?.call(this);
  }

  @override
  @optionalTypeArgs
  TResult maybeMap<TResult extends Object?>({
    TResult Function(DetectionStateSuccess value)? success,
    TResult Function(DetectionStateError value)? error,
    TResult Function(DetectionStateLoading value)? loading,
    required TResult orElse(),
  }) {
    if (loading != null) {
      return loading(this);
    }
    return orElse();
  }

  @override
  Map<String, dynamic> toJson() {
    return _$$DetectionStateLoadingToJson(
      this,
    );
  }
}

abstract class DetectionStateLoading implements DetectionState {
  const factory DetectionStateLoading() = _$DetectionStateLoading;

  factory DetectionStateLoading.fromJson(Map<String, dynamic> json) =
      _$DetectionStateLoading.fromJson;
}
