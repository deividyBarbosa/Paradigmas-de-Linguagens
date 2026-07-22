from abc import ABC, abstractmethod


class ExpressaoComplexa(ABC):
    """Unidade basica que depende de um ambiente (de compilacao ou de execucao)."""

    @abstractmethod
    def avaliar(self, amb: "AmbienteExecucao") -> "Valor":
        """Avalia a expressao no ambiente dado, retornando seu Valor."""
        raise NotImplementedError

    @abstractmethod
    def checaTipo(self, amb: "AmbienteCompilacao") -> bool:
        """Realiza a verificacao de tipos desta expressao no ambiente dado."""
        raise NotImplementedError

    @abstractmethod
    def getTipo(self, amb: "AmbienteCompilacao"):
        """Retorna os tipos possiveis desta expressao no ambiente dado."""
        raise NotImplementedError
