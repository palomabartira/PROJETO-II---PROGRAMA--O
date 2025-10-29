import json
 
class Login():
    """Essa classe tem como objetivo gerenciar o acesso de um usuário."""
    def __init__(self):
        self.nome = input("Informe seu nome: ").capitalize()
        self.senha = input("Informe sua senha: ")

        with open('usuarios.json', 'r') as arquivo:
            dados = json.load(arquivo)

            for u in dados:
                if u["Nome"] == self.nome and u["Senha"] == self.senha:
                    print(f"Bem-vindo(a), {self.nome}!")
                    # self.menu()
                    return
                
            print("Usuário ou senha incorretas!")