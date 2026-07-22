from abc import ABC, abstractmethod

from loo1.plp.expressions2.expression.Id import Id
from loo1.plp.orientadaObjetos1.memoria.AmbienteOO1 import AmbienteOO1
from loo1.plp.orientadaObjetos1.util.Tipo import Tipo


class AmbienteCompilacaoOO1(AmbienteOO1[Tipo], ABC):
    """Ambiente de compilacao: mapeia Id -> Tipo, alem de metodos/procedimentos e classes."""

    @abstractmethod
    def getTipo(self, id_arg: Id) -> Tipo:
        raise NotImplementedError

    @abstractmethod
    def mapParametrosProcedimento(self, id_arg: Id, parametros_id: "ListaDeclaracaoParametro") -> None:
        raise NotImplementedError

    @abstractmethod
    def getParametrosProcedimento(self, id_arg: Id) -> "ListaDeclaracaoParametro":
        raise NotImplementedError

    @abstractmethod
    def getTipoEntrada(self) -> Tipo:
        raise NotImplementedError
