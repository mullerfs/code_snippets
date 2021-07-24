class Produto {
  String nome = '';
  double preco = 0;

  Produto(String nome, double preco) {
    this.nome = nome;
    this.preco = preco;
  }
}

main() {
  var p1 = new Produto('mu', 0);
  p1.nome = "Muller best product ever";
  p1.preco = 12.50;
  print("O produto ${p1.nome} custa a bagatela de R\$${p1.preco}");

  var p2 = new Produto('Produto do concorrente', 23.89);
  print("O produto ${p2.nome} custa a bagatela de R\$${p2.preco}");
}
