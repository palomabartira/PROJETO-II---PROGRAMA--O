import json

class Cadastrar():
    __arquivo = "usuarios.json"

    def __init__(self):
        self.usuario = {}
        self.coletar_dados()

        if self.usuario:  # Só salva se o usuário for válido
            self.salvar(self.usuario)

    def coletar_dados(self):
        while True:
            self.nome = input("Informe seu nome: ").capitalize()
            if len(self.nome) == 0 or len(self.nome) > 10:
                print(f"O nome não pode ser vazio e não poder ter mais que 10 caracteres!")
                continue
       
            self.email = input("Informe seu email: ")
            if "@" not in self.email:
                print("E-mail inválido!")
                continue

            self.senha = input("Informe sua senha: ")
            if len(self.senha) < 5:
                print("A senha deve ter no mínimo 5 caracteres!")
                continue
            
            self.usuario = {
                "Nome": self.nome,
                "E-mail": self.email,
                "Senha": self.senha
            }

            break

    @classmethod
    def carregar(cls):
        try:
            with open(cls.__arquivo, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            return []  # Se o arquivo ainda não existir
        except json.JSONDecodeError:
            return []  # Se o arquivo estiver vazio ou corrompido

    @classmethod
    def salvar(cls, novo_usuario):
        # Carrega a lista atual de usuários
        dados = cls.carregar()

        # Adiciona o novo usuário
        dados.append(novo_usuario)

        # Sobrescreve o arquivo com a lista atualizada
        with open(cls.__arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        
        print("Usuário cadastrado com sucesso!") 