from ver_produtos import Sapatos
from inserir_produtos import Carrinho
from ver_carrinho import VerCarrinho
from cadastrar import Cadastrar
from apagar_produtos import Remover
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def menu(usuario):
    """ Exibe e gerencia o menu principal da Loja Virtual de Sapatos após o login. """

    while True:
        limpar_tela()

        print("=" *70)
        print("®️ 🅿️  Loja Virtual de Sapatos ®️ 🅿️".center(60))
        print("\033[3;34m Caminhe com a leveza de quem sabe ser única!\033[0m\n".center(70))
        print('''
              ----------👠 MENU 👠----------
            1️⃣  Ver Produtos
            2️⃣  Inserir Produtos no Carrinho
            3️⃣  Ver carrinho
            4️⃣  Apagar Produto
            5️⃣  Sair
              ''')
        
        opcao = input("⏮ Selecione uma opção no menu para continuar: ⏭  ")

        limpar_tela()

        if opcao == "1":
    
            print("-" * 70)
            print("⏮ Carregando catálogos... ⏭\n")
            Sapatos.verProdutos()

        elif opcao == "2":
            
            print("-" * 70)
            print("⏮ Carregando o carrinho... ⏭\n")
            Carrinho(usuario).inserirProduto()
          
        elif opcao == "3":
           
            print("-" * 70)
            print("⏮ Mostrando itens do seu carrinho... ⏭\n")
            VerCarrinho(usuario).exibir()
        
        elif opcao == "4":
            
            print("-" * 70)
            print("⏮ Removendo produtos do carrinho ⏭\n")
            Remover(usuario)

        elif opcao == "5":
         
            print("-" * 70)
            print("⏮ 👋 Saindo... Esperamos vê-lo em breve! ®️ 🅿️  ⏭\n")
            break
          
        else:
            print("\n\033[31m❌ Opção Inválida\033[0m")

        input("\nPressione ENTER para voltar ao menu...")


def inicio():
    """ Exibe e gerencia o menu inicial do sistema (Login/Cadastro/Sair). """
    
    limpar_tela()

    while True:
        limpar_tela()

        print("=" * 70)
        print("®️ 🅿️  Loja Virtual de Sapatos ®️ 🅿️".center(60))
        print('''
        1️⃣  Fazer Login
        2️⃣  Cadastrar Novo Usuário
        3️⃣  Sair
        ''')

        escolha = input("📍 Selecione uma opção: ")
        limpar_tela()

        if escolha == "1":
            from login import Login
            Login()
            break

        elif escolha == "2":
            Cadastrar()

        elif escolha == "3":
            print("\n👋 Encerrando o sistema. Até breve!")
            break

        else:
            print("\n\033[31m❌ Opção inválida. Tente novamente.\033[0m")

        input("\nPressione ENTER para voltar ao menu...")

        limpar_tela()

if __name__ == "__main__":
    inicio()