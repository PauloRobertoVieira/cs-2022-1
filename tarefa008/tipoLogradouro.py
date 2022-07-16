from enum import Enum


class TipoLogradouro(Enum):
    """class atribui o tipo ao logradouro usado na classe tipoEndereco

    Args:
        Enum (_type_)
    """
    Alameda = 0
    Avenida = 1
    Marginal = 2
    Rua = 3
    Rodovia = 4
    Via = 5
    Viela = 6
    Travessa = 7
