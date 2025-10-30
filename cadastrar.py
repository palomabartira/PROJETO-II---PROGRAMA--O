import json

class Cadastrar():
    """ Essa classe tem como objetivo realizar o cadastro de novos usuários. Para isso, o código
    faz verificações e salva os dados em um arquivo Json. """
    __arquivo = "usuarios.json"

    def __init__(self):
        self.usuario = {}
        self.coletar_dados()

        if self.usuario:  
            self.salvar(self.usuario)

    def coletar_dados(self):
        """ Solicita e valida os dados de cadastro do usuário (nome, e-mail e senha). Para isso, 
        realiza as seguintes verificações: Nome (não pode ser vazio e deve ter no máximo 10 caracteres),
        E-mail (deve conter o caractere '@') e Senha (deve ter no mínimo 5 caracteres). Após a coleta e 
        validação, armazena as informações em um dicionário no atributo 'self.usuario'. """
        while True:
            self.nome = input("👤 Informe seu nome: ").capitalize()
            if len(self.nome) == 0 or len(self.nome) > 10:
                print(f"\n\033[31m❌ O nome não pode ser vazio e não poder ter mais que 10 caracteres!\033[0m\n")
                continue
       
            self.email = input("📧 Informe seu email: ")
            if "@" not in self.email:
                print("\n\033[31m❌ E-mail inválido!\033[0m\n")
                continue

            self.senha = input("🔒 Informe sua senha: ")
            if len(self.senha) < 5:
                print("\n\033[31m❌ A senha deve ter no mínimo 5 caracteres!\033[0m\n")
                continue
            
            self.usuario = {
                "Nome": self.nome,
                "E-mail": self.email,
                "Senha": self.senha
            }

            break

    @classmethod
    def carregar(cls):
        """ Carrega a lista de usuários em Json. Se o arquivo estiver vazio ou corrompido, retorna 
        uma lista vazia. """
        try:
            with open(cls.__arquivo, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            return []  
        except json.JSONDecodeError:
            return []

    @classmethod
    def salvar(cls, novo_usuario):
        """ Salva um novo usuário na base de dados (arquivo JSON). O método carrega a lista 
        existente de usuários, adiciona o 'novo_usuario' e sobrescreve o arquivo com a lista atualizada. """
        
        dados = cls.carregar()
        
        dados.append(novo_usuario)

        with open(cls.__arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        
        print("\n\033[32m✔ Usuário cadastrado com sucesso!\033[0m") 