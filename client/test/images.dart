import 'dart:typed_data';

import 'package:client/utils/images/manager.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  final manager = ImageTransformationsManager();

  group('Testing reshape image', () {
    test('Assert error', () {
      final input = Uint8List.fromList([1, 2, 3, 4]);
      try {
        final reshaped = manager.imageMatrixFromBytes(
          input,
          width: 3,
          height: 1,
          channels: 1,
        );
        fail('Not catch');
      } catch (e) {
        expect(true, true);
      }
    });

    test('Test 1', () {
      final input = Uint8List.fromList([1, 2, 3, 4]);
      try {
        final reshaped = manager.imageMatrixFromBytes(
          input,
          width: 4,
          height: 1,
          channels: 1,
        );
        expect(reshaped, [
          [[1], [2], [3], [4]
          ]
        ]);
      } catch (e) {
        fail('all okay');
      }
    });

    test('Test 2', () {
      final input = Uint8List.fromList([1, 2, 3, 4]);
      try {
        final reshaped = manager.imageMatrixFromBytes(
          input,
          width: 1,
          height: 4,
          channels: 1,
        );
        expect(reshaped, [
          [[1]],
          [[2]],
          [[3]],
          [[4]],
        ]);
      } catch (e) {
        fail('all okay');
      }
    });

    test('Test 3', () {
      final input = Uint8List.fromList([1, 2, 3, 4, 5, 6, 7, 8, 9]);
      try {
        final reshaped = manager.imageMatrixFromBytes(
            input,
            width: 3,
            height: 3,
            channels: 1
        );
        expect(reshaped, [
          [[1], [2], [3]],
          [[4], [5], [6]],
          [[7], [8], [9]]
        ]);
      } catch (e) {
        fail('all okay');
      }
    });

    test('Test 4', () {
      final input = Uint8List.fromList([1, 2, 3, 4, 5, 6, 7, 8, 9]);
      try {
        final reshaped = manager.imageMatrixFromBytes(
            input,
            width: 1,
            height: 3,
            channels: 3,
        );
        expect(reshaped, [
          [[1, 2, 3]],
          [[4, 5, 6]],
          [[7, 8, 9]]
        ]);
      } catch (e) {
        fail('all okay');
      }
    });
  });
}
