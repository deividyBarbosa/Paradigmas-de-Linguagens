from abc import ABC

from le2.plp.expressions1.util.Tipo import Tipo
from le2.plp.expressions2.memory.Ambiente import Ambiente


class AmbienteCompilacao(Ambiente[Tipo], ABC):
    """Ambiente usado na checagem de tipos: mapeia Id -> Tipo."""
