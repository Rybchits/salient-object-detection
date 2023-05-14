
import 'package:client/features/selected_files/state_holder.dart';
import 'package:file_picker/file_picker.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';

final selectedFilesManagerProvider = Provider(
  (ref) => SelectedFilesManager(
    ref.watch(selectedFilesStateHolderProvider.notifier),
  ),
);

class SelectedFilesManager {
  final SelectedFilesStateHolder _filesStateHolder;

  SelectedFilesManager(
    this._filesStateHolder,
  );

  void selectFile() async {
    var picked = await FilePicker.platform.pickFiles(
      type: FileType.image,
    );

    if (picked != null) {
      _filesStateHolder.updateFiles(picked.files);
    }
  }
}
