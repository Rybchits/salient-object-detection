import 'package:client/pages/main/page.dart';
import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';

void main() {
  runApp(
    const ProviderScope(
      child: MyApp(),
    ),
  );
}

class MyApp extends HookWidget {
  const MyApp({super.key});

  @override
  Widget build(context) {
    return MaterialApp(
      title: 'Демонстрационный клиент для ВКР',
      theme: ThemeData(
        primarySwatch: Colors.indigo,
      ),
      home: const MainPage(
        title: 'Демонстрационный клиент для ВКР',
      ),
    );
  }
}
