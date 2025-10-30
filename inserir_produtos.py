import json
import os
from ver_produtos import Sapatos

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
            print(f"❌ Erro ao salvar o arquivo: {e}")

    def inserirProduto(self):
        """ Solicita o ID de um produto ao usuário e o adiciona ao carrinho,
        salvando a lista atualizada no arquivo JSON. """

        try:
            id = int(input("🆔 Informe o ID do sapato que deseja adicionar no carrinho: "))
            if 0 < id <= len(Sapatos.catalogo):
                produto = Sapatos.catalogo[id - 1]
                lista = self.carregar()

                item = {"id": produto.id, "nome": produto.nome, "preco": produto.preco}

                lista.append(item)
                self.salvar(lista)
                print("✔ Produto adicionado ao carrinho com sucesso!")
            else:
                print("❌ ID inválido!")
        except ValueError:
            print("❌ Valor inválido!")