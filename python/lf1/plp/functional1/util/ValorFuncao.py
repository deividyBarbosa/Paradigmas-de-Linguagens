from typing import Dict, List

from lf1.plp.expressions1.util.Tipo import Tipo
from lf1.plp.expressions2.expression.Expressao import Expressao
from lf1.plp.expressions2.expression.Id import Id


class ValorFuncao:
    """Representa o valor de uma funcao: seus parametros formais e o corpo (expressao)."""

    def __init__(self, args_id: List[Id], exp: Expressao):
        self._args_id = args_id
        self._exp = exp

    def getListaId(self) -> List[Id]:
        return self._args_id

    def getExp(self) -> Expressao:
        return self._exp

    def getAridade(self) -> int:
        """Retorna a aridade desta funcao."""
        return len(self._args_id)

    def checaTipo(self, ambiente: "AmbienteCompilacao") -> bool:
        ambiente.incrementa()
        t = self.getTipo(ambiente)
        for id_ in self._args_id:
            ambiente.map(id_, Tipo(t.get()))
            t = t.getProx()
        ambiente.restaura()
        return True

    def getTipo(self, ambiente: "AmbienteCompilacao") -> Tipo:
        from lf1.plp.functional1.util.RestrictTypesVisitor import RestrictTypesVisitor

        map_id_tipo: Dict[Id, Tipo] = {id_: Tipo() for id_ in self._args_id}
        ids_arg: List[Id] = list(self._args_id)

        RestrictTypesVisitor.visit(self._exp, ambiente, map_id_tipo, Tipo())

        ambiente.incrementa()
        for id_, tipo in map_id_tipo.items():
            ambiente.map(id_, tipo)

        result = self._exp.getTipo(ambiente)
        for id_ in reversed(ids_arg):
            result = Tipo(map_id_tipo[id_].get(), result)
        ambiente.restaura()
        return result
