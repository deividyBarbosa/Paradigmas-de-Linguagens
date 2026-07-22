from abc import ABC, abstractmethod

from li1.plp.expressions1.util.Tipo import Tipo
from li1.plp.expressions2.memory.AmbienteCompilacao import AmbienteCompilacao


class AmbienteCompilacaoImperativa(AmbienteCompilacao, ABC):

    @abstractmethod
    def getTipoEntrada(self) -> Tipo:
        raise NotImplementedError
