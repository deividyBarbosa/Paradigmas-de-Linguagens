from typing import Dict, Generic, List, Optional, TypeVar

from lf1.plp.expressions2.memory.IdentificadorNaoDeclaradoException import IdentificadorNaoDeclaradoException
from lf1.plp.expressions2.memory.VariavelJaDeclaradaException import VariavelJaDeclaradaException
from lf1.plp.expressions2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException

T = TypeVar("T")


class Contexto(Generic[T]):
    """Representa um contexto: uma pilha de blocos (escopos), cada um mapeando Id -> T."""

    def __init__(self, pilha: Optional[List[Dict]] = None):
        self._pilha: List[Dict] = pilha if pilha is not None else []

    def incrementa(self) -> None:
        self._pilha.append({})

    def restaura(self) -> None:
        self._pilha.pop()

    def map(self, id_arg, valor_id: T) -> None:
        """Mapeia o id no valor dado, no bloco mais interno."""
        topo = self._pilha[-1]
        if id_arg in topo:
            raise VariavelJaDeclaradaException(id_arg)
        topo[id_arg] = valor_id

    def get(self, id_arg) -> T:
        """Retorna o valor mapeado ao id dado, buscando do bloco mais interno ao mais externo."""
        try:
            for bloco in reversed(self._pilha):
                if id_arg in bloco:
                    return bloco[id_arg]
            raise IdentificadorNaoDeclaradoException()
        except IdentificadorNaoDeclaradoException:
            raise VariavelNaoDeclaradaException(id_arg)

    def getPilha(self) -> List[Dict]:
        return self._pilha

    def setPilha(self, pilha: List[Dict]) -> None:
        self._pilha = pilha

    def clone(self) -> "Contexto[T]":
        """Clone raso: nova pilha (lista), mas os blocos (dicts) continuam compartilhados."""
        return Contexto(list(self._pilha))
