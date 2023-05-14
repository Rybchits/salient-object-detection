// coverage:ignore-file
// GENERATED CODE - DO NOT MODIFY BY HAND
// ignore_for_file: type=lint
// ignore_for_file: unused_element, deprecated_member_use, deprecated_member_use_from_same_package, use_function_type_syntax_for_parameters, unnecessary_const, avoid_init_to_null, invalid_override_different_default_values_named, prefer_expression_function_bodies, annotate_overrides, invalid_annotation_target, unnecessary_question_mark

part of 'display_state.dart';

// **************************************************************************
// FreezedGenerator
// **************************************************************************

T _$identity<T>(T value) => value;

final _privateConstructorUsedError = UnsupportedError(
    'It seems like you constructed your class using `MyClass._()`. This constructor is only meant to be used by freezed and you are not supposed to need it nor use it.\nPlease check the documentation here for more information: https://github.com/rrousselGit/freezed#custom-getters-and-methods');

/// @nodoc
mixin _$LabeledImage {
  Image? get image => throw _privateConstructorUsedError;
  String? get label => throw _privateConstructorUsedError;

  @JsonKey(ignore: true)
  $LabeledImageCopyWith<LabeledImage> get copyWith =>
      throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $LabeledImageCopyWith<$Res> {
  factory $LabeledImageCopyWith(
          LabeledImage value, $Res Function(LabeledImage) then) =
      _$LabeledImageCopyWithImpl<$Res, LabeledImage>;
  @useResult
  $Res call({Image? image, String? label});
}

/// @nodoc
class _$LabeledImageCopyWithImpl<$Res, $Val extends LabeledImage>
    implements $LabeledImageCopyWith<$Res> {
  _$LabeledImageCopyWithImpl(this._value, this._then);

  // ignore: unused_field
  final $Val _value;
  // ignore: unused_field
  final $Res Function($Val) _then;

  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? image = freezed,
    Object? label = freezed,
  }) {
    return _then(_value.copyWith(
      image: freezed == image
          ? _value.image
          : image // ignore: cast_nullable_to_non_nullable
              as Image?,
      label: freezed == label
          ? _value.label
          : label // ignore: cast_nullable_to_non_nullable
              as String?,
    ) as $Val);
  }
}

/// @nodoc
abstract class _$$_LabeledImageCopyWith<$Res>
    implements $LabeledImageCopyWith<$Res> {
  factory _$$_LabeledImageCopyWith(
          _$_LabeledImage value, $Res Function(_$_LabeledImage) then) =
      __$$_LabeledImageCopyWithImpl<$Res>;
  @override
  @useResult
  $Res call({Image? image, String? label});
}

/// @nodoc
class __$$_LabeledImageCopyWithImpl<$Res>
    extends _$LabeledImageCopyWithImpl<$Res, _$_LabeledImage>
    implements _$$_LabeledImageCopyWith<$Res> {
  __$$_LabeledImageCopyWithImpl(
      _$_LabeledImage _value, $Res Function(_$_LabeledImage) _then)
      : super(_value, _then);

  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? image = freezed,
    Object? label = freezed,
  }) {
    return _then(_$_LabeledImage(
      image: freezed == image
          ? _value.image
          : image // ignore: cast_nullable_to_non_nullable
              as Image?,
      label: freezed == label
          ? _value.label
          : label // ignore: cast_nullable_to_non_nullable
              as String?,
    ));
  }
}

/// @nodoc

class _$_LabeledImage implements _LabeledImage {
  _$_LabeledImage({this.image, this.label = ''});

  @override
  final Image? image;
  @override
  @JsonKey()
  final String? label;

  @override
  String toString() {
    return 'LabeledImage(image: $image, label: $label)';
  }

  @override
  bool operator ==(dynamic other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$_LabeledImage &&
            const DeepCollectionEquality().equals(other.image, image) &&
            (identical(other.label, label) || other.label == label));
  }

  @override
  int get hashCode => Object.hash(
      runtimeType, const DeepCollectionEquality().hash(image), label);

  @JsonKey(ignore: true)
  @override
  @pragma('vm:prefer-inline')
  _$$_LabeledImageCopyWith<_$_LabeledImage> get copyWith =>
      __$$_LabeledImageCopyWithImpl<_$_LabeledImage>(this, _$identity);
}

abstract class _LabeledImage implements LabeledImage {
  factory _LabeledImage({final Image? image, final String? label}) =
      _$_LabeledImage;

  @override
  Image? get image;
  @override
  String? get label;
  @override
  @JsonKey(ignore: true)
  _$$_LabeledImageCopyWith<_$_LabeledImage> get copyWith =>
      throw _privateConstructorUsedError;
}

