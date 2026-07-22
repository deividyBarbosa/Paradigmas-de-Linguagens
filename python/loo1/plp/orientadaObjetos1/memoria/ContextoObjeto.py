from typing import Dict

from loo1.plp.expressions2.expression.Id import Id
from loo1.plp.orientadaObjetos1.expressao.valor.Valor import Valor


class ContextoObjeto:
    """O estado (atributos) de um objeto: um mapeamento Id -> Valor."""

    def __init__(self, hash_: Dict[Id, Valor]):
        self._estado: Dict[Id, Valor] = dict(hash_)

    def remove(self, id_: Id) -> None:
        self._estado.pop(id_, None)

    def put(self, id_: Id, valor: Valor) -> None:
        self._estado[id_] = valor

    def containsKey(self, id_variavel: Id) -> bool:
        return id_variavel in self._estado

    def get(self, id_: Id) -> Valor:
        return self._estado.get(id_)
