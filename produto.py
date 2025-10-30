class Produto:
    """ Classe base para todos os produtos. """

    def __init__(self, id, nome, preco):
        """ Inicializa um novo produto. """

        self.id = id
        self.nome = nome
        self.preco = preco

    def mostrar(self):
        """ Retorna uma string formatada para exibição do produto. """

        return f"ID: {self.id} - {self.nome} - R$ {self.preco:.2f}"


class Sapato(Produto):
    """ Representa um Sapato, herdando de Produto.
    Adiciona o atributo 'tipo' (com valor padrão 'sapato'). """
    
    def __init__(self, id, nome, preco, tipo="sapato"):
        super().__init__(id, nome, preco)
        self.tipo = tipo