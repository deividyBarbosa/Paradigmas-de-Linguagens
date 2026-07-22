from abc import ABC, abstractmethod


class Expressao(ABC):
    """Uma expressao e a unidade basica na Linguagem de Expressoes."""

    @abstractmethod
    def avaliar(self) -> "Valor":
        """Avalia a expressao retornando seu Valor."""
        raise NotImplementedError

    @abstractmethod
    def checaTipo(self) -> bool:
        """Realiza a verificacao de tipos desta expressao."""
        raise NotImplementedError

    @abstractmethod
    def getTipo(self):
        """Retorna os tipos possiveis desta expressao."""
        raise NotImplementedError
