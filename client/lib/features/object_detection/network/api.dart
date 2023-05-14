import 'dart:convert';
import 'package:flutter/foundation.dart' show kIsWeb;

import 'package:client/features/object_detection/models/predict_request.dart';
import 'package:client/features/object_detection/models/predict_response.dart';
import 'package:dio/browser.dart';
import 'package:dio/dio.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';

import '../../../utils/images/manager.dart';

final networkOptions = BaseOptions(
  baseUrl: 'http://127.0.0.1:8501/v1/models/u2net',
  connectTimeout: const Duration(milliseconds: 5000),
  receiveTimeout: const Duration(milliseconds: 3000),
);

final dioProvider = Provider(
    (_) => kIsWeb ? DioForBrowser(networkOptions) : Dio(networkOptions));

final objectDetectionApiProvider = Provider(
  (ref) => ObjectDetectionApi(
    ref.watch(dioProvider),
  ),
);

class ObjectDetectionApi {
  final Dio _dio;

  ObjectDetectionApi(this._dio);

  Future<void> checkModelVersionStatus() async => _dio.get('');

  Future<PredictResponse?> predictSalientObject(ImageMatrix matrix) async {
    final request = PredictRequest(instances: matrix);

    final response = await _dio
        .post(
          ':predict',
          data: jsonEncode(request.toJson()),
        )
        .then((value) => PredictResponse.fromJson(value.data));

    return response;
  }
}
