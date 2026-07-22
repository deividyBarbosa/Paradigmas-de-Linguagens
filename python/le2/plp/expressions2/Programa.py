from le2.plp.expressions2.expression.Expressao import Expressao
from le2.plp.expressions2.expression.Valor import Valor
from le2.plp.expressions2.memory.ContextoCompilacao import ContextoCompilacao
from le2.plp.expressions2.memory.ContextoExecucao import ContextoExecucao


class Programa:
    """Um programa em le2: uma expressao a ser checada e avaliada num ambiente proprio."""

    def __init__(self, exp: Expressao):
        self._exp = exp

    def executar(self) -> Valor:
        amb_exec = ContextoExecucao()
        return self._exp.avaliar(amb_exec)

    def checaTipo(self) -> bool:
        amb_comp = ContextoCompilacao()
        return self._exp.checaTipo(amb_comp)

    def getExpressao(self) -> Expressao:
        return self._exp
