import 'package:client/features/display/controller.dart';
import 'package:client/features/display/ui/preview.dart';

import 'package:client/ui/display_image.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';

import '../models/display_state.dart';

class DisplayWidget extends ConsumerWidget {
  const DisplayWidget({super.key});

  @override
  Widget build(context, ref) {
    final controller = ref.watch(displayControllerProvider.notifier);

    return StreamBuilder<DisplayState>(
      stream: controller.stream,
      initialData: controller.currentState,
      builder: (context, snapshot) {
        final data = snapshot.data;
        if (data == null) {
          return const SizedBox.shrink();
        }
        return Column(
          children: [
            Text(
              data.displayTitle ?? '',
              style: TextStyle(
                fontSize: 24,
                fontWeight: FontWeight.bold,
                color: Theme.of(context).primaryColor,
              ),
            ),
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 24.0),
              child: data.images.isNotEmpty
                  ? Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: data.images
                          .map(
                            (element) => Padding(
                              padding:
                                  const EdgeInsets.symmetric(horizontal: 8.0),
                              child: DisplayImage(
                                element.image!,
                                title: element.label ?? '',
                                targetSide: 500,
                              ),
                            ),
                          )
                          .toList())
                  : const WebPreviewList(),
            ),
          ],
        );
      },
    );
  }
}
