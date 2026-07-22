from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from le2.plp.expressions2.expression.Id import Id

T = TypeVar("T")


class Ambiente(ABC, Generic[T]):
    """Interface generica de ambiente: mapeia identificadores (Id) a valores do tipo T."""

    @abstractmethod
    def incrementa(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def restaura(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def map(self, id_arg: Id, tipo_id: T) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, id_arg: Id) -> T:
        raise NotImplementedError
