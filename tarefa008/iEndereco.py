from abc import ABC, abstractmethod


class IEndereco(ABC):
    """class abstrata atribuir cep

    Args:
        ABC biblioteca abstract class
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
