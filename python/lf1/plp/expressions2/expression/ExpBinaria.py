from abc import abstractmethod

from lf1.plp.expressions2.expression.Expressao import Expressao


class ExpBinaria(Expressao):
    """Uma expressao binaria contem duas expressoes e um operador, em ordem definida."""

    def __init__(self, esq: Expressao, dir: Expressao, operador: str):
        self._esq = esq
        self._dir = dir
        self._operador = operador

    def getEsq(self) -> Expressao:
        return self._esq

    def getDir(self) -> Expressao:
        return self._dir

    def getOperador(self) -> str:
        return self._operador

    def __str__(self):
        return f"{self._esq} {self._operador} {self._dir}"

    def checaTipo(self, amb: "AmbienteCompilacao") -> bool:
        if not self.getEsq().checaTipo(amb) or not self.getDir().checaTipo(amb):
            return False
        return self._checaTipoElementoTerminal(amb)

    @abstractmethod
    def _checaTipoElementoTerminal(self, amb: "AmbienteCompilacao") -> bool:
        """Metodo 'template' implementado nas subclasses para checar o tipo do elemento terminal."""
        raise NotImplementedError
