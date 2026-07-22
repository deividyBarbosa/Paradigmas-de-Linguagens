from abc import ABC, abstractmethod

from li1.plp.expressions2.expression.Id import Id
from li1.plp.expressions2.expression.Valor import Valor
from li1.plp.expressions2.memory.AmbienteExecucao import AmbienteExecucao


class AmbienteExecucaoImperativa(AmbienteExecucao, ABC):

    @abstractmethod
    def changeValor(self, id_arg: Id, valor_id: Valor) -> None:
        raise NotImplementedError

    @abstractmethod
    def read(self) -> Valor:
        raise NotImplementedError

    @abstractmethod
    def write(self, v: Valor) -> None:
        raise NotImplementedError

    @abstractmethod
    def getSaida(self) -> "ListaValor":
        raise NotImplementedError
