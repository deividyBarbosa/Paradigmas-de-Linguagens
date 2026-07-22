from abc import ABC, abstractmethod

from le2.plp.expressions2.expression.Valor import Valor
from le2.plp.expressions2.memory.Ambiente import Ambiente


class AmbienteExecucao(Ambiente[Valor], ABC):
    """Ambiente usado na execucao: mapeia Id -> Valor."""

    @abstractmethod
    def clone(self) -> "AmbienteExecucao":
        raise NotImplementedError
