"""
Exercicio gerando documentação python
No Windows (powershell) use:
    python -m pydocs sys
Para gerar arquivo .html:
    python -m pydoc -w nomeDoArquivoSemExtensão


################################################

Para versões Linux use:
    pydoc sys
Para gerar arquivo .html:
    pydoc -w nomeDoArquivoSemExtensão
"""

from abc import ABC, abstractmethod
from datetime import date
from enum import Enum


class Bairro():
    """
    class atribuir nome bairro
    Paulo Roberto
    16-07-2022
    """

    def __init__(self, nome):
        self.nome = nome


class Cidade():
    """
    class atribuir nome a cidade
    Paulo Roberto
    16-07-2022
    """

    def __init__(self, nome):
        self.nome = nome


class Edereco():
    """
    class atribuir dados a endereço
    Paulo Roberto
    16-07-2022
    """

    def __init__(self, numero, complemento, cep):
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
    """
    Método construtor classe endereço
    """


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


class IEndereco(ABC):
    """
    class abstrata atribuir cep
    Paulo Roberto
    16-07-2022

    Args:
        ABC biblioteca abstract class
        Paulo Roberto
        16-07-2022
    """

    @abstractmethod
    def ConsultarPorCep(self, cep):
        pass


class IEderecocompl(IEndereco):
    """class consulta endereço por cep

    Args:
        IEndereco super class
    """

    def ConsultarPorCep(self, cep):
        return None


class Logradouro():
    """
    class atribuir nome a logradouro
    Paulo Roberto
    16-07-2022
    """

    def __init__(self, nome):
        self.nome = nome


class Pais():
    """
    class atribui nome a país
    Paulo Roberto
    16-07-2022
    """

    def __init__(self, nome):
        self.nome = nome


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


class TipoEndereco(Enum):
    """
    class tipo Enum, boolean para tipo de endereço
    Paulo Roberto
    16-07-2022

    Args:
        Enum (_type_)
        Paulo Roberto
        16-07-2022
    """
    Comercial = 0
    Residencial = 1


class TipoLogradouro(Enum):
    """
    class atribui o tipo ao logradouro usado na classe tipoEndereco
    Paulo Roberto
    16-07-2022

    Args:
        Enum (_type_)
        Paulo Roberto
        16-07-2022
    """
    Alameda = 0
    Avenida = 1
    Marginal = 2
    Rua = 3
    Rodovia = 4
    Via = 5
    Viela = 6
    Travessa = 7
