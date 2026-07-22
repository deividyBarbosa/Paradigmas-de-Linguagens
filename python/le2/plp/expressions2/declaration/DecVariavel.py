from le2.plp.expressions2.expression.Expressao import Expressao
from le2.plp.expressions2.expression.Id import Id


class DecVariavel:
    """Associa um identificador a expressao que define seu valor/tipo."""

    def __init__(self, id_arg: Id, expressao_arg: Expressao):
        self._id = id_arg
        self._expressao = expressao_arg

    def getID(self) -> Id:
        return self._id

    def getExpressao(self) -> Expressao:
        return self._expressao
