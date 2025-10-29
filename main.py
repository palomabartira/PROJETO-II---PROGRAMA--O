from ver_produtos import Sapatos
from inserir_produtos import Carrinho
from apagar_produtos import Remover

def menu():
    """Criação do menu para possibilitar que o usuário consiga interagir com o sistema.
    Para isso, é solicitado que o usuário escolha uma opção válida, e, em seguida,
    direciona a execução do programa para a função correspondente, baseado na escolha feita"""
    while True:
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
        
        opcao = input("⏮ Selecione uma opção no menu para continuar: ⏭ ")

        if opcao == "1":
            print("-" * 70)
            print("⏮ Carregando o Catálogo... ⏭\n")
            Sapatos.verProdutos()

        elif opcao == "2":
            print("-" * 70)
            print("⏮ Carregando o Carrinho... ⏭\n")
            Carrinho.inserirProdutos()
          
        elif opcao == "3":
            print("-" * 70)
            print("⏮ Mostrando itens do seu carrinho... ⏭\n")
            
        
        elif opcao == "4":
            print("-" * 70)
            print("⏮ Removendo produtos do carrinho ⏭\n")
            Remover.excluirSapatos()

        elif opcao == "5":
            print("-" * 70)
            print("⏮ Saindo... Esperamos vê-lo em breve! ⏭\n")
            break
          
        else:
            print("\033[31m❌ Opção Inválida\033[0m")


if __name__ == "__main__":
    menu()