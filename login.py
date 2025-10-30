import json
from main import menu
 
class Login():
    """ Gerencia o processo de login do usuário. Solicita nome e senha, verifica as credenciais no arquivo 'usuarios.json'
    e, em caso de sucesso, inicia o menu principal. """

    def __init__(self):
        """ Inicializa o login, solicitando nome e senha e realizando a autenticação.
        Se as credenciais estiverem corretas, chama a função 'menu'. """

        self.nome = input("Informe seu nome: ").capitalize()
        self.senha = input("Informe sua senha: ")

        with open('usuarios.json', 'r') as arquivo:
            dados = json.load(arquivo)

            for u in dados:
                if u["Nome"] == self.nome and u["Senha"] == self.senha:
                    print(f"Bem-vindo(a), {self.nome}!")
                    menu(self.nome)
                    return
                
            print("Usuário ou senha incorretas!")