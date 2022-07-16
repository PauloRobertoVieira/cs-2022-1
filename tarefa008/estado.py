from pais import Pais


class Estado():
    """class para atribuir sigla e nome a um estado que esta ligado a um país
    """

    def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome
        self.pais = Pais
