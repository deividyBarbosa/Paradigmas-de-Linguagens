from abc import ABC, abstractmethod

from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id


class DecProcedimento(ABC):
    """Interface que representa uma declaracao de procedimento (metodo)."""

    @abstractmethod
    def getProcedimento(self, nome_procedimento: Id) -> "Procedimento":
        raise NotImplementedError

    @abstractmethod
    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        raise NotImplementedError
