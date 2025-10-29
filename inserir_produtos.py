import json
from ver_produtos import Sapatos

class Carrinho:
    """Essa classe tem como objetivo gerenciar a persistência de dados do carrinho de compras,
    utilizando o arquivo Json. Desse modo, o intuito é carregar, salvar e manipular a lista de produtos 
    no carrinho, permitindo a inserção de novos itens por meio de seus IDs, com verificações de integridade."""
    
    __arquivo = "sapatos.json"
    
    @classmethod
    def carregar(cls):
        """Carrega e retorna a lista de sapatos armazenada no arquivo JSON. Se o arquivo 
        não for encontrado ou estiver corrompido, retorna uma lista vazia."""
        try:
            with open(cls.__arquivo, "r", encoding="UTF-8") as arquivo:
                dado = json.load(arquivo)
                return dado
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @classmethod
    def salvar(cls, dado):
        """Salva a lista de dados no arquivo Json"""
        try:
            with open(cls.__arquivo, "w", encoding="UTF-8") as arquivo:
                json.dump(dado, arquivo, indent=4, ensure_ascii=False)
                return True
        except Exception as e:
            print(f"\n \033[31m❌ Erro ao salvar o arquivo: {e}\033[0m")
            return False

    @classmethod
    def inserirProdutos(cls):
        """Solicita o ID do sapato para ser inserido no carrinho e, logo após, adiciona à lista, 
        salvando no arquivo Json."""
        try:
            id = int(input("🆔 Informe o id do sapato que deseja adicionar no carrinho: "))

            if 0 < id <= len(Sapatos.catalogo):
                carrinho = Sapatos.catalogo[id - 1]
                lista = cls.carregar()
                lista.append(carrinho)
                cls.salvar(lista)
                print("\n \033[32m✔ Sapato adicionado ao carrinho com sucesso!\033[0m")
            else:
                print("\n \033[31m❌ ID inválido! O sapato não foi localizado!\033[0m")

        except ValueError:
           print("\n \033[31m❌ Valor inválido!\033[0m")
