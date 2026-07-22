from typing import List

from li2.plp.expressions1.util.Tipo import Tipo
from li2.plp.expressions1.util.ToStringProvider import ToStringProvider


class TipoProcedimento(Tipo):
    """Tipo de um procedimento: a lista (ordenada) dos tipos dos seus parametros formais."""

    def __init__(self, tipos_parametros_formais: List[Tipo]):
        self._tipos_parametros_formais: List[Tipo] = list(tipos_parametros_formais)

    def eBooleano(self) -> bool:
        return False

    def eInteiro(self) -> bool:
        return False

    def eString(self) -> bool:
        return False

    def eIgual(self, tipo: Tipo) -> bool:
        if isinstance(tipo, TipoProcedimento):
            return tipo._tipos_parametros_formais == self._tipos_parametros_formais
        return tipo.eIgual(self)

    def eValido(self) -> bool:
        return all(tipo.eValido() for tipo in self._tipos_parametros_formais)

    def getNome(self) -> str:
        return ToStringProvider.listToString(self._tipos_parametros_formais, "{", "}", ",")

    def intersecao(self, outro_tipo: Tipo):
        if outro_tipo.eIgual(self):
            return self
        return None

    def __str__(self):
        return self.getNome()
