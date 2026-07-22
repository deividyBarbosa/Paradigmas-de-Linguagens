from abc import abstractmethod

from loo1.plp.expressions2.expression.Expressao import Expressao


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

    def __str__(self):
        return f"{self._operador} {self._exp}"

    @abstractmethod
    def _checaTipoElementoTerminal(self, amb: "AmbienteCompilacao") -> bool:
        """Metodo 'template' implementado nas subclasses para checar o tipo do elemento terminal."""
        raise NotImplementedError

    def reduzir(self, ambiente: "AmbienteExecucao") -> "ExpUnaria":
        self._exp = self._exp.reduzir(ambiente)
        return self

    @abstractmethod
    def clone(self) -> "ExpUnaria":
        raise NotImplementedError
