# import os
# import json
# from inserir_produtos import Carrinho

# class Remover:
#     """Essa classe tem como objetivo solicitar o id do sapato que deseja ser removido e, consequentemente,
#     apagá - lo do arquivo Json. Para isso, são feitas diversas verificações a fim de testar 
#     se o ID é um número inteiro, cadastrado, comrompido ou inválido. Caso o ID esteja correto, 
#     o produto será apagado."""

#     def __init__(self):
#         """Remove um sapato do arquivo Json com base no ID fornecido pelo usuário"""

#         try:
#             id_sapato = int(input("🆔 Informe o ID do sapato que deseja excluir:"))
            
#         except ValueError:
#             print("\n \033[31m❌ O ID deve ser um número inteiro!\033[0m")
#             return
        
#         if not os.path.exists(self.__arquivo):
#             print("\n \033[31m❌ Esse ID não está cadastrado!\033[0m")
#             return
        
#         try:
#             with open(self.__arquivo, "r", encoding="UTF-8") as dado:
#                 sapatos = json.load(dado)
        
#         except json.JSONDecodeError:
#             print(f"\n\033[31m☠️ Erro ao ler o arquivo {self.__arquivo}. O arquivo pode estar vazio ou corrompido!\033[0m")
#             return
        
#         except Exception as e:
#             print(f"\n\033[31m❌ Ocorreu um erro ao ler o arquivo: {e}!\033[0m")
#             return
        
#         sapato_encontrado = None
#         for i, sapato in enumerate(sapatos):
#             if sapato.get("id") == id_sapato:
#                 sapato_encontrado = i
#                 break
            
#         if sapato_encontrado is None:
#             print(f"\n\033[31m❌ O ID fornecido não foi encontrado no catálogo de sapatos!\033[0m")
#             return
        
#         sapato_removido = sapatos.pop(sapato_encontrado)
        
#         try:
          
#             with open(self.__arquivo, "w", encoding="UTF-8") as arquivo:
#                 json.dump(sapatos, arquivo, ensure_ascii=False, indent=4)
#         except Exception as e:
#              print(f"\n \033[31m❌ Ocorreu um erro ao escrever no arquivo: {e}\033[0m")
#              return
            
#         nome_sapato = sapato_removido.get('nome', sapato_removido.get('modelo', 'Item Desconhecido'))
#         print(f"\n \033[32m✔ O sapato '{nome_sapato}' (ID: {sapato_removido.get('id', id_sapato)}) foi excluído! \033[0m")

import os
import json
# from inserir_produtos import Carrinho # Não é usada

class Remover:
    """Essa classe tem como objetivo solicitar o id do sapato que deseja ser removido e, consequentemente,
    apagá - lo do arquivo Json do carrinho do usuário."""

    def __init__(self, usuario): # <--- Adicionar 'usuario' aqui
        """Remove um sapato do arquivo Json do carrinho com base no ID fornecido pelo usuário"""

        # O arquivo agora é o carrinho do usuário logado
        self.__arquivo = f"carrinho_{usuario}.json" # <--- Mudar a definição do arquivo
        
        try:
            id_sapato = int(input("🆔 Informe o ID do sapato que deseja excluir do carrinho:"))
            
        except ValueError:
            print("\n \033[31m❌ O ID deve ser um número inteiro!\033[0m")
            return
        
        if not os.path.exists(self.__arquivo):
            print(f"\n \033[31m❌ O seu carrinho está vazio ou o arquivo '{self.__arquivo}' não foi encontrado!\033[0m")
            return
        
        try:
            with open(self.__arquivo, "r", encoding="UTF-8") as dado:
                sapatos = json.load(dado)
        
        except json.JSONDecodeError:
            print(f"\n\033[31m☠️ Erro ao ler o arquivo {self.__arquivo}. O arquivo pode estar vazio ou corrompido!\033[0m")
            return
        
        except Exception as e:
            print(f"\n\033[31m❌ Ocorreu um erro ao ler o arquivo: {e}!\033[0m")
            return
        
        # --------------------------------------------------------------------------------------
        # A lógica de remoção precisa ser ajustada, pois o arquivo não tem o catálogo completo, 
        # mas apenas os itens do carrinho. Buscaremos o item no *carrinho*.
        # --------------------------------------------------------------------------------------
        
        sapato_encontrado_index = None
        for i, item in enumerate(sapatos):
            if item.get("id") == id_sapato:
                sapato_encontrado_index = i
                break
            
        if sapato_encontrado_index is None:
            print(f"\n\033[31m❌ O ID fornecido não foi encontrado no seu carrinho!\033[0m")
            return
        
        sapato_removido = sapatos.pop(sapato_encontrado_index)
        
        try:
            
            with open(self.__arquivo, "w", encoding="UTF-8") as arquivo:
                json.dump(sapatos, arquivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"\n \033[31m❌ Ocorreu um erro ao escrever no arquivo: {e}\033[0m")
            return
            
        nome_sapato = sapato_removido.get('nome', 'Item Desconhecido')
        print(f"\n \033[32m✔ O sapato '{nome_sapato}' (ID: {sapato_removido.get('id', id_sapato)}) foi excluído do carrinho! \033[0m")