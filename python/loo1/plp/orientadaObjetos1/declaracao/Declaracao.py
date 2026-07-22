from abc import ABC, abstractmethod


class Declaracao(ABC):
    """Interface que representa uma declaracao."""

    @abstractmethod
    def elabora(self, ambiente: "AmbienteExecucaoOO1") -> "AmbienteExecucaoOO1":
        raise NotImplementedError

    @abstractmethod
    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        raise NotImplementedError
