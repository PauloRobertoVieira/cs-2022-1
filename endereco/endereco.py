from datetime import date
from enum import Enum


class PessoaFisica():
    def __init__(self, nome, sexo, endereco):
        self.nome = nome
        self.sexo = sexo
        self.dataNascimento = date
        self.endereco = endereco


class Edereco():
    def __init__(self, numero, complemento, cep, bairro, tipoendereco, logradouro):
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.bairro = bairro
        self.tipoendereco = tipoendereco
        self.logradouro = logradouro


class Bairro():
    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade


class Cidade():
    def __init__(self, nome, estado):
        self.nome = nome
        self.estado = estado


class Estado():
    def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome
        self.pais = Pais


class Pais():
    def __init__(self, nome):
        self.nome = nome


class Logradouro():
    def __init__(self, nome, tipologradouro):
        self.nome = nome
        self.tipologradouro = tipologradouro


class TipoEndereco(Enum):
    Comercial = 0
    Residencial = 1


class TipoLogradouro(Enum):
    Alameda = 0
    Avenida = 1
    Marginal = 2
    Rua = 3
    Rodovia = 4
    Via = 5
    Viela = 6
    Travessa = 7
