from datetime import date


class PessoaFisica():
    """class atribui nome, sexo e data nascimento à uma pessoa
    """

    def __init__(self, nome, sexo):
        self.nome = nome
        self.sexo = sexo
        self.dataNascimento = date
