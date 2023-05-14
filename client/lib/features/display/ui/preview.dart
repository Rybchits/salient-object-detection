import 'package:flutter/cupertino.dart';
import 'package:flutter_hooks/flutter_hooks.dart';

class WebPreviewList extends HookWidget {
  const WebPreviewList({super.key});

  static const height = 320.0;
  static const width = 320.0;

  static const listPathImages = [
    'assets/images/preview_source_image.jpeg',
    'assets/images/preview_mask.jpeg',
    'assets/images/preview_masked_image.jpeg'
  ];

  @override
  Widget build(BuildContext context) => Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: listPathImages
            .map((e) => Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 8.0),
                  child: Image.asset(
                    e,
                    width: width,
                    height: height,
                  ),
                ))
            .toList(),
      );
}
