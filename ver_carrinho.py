import json
import os

class VerCarrinho:
    """ Essa classe tem como objetivo visualizar os itens que foram adicionados ao carrinho. Para isso,
    usamos uma estrutura de repetição para percorrer cada elemento da lista. """
    def __init__(self, usuario):
        self.usuario = usuario
        self.arquivo = f"carrinho_{self.usuario}.json"

    def exibir(self):
        if not os.path.exists(self.arquivo):
            print("\n🛒 Seu carrinho está vazio!")
            return

        with open(self.arquivo, "r", encoding="utf-8") as f:
            try:
                itens = json.load(f)
            except json.JSONDecodeError:
                itens = []

        if not itens:
            print("\n🛒 Seu carrinho está vazio!")
        else:
            print(f"\n🛍️  Itens no carrinho de {self.usuario}:\n")
            total = 0
            for p in itens:
                print(f"ID: {p['id']} - {p['nome']} - R$ {p['preco']:.2f}")
                total += p["preco"]
            print(f"\n💰 Total: R$ {total:.2f}")