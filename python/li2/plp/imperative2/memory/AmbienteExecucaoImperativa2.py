from abc import ABC, abstractmethod

from li2.plp.expressions2.expression.Id import Id
from li2.plp.imperative1.memory.AmbienteExecucaoImperativa import AmbienteExecucaoImperativa


class AmbienteExecucaoImperativa2(AmbienteExecucaoImperativa, ABC):

    @abstractmethod
    def mapProcedimento(self, id_arg: Id, procedimento_id: "DefProcedimento") -> None:
        raise NotImplementedError

    @abstractmethod
    def getProcedimento(self, id_arg: Id) -> "DefProcedimento":
        raise NotImplementedError
