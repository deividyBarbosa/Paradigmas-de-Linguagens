from abc import abstractmethod
from typing import Generic, TypeVar

from li1.plp.expressions2.expression.Valor import Valor

T = TypeVar("T")


class ValorConcreto(Valor, Generic[T]):
    """Agrupa os diferentes tipos de valor concreto (inteiro, booleano, string)."""

    def __init__(self, valor: T):
        self._valor = valor

    def valor(self) -> T:
        """Retorna o valor encapsulado pelo objeto desta classe."""
        return self._valor

    def isEquals(self, obj: "ValorConcreto[T]") -> bool:
        """Determina igualdade entre objetos desta classe."""
        return self.valor() == obj.valor()

    def avaliar(self, amb: "AmbienteExecucao") -> "ValorConcreto[T]":
        """Retorna o valor deste valor primitivo, i.e., ele mesmo."""
        return self

    def checaTipo(self, amb: "AmbienteCompilacao") -> bool:
        """Um valor concreto e sempre bem tipado."""
        return True

    def reduzir(self, ambiente: "AmbienteExecucao") -> "ValorConcreto[T]":
        return self

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if other is None or type(other) is not type(self):
            return False
        return self._valor == other._valor

    def __hash__(self) -> int:
        return hash(self._valor)

    def __str__(self):
        return str(self._valor)

    @abstractmethod
    def clone(self) -> "ValorConcreto[T]":
        raise NotImplementedError
