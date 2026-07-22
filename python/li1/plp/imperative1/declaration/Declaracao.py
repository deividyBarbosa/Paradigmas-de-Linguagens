from abc import ABC, abstractmethod


class Declaracao(ABC):

    @abstractmethod
    def elabora(self, ambiente: "AmbienteExecucaoImperativa") -> "AmbienteExecucaoImperativa":
        raise NotImplementedError

    @abstractmethod
    def checaTipo(self, ambiente: "AmbienteCompilacaoImperativa") -> bool:
        raise NotImplementedError