/// @nodoc
mixin _$DisplayState {
  List<LabeledImage> get images => throw _privateConstructorUsedError;
  bool get isFetching => throw _privateConstructorUsedError;
  String? get displayTitle => throw _privateConstructorUsedError;

  @JsonKey(ignore: true)
  $DisplayStateCopyWith<DisplayState> get copyWith =>
      throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $DisplayStateCopyWith<$Res> {
  factory $DisplayStateCopyWith(
          DisplayState value, $Res Function(DisplayState) then) =
      _$DisplayStateCopyWithImpl<$Res, DisplayState>;
  @useResult
  $Res call({List<LabeledImage> images, bool isFetching, String? displayTitle});
}

/// @nodoc
class _$DisplayStateCopyWithImpl<$Res, $Val extends DisplayState>
    implements $DisplayStateCopyWith<$Res> {
  _$DisplayStateCopyWithImpl(this._value, this._then);

  // ignore: unused_field
  final $Val _value;
  // ignore: unused_field
  final $Res Function($Val) _then;

  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? images = null,
    Object? isFetching = null,
    Object? displayTitle = freezed,
  }) {
    return _then(_value.copyWith(
      images: null == images
          ? _value.images
          : images // ignore: cast_nullable_to_non_nullable
              as List<LabeledImage>,
      isFetching: null == isFetching
          ? _value.isFetching
          : isFetching // ignore: cast_nullable_to_non_nullable
              as bool,
      displayTitle: freezed == displayTitle
          ? _value.displayTitle
          : displayTitle // ignore: cast_nullable_to_non_nullable
              as String?,
    ) as $Val);
  }
}

/// @nodoc
abstract class _$$_DisplayStateCopyWith<$Res>
    implements $DisplayStateCopyWith<$Res> {
  factory _$$_DisplayStateCopyWith(
          _$_DisplayState value, $Res Function(_$_DisplayState) then) =
      __$$_DisplayStateCopyWithImpl<$Res>;
  @override
  @useResult
  $Res call({List<LabeledImage> images, bool isFetching, String? displayTitle});
}

/// @nodoc
class __$$_DisplayStateCopyWithImpl<$Res>
    extends _$DisplayStateCopyWithImpl<$Res, _$_DisplayState>
    implements _$$_DisplayStateCopyWith<$Res> {
  __$$_DisplayStateCopyWithImpl(
      _$_DisplayState _value, $Res Function(_$_DisplayState) _then)
      : super(_value, _then);

  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? images = null,
    Object? isFetching = null,
    Object? displayTitle = freezed,
  }) {
    return _then(_$_DisplayState(
      images: null == images
          ? _value._images
          : images // ignore: cast_nullable_to_non_nullable
              as List<LabeledImage>,
      isFetching: null == isFetching
          ? _value.isFetching
          : isFetching // ignore: cast_nullable_to_non_nullable
              as bool,
      displayTitle: freezed == displayTitle
          ? _value.displayTitle
          : displayTitle // ignore: cast_nullable_to_non_nullable
              as String?,
    ));
  }
}

/// @nodoc

class _$_DisplayState implements _DisplayState {
  _$_DisplayState(
      {final List<LabeledImage> images = const [],
      this.isFetching = false,
      this.displayTitle = ''})
      : _images = images;

  final List<LabeledImage> _images;
  @override
  @JsonKey()
  List<LabeledImage> get images {
    if (_images is EqualUnmodifiableListView) return _images;
    // ignore: implicit_dynamic_type
    return EqualUnmodifiableListView(_images);
  }

  @override
  @JsonKey()
  final bool isFetching;
  @override
  @JsonKey()
  final String? displayTitle;

  @override
  String toString() {
    return 'DisplayState(images: $images, isFetching: $isFetching, displayTitle: $displayTitle)';
  }

  @override
  bool operator ==(dynamic other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$_DisplayState &&
            const DeepCollectionEquality().equals(other._images, _images) &&
            (identical(other.isFetching, isFetching) ||
                other.isFetching == isFetching) &&
            (identical(other.displayTitle, displayTitle) ||
                other.displayTitle == displayTitle));
  }

  @override
  int get hashCode => Object.hash(runtimeType,
      const DeepCollectionEquality().hash(_images), isFetching, displayTitle);

  @JsonKey(ignore: true)
  @override
  @pragma('vm:prefer-inline')
  _$$_DisplayStateCopyWith<_$_DisplayState> get copyWith =>
      __$$_DisplayStateCopyWithImpl<_$_DisplayState>(this, _$identity);
}

abstract class _DisplayState implements DisplayState {
  factory _DisplayState(
      {final List<LabeledImage> images,
      final bool isFetching,
      final String? displayTitle}) = _$_DisplayState;

  @override
  List<LabeledImage> get images;
  @override
  bool get isFetching;
  @override
  String? get displayTitle;
  @override
  @JsonKey(ignore: true)
  _$$_DisplayStateCopyWith<_$_DisplayState> get copyWith =>
      throw _privateConstructorUsedError;
}
