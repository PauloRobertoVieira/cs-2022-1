from abc import ABC, abstractmethod


class IEndereco(ABC):

    @abstractmethod
    def ConsultarPorCep(self, cep):
        pass


class IEderecocompl(IEndereco):

    def ConsultarPorCep(self, cep):
        return None
