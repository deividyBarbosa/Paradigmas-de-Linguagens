from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from loo1.plp.expressions2.expression.Id import Id
from loo1.plp.expressions2.memory.Ambiente import Ambiente

T = TypeVar("T")


class AmbienteOO1(Ambiente[T], ABC, Generic[T]):
    """Interface que representa um ambiente (de compilacao ou execucao) na linguagem OO."""

    @abstractmethod
    def mapDefClasse(self, id_arg: Id, def_classe: "DefClasse") -> None:
        raise NotImplementedError

    @abstractmethod
    def getDefClasse(self, id_arg: Id) -> "DefClasse":
        raise NotImplementedError
