from abc import ABC

from lf1.plp.expressions2.expression.Valor import Valor
from lf1.plp.expressions2.memory.Ambiente import Ambiente


class AmbienteExecucao(Ambiente[Valor], ABC):
    """Ambiente usado na execucao: mapeia Id -> Valor."""
