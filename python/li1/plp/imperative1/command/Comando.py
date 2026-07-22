from abc import ABC, abstractmethod


class Comando(ABC):
    """
    A execucao de um comando ocorre em um determinado ambiente. O resultado
    de tal execucao e a modificacao deste ambiente, i.e., comandos tem
    efeito colateral.
    """

    @abstractmethod
    def executar(self, ambiente: "AmbienteExecucaoImperativa") -> "AmbienteExecucaoImperativa":
        raise NotImplementedError

    @abstractmethod
    def checaTipo(self, ambiente: "AmbienteCompilacaoImperativa") -> bool:
        raise NotImplementedError
