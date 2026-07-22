from abc import abstractmethod

from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
from loo1.plp.orientadaObjetos1.expressao.leftExpression.LeftExpression import LeftExpression


class AcessoAtributo(LeftExpression):
    """Representa um acesso de atributo (obj.attr ou this.attr)."""

    def __init__(self, id_: Id):
        self._id = id_

    def getId(self) -> Id:
        return self._id

    @abstractmethod
    def getExpressaoObjeto(self) -> Expressao:
        raise NotImplementedError
