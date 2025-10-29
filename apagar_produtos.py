import os
import json

class Remover:
    """Essa classe tem como objetivo solicitar o id do sapato que deseja ser removido e, consequentemente,
    apagá - lo do arquivo Json. Para isso, são feitas diversas verificações a fim de testar 
    se o ID é um número inteiro, cadastrado, comrompido ou inválido. Caso o ID esteja correto, 
    o produto será apagado."""
    
    __arquivo = "sapatos.json"
    
    @classmethod
    def excluirSapatos(cls):
        """Remove um sapato do arquivo Json com base no ID fornecido pelo usuário"""
        try:
            id_sapato = int(input("🆔 Informe o ID do sapato que deseja excluir:"))
            
        except ValueError:
            print("\n \033[31m❌ O ID deve ser um número inteiro!\033[0m")
            return
        
        if not os.path.exists(cls.__arquivo):
            print("\n \033[31m❌ Esse ID não está cadastrado!\033[0m")
            return
        
        try:
            with open(cls.__arquivo, "r", encoding="UTF-8") as arquivo:
                sapatos = json.load(arquivo)
        
        except json.JSONDecodeError:
            print(f"\n \033[31m☠️ Erro ao ler o arquivo {cls.__arquivo}. O arquivo pode estar vazio ou corrompido!\033[0m")
            return
        
        except Exception as e:
            print(f"\n \033[31m❌ Ocorreu um erro ao ler o arquivo: {e}!\033[0m")
            return
        
        indice_sapato = id_sapato - 1
        
        if id_sapato < 1 or id_sapato > len(sapatos):
            print(f"\n \033[31m❌ O ID fornecido não foi encontrado no catálogo de sapatos!\033[0m")
            return
        
        sapato_removido = sapatos.pop(indice_sapato)
        
        try:
          
            with open(cls.__arquivo, "w", encoding="UTF-8") as arquivo:
                json.dump(sapatos, arquivo, ensure_ascii=False, indent=4)
        except Exception as e:
             print(f"\n \033[31m❌ Ocorreu um erro ao escrever no arquivo: {e}\033[0m")
             return
            
        nome_sapato = sapato_removido.get('nome', sapato_removido.get('modelo', 'Item Desconhecido'))
        print(f"\n \033[32m✔ O sapato '{nome_sapato}' (ID: {sapato_removido.get('id', id_sapato)}) foi excluído! \033[0m")