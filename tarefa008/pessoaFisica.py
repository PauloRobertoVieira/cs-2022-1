from datetime import date


class PessoaFisica():
    """
    class atribui nome, sexo e data nascimento à uma pessoa
    Paulo Roberto
    16-07-2022
    """

    def __init__(self, nome, sexo):
        self.nome = nome
        self.sexo = sexo
        self.dataNascimento = date
