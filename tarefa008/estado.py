from pais import Pais


class Estado():
    """
    class para atribuir sigla e nome a um estado que esta ligado a um país
    Paulo Roberto
    16-07-2022
    """

    def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome
        self.pais = Pais
