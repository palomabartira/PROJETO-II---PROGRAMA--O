import json
from ver_produtos import Sapatos

class inserirProdutos():
    __arquivo = "sapatos.json"
        
    @classmethod
    def carregar(cls):
        try:
            with open(cls.__arquivo, "r", encoding="UTF-8") as arquivo:
                dado = json.load(arquivo)
                return dado
        except FileNotFoundError:
            return []  
        except json.JSONDecodeError:
            return []  

    @classmethod
    def salvar(cls, dado):
        try:
            with open(cls.__arquivo, "w", encoding="UTF-8") as arquivo:
                json.dump(dado, arquivo, indent=4, ensure_ascii=False)
                return True
        except Exception as e:
            print(f"❌ Erro ao salvar o arquivo: {e}")
            return False
      
class Carrinho:
    @classmethod
    def inserirCarrinho(cls):
        try:
            id = int(input("🆔 Informe o id do sapato que deseja adicionar no carrinho:"))
            if 0 < id <= len(Sapatos.catalogo):
                carrinho = Sapatos.catalago[id - 1]
                lista = inserirProdutos.carregar()
                lista.append(carrinho)
                inserirProdutos.salvar(lista)
                print("✔ Sapato adicionado ao carrinho com sucesso!")

            else:
                print("❌ ID inválido! O sapato não foi localizado!")

        except ValueError: 
            print("❌ Valor inválido!")    
        
Carrinho.inserirCarrinho()