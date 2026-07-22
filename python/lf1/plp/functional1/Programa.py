from lf1.plp.expressions2.expression.Expressao import Expressao
from lf1.plp.expressions2.expression.Valor import Valor
from lf1.plp.expressions2.memory.ContextoCompilacao import ContextoCompilacao
from lf1.plp.functional1.memory.ContextoExecucaoFuncional import ContextoExecucaoFuncional


class Programa:
    """Um programa em lf1: uma expressao (possivelmente com funcoes) a avaliar."""

    def __init__(self, exp: Expressao):
        self._exp = exp

    def executar(self) -> Valor:
        amb_exec = ContextoExecucaoFuncional()
        return self._exp.avaliar(amb_exec)

    def checaTipo(self) -> bool:
        amb_comp = ContextoCompilacao()
        return self._exp.checaTipo(amb_comp)

    def getExpressao(self) -> Expressao:
        return self._exp
