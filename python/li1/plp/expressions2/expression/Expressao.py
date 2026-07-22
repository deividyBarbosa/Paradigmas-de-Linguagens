from abc import ABC, abstractmethod


class Expressao(ABC):
    """Uma expressao e a unidade basica na Linguagem de Expressoes."""

    @abstractmethod
    def avaliar(self, amb: "AmbienteExecucao") -> "Valor":
        """Avalia a expressao retornando seu Valor."""
        raise NotImplementedError

    @abstractmethod
    def checaTipo(self, amb: "AmbienteCompilacao") -> bool:
        """Realiza a verificacao de tipos desta expressao."""
        raise NotImplementedError

    @abstractmethod
    def getTipo(self, amb: "AmbienteCompilacao"):
        """Retorna os tipos possiveis desta expressao."""
        raise NotImplementedError

    @abstractmethod
    def reduzir(self, ambiente: "AmbienteExecucao") -> "Expressao":
        """Retorna uma expressao reduzida, sem ocorrencia de identificadores conhecidos."""
        raise NotImplementedError

    @abstractmethod
    def clone(self) -> "Expressao":
        raise NotImplementedError
