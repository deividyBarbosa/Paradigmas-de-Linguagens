from typing import Dict, List

from lf1.plp.expressions2.memory.IdentificadorJaDeclaradoException import IdentificadorJaDeclaradoException
from lf1.plp.expressions2.memory.IdentificadorNaoDeclaradoException import IdentificadorNaoDeclaradoException


class StackHandler:
    """Operacoes utilitarias sobre uma pilha de blocos (Id -> Object) crua."""

    def __init__(self):
        raise TypeError("StackHandler nao deve ser instanciada")

    @staticmethod
    def getFromId(stack: List[Dict], id_):
        """Procura o objeto indexado por 'id_' nos blocos da pilha, do topo para a base."""
        for bloco in reversed(stack):
            if id_ in bloco:
                return bloco[id_]
        raise IdentificadorNaoDeclaradoException()

    @staticmethod
    def mapIdObject(stack: List[Dict], id_, objeto) -> None:
        """Adiciona um mapeamento no bloco do topo da pilha."""
        topo = stack[-1]
        if id_ in topo:
            raise IdentificadorJaDeclaradoException()
        topo[id_] = objeto
