from abc import ABC, abstractmethod

from lf1.plp.expressions1.util.Tipo import Tipo
from lf1.plp.expressions2.expression.Expressao import Expressao
from lf1.plp.expressions2.expression.Id import Id


class DeclaracaoFuncional(ABC):
    """Uma declaracao (de variavel ou de funcao) dentro de um bloco 'let'."""

    @abstractmethod
    def getID(self) -> Id:
        raise NotImplementedError

    @abstractmethod
    def getAridade(self) -> int:
        """Retorna a aridade da funcao declarada. Variaveis tem aridade 0."""
        raise NotImplementedError

    @abstractmethod
    def getExpressao(self) -> Expressao:
        raise NotImplementedError

    @abstractmethod
    def checaTipo(self, ambiente: "AmbienteCompilacao") -> bool:
        raise NotImplementedError

    @abstractmethod
    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        raise NotImplementedError
