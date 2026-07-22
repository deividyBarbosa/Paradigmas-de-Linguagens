from le1.plp.expressions1.expression.Expressao import Expressao
from le1.plp.expressions1.expression.Valor import Valor


class Programa:
    """Um programa em le1 e uma unica expressao a ser avaliada."""

    def __init__(self, exp: Expressao):
        self._exp = exp

    def executar(self) -> Valor:
        result = self._exp.avaliar()
        print(result)
        return result

    def checaTipo(self) -> bool:
        return self._exp.checaTipo()

    def getExpressao(self) -> Expressao:
        return self._exp
