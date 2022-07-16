from abc import ABC, abstractmethod


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
