import 'package:hooks_riverpod/hooks_riverpod.dart';

import '../../features/initialization/initialized_manager.dart';

final mainManagerProvider = Provider(
  (ref) => MainManager([]),
);

class MainManager {
  List<InitializedManager> managers;

  MainManager(this.managers);

  Future<void> init() async {
    for (var manager in managers) {
      manager.init();
    }
  }

  Future<void> dispose() async {
    for (var manager in managers) {
      manager.dispose();
    }
  }
}
