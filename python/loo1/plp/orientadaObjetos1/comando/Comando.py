from abc import ABC, abstractmethod

# A execucao de um comando ocorre em um determinado ambiente. O resultado de
# tal execucao e a modificacao deste ambiente, i.e., comandos tem efeito
# colateral.


class Comando(ABC):
    """Interface representando um comando na linguagem OO."""

    @abstractmethod
    def executar(self, ambiente: "AmbienteExecucaoOO1") -> "AmbienteExecucaoOO1":
        raise NotImplementedError

    @abstractmethod
    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        raise NotImplementedError
