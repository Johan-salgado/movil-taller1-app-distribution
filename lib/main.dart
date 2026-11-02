import 'package:flutter/material.dart';

void main() {
  runApp(const MiApp());
}

class MiApp extends StatelessWidget {
  const MiApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Taller App Distribution',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
        useMaterial3: true,
      ),
      home: const PaginaPrincipal(),
    );
  }
}

class PaginaPrincipal extends StatefulWidget {
  const PaginaPrincipal({super.key});

  @override
  State<PaginaPrincipal> createState() => _PaginaPrincipalState();
}

class _PaginaPrincipalState extends State<PaginaPrincipal> {
  int contador = 0;

  void incrementar() {
    setState(() {
      contador++;
    });
  }

  void reiniciar() {
    setState(() {
      contador = 0;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Taller 1 - App Distribution'),
        backgroundColor: Colors.blue,
        foregroundColor: Colors.white,
        centerTitle: true,
      ),
      body: Center(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(24.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Card(
                elevation: 3,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
                child: const Padding(
                  padding: EdgeInsets.all(16.0),
                  child: Column(
                    children: [
                      Text(
                        'Programación Móvil - UCEVA',
                        style: TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      SizedBox(height: 8),
                      Text(
                        'Estudiante: Johan Eliu Salgado Castro',
                        style: TextStyle(fontSize: 15),
                      ),
                      SizedBox(height: 6),
                      Text(
                        'Grupo QA: QA_Clase',
                        style: TextStyle(fontSize: 14, color: Colors.black54),
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 30),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                decoration: BoxDecoration(
                  color: Colors.blue.shade50,
                  borderRadius: BorderRadius.circular(24),
                  border: Border.all(color: Colors.blue, width: 2),
                ),
                child: const Text(
                  'Versión 1.0.0',
                  style: TextStyle(
                    fontSize: 22,
                    fontWeight: FontWeight.bold,
                    color: Colors.blue,
                  ),
                ),
              ),
              const SizedBox(height: 30),
              const Text(
                'Contador de pruebas de distribución:',
                style: TextStyle(fontSize: 16),
              ),
              const SizedBox(height: 8),
              Text(
                '$contador',
                style: const TextStyle(
                  fontSize: 48,
                  fontWeight: FontWeight.bold,
                  color: Colors.blue,
                ),
              ),
              const SizedBox(height: 24),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  ElevatedButton.icon(
                    onPressed: incrementar,
                    icon: const Icon(Icons.add),
                    label: const Text('Incrementar'),
                  ),
                  const SizedBox(width: 12),
                  OutlinedButton.icon(
                    onPressed: reiniciar,
                    icon: const Icon(Icons.refresh),
                    label: const Text('Reiniciar'),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
