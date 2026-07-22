from abc import ABC

from lf1.plp.expressions1.util.Tipo import Tipo
from lf1.plp.expressions2.memory.Ambiente import Ambiente


class AmbienteCompilacao(Ambiente[Tipo], ABC):
    """Ambiente usado na checagem de tipos: mapeia Id -> Tipo."""
