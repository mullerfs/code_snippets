int soma(int a, int b) {
  return a + b;
}

void soma2(int a, int b) {
  print(a + b);
}

int exec(int a, int b, int Function(int, int) fn) {
  return fn(a, b);
}

main() {
  final r = soma(5, 3);
  print('O valor da some é: $r');

  soma2(5, 4);

  print(exec(3, 4, soma));

  int r2 = exec(5, 3, (d, e) {
    return d - e;
  });
  print(r2);
}
