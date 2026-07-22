from typing import Dict, Generic, List, TypeVar

from loo1.plp.expressions2.memory.IdentificadorJaDeclaradoException import IdentificadorJaDeclaradoException
from loo1.plp.expressions2.memory.IdentificadorNaoDeclaradoException import IdentificadorNaoDeclaradoException
from loo1.plp.expressions2.memory.VariavelJaDeclaradaException import VariavelJaDeclaradaException
from loo1.plp.expressions2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException

T = TypeVar("T")


class Contexto(Generic[T]):
    """Representa um contexto: uma pilha de blocos (escopos), cada um mapeando Id -> T."""

    def __init__(self):
        self._pilha: List[Dict] = []

    def incrementa(self) -> None:
        self._pilha.append({})

    def restaura(self) -> None:
        self._pilha.pop()

    def map(self, id_arg, valor_id: T) -> None:
        """Mapeia o id no valor dado, no bloco mais interno."""
        topo = self._pilha[-1]
        try:
            if id_arg in topo:
                raise IdentificadorJaDeclaradoException()
            topo[id_arg] = valor_id
        except IdentificadorJaDeclaradoException:
            raise VariavelJaDeclaradaException(id_arg)

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
