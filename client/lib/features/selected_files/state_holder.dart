import 'package:collection/collection.dart';
import 'package:file_picker/file_picker.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';

final selectedFilesStateHolderProvider =
    StateNotifierProvider<SelectedFilesStateHolder, List<PlatformFile>>(
  (ref) => SelectedFilesStateHolder(),
);

class SelectedFilesStateHolder extends StateNotifier<List<PlatformFile>> {
  SelectedFilesStateHolder() : super(const []);

  List<PlatformFile> get files => state;

  PlatformFile? get first => state.firstOrNull;

  void updateFiles(List<PlatformFile> files) => state = files;
}
