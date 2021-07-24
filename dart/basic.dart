main() {
  print("Meu primeiro programa");
  int a = 3;
  double b = 3.1;
  var c = "sou uma string";
  c = '3';
  var nome = ['muller', 'leo', 'pedro', 'jeff', 'jonas'];
  nome.add('nick');
  nome.add('taylor');
  print(nome.length);
  print(nome);
  print(nome.isNotEmpty);
  print(nome.removeLast());
  print(nome);

  Set conjunto = {0, 1, 2, 3, 4, 5, 5, 5, 5};
  print(conjunto.length);
  print(conjunto is Set);

  Map<String, double> notas = {'Ana': 8, 'Pedro': 10, 'muller': 100};
  print(notas);
  for (var chave in notas.keys) {
    print('chave = $chave');
    print('chave2 = ' + chave);
  }
  for (var valor in notas.values) {
    print('valor = $valor');
  }

  for (var entradas in notas.entries) {
    print('chave:${entradas.key} - valor:${entradas.value}');
  }
}
