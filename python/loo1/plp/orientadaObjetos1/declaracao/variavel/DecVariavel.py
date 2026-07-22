from abc import abstractmethod

from loo1.plp.orientadaObjetos1.declaracao.Declaracao import Declaracao
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
from loo1.plp.orientadaObjetos1.util.Tipo import Tipo


class DecVariavel(Declaracao):
    """Interface representando uma declaracao de variavel (atributo)."""

    @abstractmethod
    def getTipo(self, id_: Id) -> Tipo:
        """Retorna o tipo do identificador declarado."""
        raise NotImplementedError
