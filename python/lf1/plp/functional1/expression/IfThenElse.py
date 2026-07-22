from lf1.plp.expressions1.util.Tipo import Tipo
from lf1.plp.expressions2.expression.Expressao import Expressao
from lf1.plp.expressions2.expression.Valor import Valor


class IfThenElse(Expressao):
    """Expressao condicional: avalia 'then' ou 'else' de acordo com 'condicao'."""

    def __init__(self, teste: Expressao, then_expressao: Expressao, else_expressao: Expressao):
        self._condicao = teste
        self._then = then_expressao
        self._else_expressao = else_expressao

    def avaliar(self, ambiente: "AmbienteExecucao") -> Valor:
        if self._condicao.avaliar(ambiente).valor():
            return self._then.avaliar(ambiente)
        return self._else_expressao.avaliar(ambiente)

    def __str__(self):
        return f"if ({self._condicao}) then ({self._then}) else ({self._else_expressao})"

    def checaTipo(self, amb: "AmbienteCompilacao") -> bool:
        if not self._condicao.getTipo(amb).eBooleano():
            return False
        if self._then.getTipo(amb).intersecao(self._else_expressao.getTipo(amb)).eVoid():
            return False
        return True

    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        return self._then.getTipo(amb).intersecao(self._else_expressao.getTipo(amb))

    def getCondicao(self) -> Expressao:
        return self._condicao

    def getThen(self) -> Expressao:
        return self._then

    def getElseExpressao(self) -> Expressao:
        return self._else_expressao
