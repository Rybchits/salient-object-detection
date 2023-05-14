import 'package:client/features/object_detection/ui/detect_object_button.dart';
import 'package:client/features/selected_files/state_holder.dart';
import 'package:flutter/material.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';

import '../../features/display/ui/display.dart';
import '../../features/selected_files/ui/file_upload_button.dart';

class MainPage extends ConsumerWidget {
  const MainPage({
    super.key,
    required this.title,
  });

  final String title;

  @override
  Widget build(context, ref) {
    final selectedFilesStateHolder =
        ref.watch(selectedFilesStateHolderProvider);

    final imageSelected = selectedFilesStateHolder.isNotEmpty;

    return Scaffold(
      appBar: AppBar(
        title: Text(title),
      ),
      body: Container(
        decoration: const BoxDecoration(
          image: DecorationImage(
            image: AssetImage("assets/images/background.jpeg"),
            fit: BoxFit.cover,
          ),
        ),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const DisplayWidget(),
              const SizedBox(
                height: 16,
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Padding(
                    padding: EdgeInsets.all(8.0),
                    child: FileUploadButton(),
                  ),
                  if (imageSelected) const DetectObjectButton(),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
