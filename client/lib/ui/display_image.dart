import 'package:flutter/widgets.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';
import 'package:image/image.dart' as img;

import '../utils/images/manager.dart';

class DisplayImage extends ConsumerWidget {
  const DisplayImage(
    this.image, {
    this.title = '',
    super.key,
  });

  final img.Image image;
  final String title;

  @override
  Widget build(context, ref) {
    final imageManager = ref.watch(imageManagerProvider);

    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [
        if (title.isNotEmpty)
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text(
              title,
              style: const TextStyle(fontWeight: FontWeight.w600, fontSize: 16),
            ),
          ),
        FutureBuilder(
          future: imageManager.convertImageToFlutterUi(image),
          builder: (context, snapshot) {
            if (snapshot.hasData) {
              return RawImage(image: snapshot.data);
            } else if (snapshot.hasError) {
              return const Text('Ошибка при загрузке');
            }
            return const Text('Загрузка...');
          },
        ),
      ],
    );
  }
}
