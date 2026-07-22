from abc import ABC, abstractmethod


class Expressao(ABC):
    """Uma expressao e a unidade basica na Linguagem Orientada a Objetos."""

    @abstractmethod
    def avaliar(self, ambiente: "AmbienteExecucaoOO1") -> "Valor":
        """Avalia a expressao retornando seu Valor."""
        raise NotImplementedError

    @abstractmethod
    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        """Realiza a verificacao de tipos desta expressao."""
        raise NotImplementedError

    @abstractmethod
    def getTipo(self, ambiente: "AmbienteCompilacaoOO1"):
        """Retorna os tipos possiveis desta expressao."""
        raise NotImplementedError
