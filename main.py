from ver_produtos import Sapatos
from inserir_produtos import Carrinho

def menu():
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
            print("⏮ Carregando catálogos... ⏭\n")
            Sapatos.verProdutos()

        elif opcao == "2":
            print("-" * 70)
            print("⏮ Carregando o carrinho... ⏭\n")
            Carrinho.inserirProduto()
          
        elif opcao == "3":
            print("-" * 70)
            print("⏮ Mostrando itens do seu carrinho... ⏭\n")
        
        elif opcao == "4":
            print("-" * 70)
            print("⏮ Removendo produtos do carrinho ⏭\n")

        elif opcao == "5":
            print("-" * 70)
            print("⏮ Saindo... Esperamos vê-lo em breve! ⏭\n")
            break
          
        else:
            print("❌ Opção Inválida")


if __name__ == "__main__":
    menu()