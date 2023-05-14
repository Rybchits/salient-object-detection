import 'package:client/features/object_detection/models/detection_state.dart';
import 'package:flutter/material.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';

import '../manager.dart';

class DetectObjectButton extends ConsumerWidget {
  static const sendRequestTitle = 'Найти основной объект';

  const DetectObjectButton({super.key});

  @override
  Widget build(context, ref) {
    final manager = ref.watch(objectDetectionManagerProvider);

    return StreamBuilder<DetectionState?>(
        stream: manager.stream,
        builder: (context, snapshot) {
          return ElevatedButton(

            onPressed: snapshot.data is DetectionStateLoading
                ? null
                : manager.predictOnSelectedFile,
            style: ElevatedButton.styleFrom(
              elevation: 12.0,
              backgroundColor: Colors.teal,
              textStyle: const TextStyle(
                color: Colors.white,
                fontSize: 18,
              ),
            ),
            child: const Text(
              sendRequestTitle,
            ),
          );
        });
  }
}
