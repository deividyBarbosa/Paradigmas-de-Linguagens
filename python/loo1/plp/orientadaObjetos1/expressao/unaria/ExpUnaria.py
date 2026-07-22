from abc import abstractmethod

from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao


class ExpUnaria(Expressao):
    """Uma expressao unaria contem uma expressao e um operador sobre a mesma."""

    def __init__(self, exp: Expressao, operador: str):
        self._exp = exp
        self._operador = operador

    def getExp(self) -> Expressao:
        return self._exp

    def getOperador(self) -> str:
        return self._operador

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        return self.getExp().checaTipo(ambiente)
