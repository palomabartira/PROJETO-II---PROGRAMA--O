import json
import os
from ver_produtos import Sapatos
from ver_carrinho import VerCarrinho

class Carrinho:
    """ Representa o carrinho de compras de um usuário específico,
    gerenciando a persistência (carregar e salvar) e a inserção de produtos. """

    def __init__(self, usuario):
        """ Inicializa uma instância de Carrinho. """

        self.usuario = usuario
        self.arquivo = f"carrinho_{self.usuario}.json"

    def carregar(self):
        """ Carrega a lista de produtos do arquivo JSON do carrinho do usuário. """

        if os.path.exists(self.arquivo):
            try:
                with open(self.arquivo, "r", encoding="utf-8") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def salvar(self, lista):
        """ Salva a lista de produtos no arquivo JSON do carrinho do usuário. """

        try:
            with open(self.arquivo, "w", encoding="utf-8") as f:
                json.dump(lista, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"\n\033[31m❌ Erro ao salvar o arquivo: {e}\033[0m")

    def inserirProduto(self):
        """ Solicita o ID de um produto ao usuário e o adiciona ao carrinho,
        salvando a lista atualizada no arquivo JSON. """

        try:
            VerCarrinho(self.usuario).exibir()
            id = int(input("\n🆔 Informe o ID do sapato que deseja adicionar no carrinho: "))
            self.qtd_produto = int(input("\nQual é a quantidade desse sapato que você deseja adicionar no carrinho? "))

            if self.qtd_produto == 0:
                print("\n\033[31m❌ Quantidade inválida!\033[0m")

            if 0 < id <= len(Sapatos.catalogo):
                produto = Sapatos.catalogo[id - 1]
                lista = self.carregar()

                item = {"id": produto.id, "nome": produto.nome, "preco": produto.preco}

                for n in range(self.qtd_produto):
                    lista.append(item)
                    self.salvar(lista)
                    
                print(f"\n\033[32m✔ Produto '{produto.nome}' adicionado ao carrinho com sucesso!\033[0m")
            else:
                print("\n\033[31m❌ ID inválido!\033[0m")
        except ValueError:
            print("\n\033[31m❌ Valor inválido!\033[0m")