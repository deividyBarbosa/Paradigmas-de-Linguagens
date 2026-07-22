from abc import abstractmethod

from lf1.plp.expressions2.expression.Expressao import Expressao


class ExpUnaria(Expressao):
    """Uma expressao unaria contem uma expressao e um operador sobre a mesma."""

    def __init__(self, exp: Expressao, operador: str):
        self._exp = exp
        self._operador = operador

    def getExp(self) -> Expressao:
        return self._exp

    def getOperador(self) -> str:
        return self._operador

    def checaTipo(self, amb: "AmbienteCompilacao") -> bool:
        return self.getExp().checaTipo(amb) and self._checaTipoElementoTerminal(amb)

    @abstractmethod
    def _checaTipoElementoTerminal(self, amb: "AmbienteCompilacao") -> bool:
        """Metodo 'template' implementado nas subclasses para checar o tipo do elemento terminal."""
        raise NotImplementedError
