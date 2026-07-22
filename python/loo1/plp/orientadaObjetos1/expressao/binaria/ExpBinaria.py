from abc import abstractmethod

from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao


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

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        return self.getEsq().checaTipo(ambiente) and self.getDir().checaTipo(ambiente)
