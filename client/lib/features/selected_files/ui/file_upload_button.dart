import 'package:flutter/material.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';

import '../manager.dart';

class FileUploadButton extends ConsumerWidget {
  static const imageNotSelectedTitle = 'Выбрать изображение';

  const FileUploadButton({super.key});

  @override
  Widget build(context, ref) {
    final manager = ref.watch(selectedFilesManagerProvider);

    return ElevatedButton(
      onPressed: manager.selectFile,
      style: ElevatedButton.styleFrom(
        elevation: 12.0,
        textStyle: const TextStyle(
          color: Colors.white,
          fontSize: 18,
        ),
      ),
      child: const Text(imageNotSelectedTitle),
    );
  }
}
