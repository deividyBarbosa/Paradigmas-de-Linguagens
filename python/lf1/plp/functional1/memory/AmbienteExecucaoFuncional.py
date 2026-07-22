from abc import ABC, abstractmethod

from lf1.plp.expressions2.expression.Id import Id
from lf1.plp.expressions2.memory.AmbienteExecucao import AmbienteExecucao


class AmbienteExecucaoFuncional(AmbienteExecucao, ABC):
    """Ambiente de execucao que tambem mapeia identificadores para funcoes (ValorFuncao)."""

    @abstractmethod
    def mapFuncao(self, id_arg: Id, funcao: "ValorFuncao") -> None:
        """Mapeia um identificador em uma funcao."""
        raise NotImplementedError

    @abstractmethod
    def getFuncao(self, id_arg: Id) -> "ValorFuncao":
        """Retorna a funcao mapeada pelo identificador."""
        raise NotImplementedError
