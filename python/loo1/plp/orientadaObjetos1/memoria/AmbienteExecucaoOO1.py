from abc import ABC, abstractmethod
from typing import Dict, List

from loo1.plp.expressions2.expression.Id import Id
from loo1.plp.orientadaObjetos1.expressao.valor.Valor import Valor
from loo1.plp.orientadaObjetos1.expressao.valor.ValorRef import ValorRef
from loo1.plp.orientadaObjetos1.memoria.AmbienteOO1 import AmbienteOO1


class AmbienteExecucaoOO1(AmbienteOO1[Valor], ABC):
    """Ambiente de execucao: mapeia Id -> Valor, alem do heap de objetos e E/S."""

    @abstractmethod
    def getPilha(self) -> List[Dict[Id, Valor]]:
        raise NotImplementedError

    @abstractmethod
    def getMapDefClasse(self) -> Dict[Id, "DefClasse"]:
        raise NotImplementedError

    @abstractmethod
    def getMapObjetos(self) -> Dict[ValorRef, "Objeto"]:
        raise NotImplementedError

    @abstractmethod
    def mapObjeto(self, valor_ref: ValorRef, objeto: "Objeto") -> None:
        raise NotImplementedError

    @abstractmethod
    def changeValor(self, id_arg: Id, valor_id: Valor) -> None:
        raise NotImplementedError

    @abstractmethod
    def getObjeto(self, valor_ref: ValorRef) -> "Objeto":
        raise NotImplementedError

    @abstractmethod
    def getProxRef(self) -> ValorRef:
        raise NotImplementedError

    @abstractmethod
    def getRef(self) -> ValorRef:
        raise NotImplementedError

    @abstractmethod
    def read(self, tipo_id_lido) -> Valor:
        raise NotImplementedError

    @abstractmethod
    def write(self, v: Valor) -> "AmbienteExecucaoOO1":
        raise NotImplementedError

    @abstractmethod
    def getEntrada(self) -> "ListaValor":
        raise NotImplementedError

    @abstractmethod
    def getSaida(self) -> "ListaValor":
        raise NotImplementedError

    @abstractmethod
    def getContextoIdValor(self) -> "ContextoExecucaoOO1":
        raise NotImplementedError

    @abstractmethod
    def getValor(self, id_arg: Id) -> Valor:
        raise NotImplementedError
