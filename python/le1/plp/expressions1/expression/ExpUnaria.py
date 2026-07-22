from abc import abstractmethod

from le1.plp.expressions1.expression.Expressao import Expressao


class ExpUnaria(Expressao):
    """Uma expressao unaria contem uma expressao e um operador sobre a mesma."""

    def __init__(self, exp: Expressao, operador: str):
        self._exp = exp
        self._operador = operador

    def getExp(self) -> Expressao:
        return self._exp

    def getOperador(self) -> str:
        return self._operador

    def __str__(self):
        return f"{self._operador} {self._exp}"

    def checaTipo(self) -> bool:
        return self.getExp().checaTipo() and self._checaTipoElementoTerminal()

    @abstractmethod
    def _checaTipoElementoTerminal(self) -> bool:
        """Metodo 'template' implementado nas subclasses para checar o tipo do elemento terminal."""
        raise NotImplementedError
