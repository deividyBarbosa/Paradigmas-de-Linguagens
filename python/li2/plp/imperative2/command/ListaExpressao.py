from typing import List

from li2.plp.expressions1.util.Tipo import Tipo
from li2.plp.expressions2.expression.Expressao import Expressao
from li2.plp.imperative1.memory.ListaValor import ListaValor
from li2.plp.imperative1.util.Lista import Lista


class ListaExpressao(Lista[Expressao]):

    def __init__(self, expressao: Expressao = None, lista_expressao: "ListaExpressao" = None):
        if expressao is None and lista_expressao is None:
            super().__init__()
        elif lista_expressao is None:
            super().__init__(expressao, ListaExpressao())
        else:
            super().__init__(expressao, lista_expressao)

    def avaliar(self, ambiente: "AmbienteExecucaoImperativa") -> ListaValor:
        if self.length() >= 2:
            return ListaValor(self.getHead().avaliar(ambiente), self.getTail().avaliar(ambiente))
        elif self.length() == 1:
            return ListaValor(self.getHead().avaliar(ambiente))
        return ListaValor()

    def getTipos(self, ambiente: "AmbienteCompilacaoImperativa") -> List[Tipo]:
        result: List[Tipo] = []
        if self.length() >= 2:
            result.append(self.getHead().getTipo(ambiente))
            result.extend(self.getTail().getTipos(ambiente))
        elif self.length() == 1:
            result.append(self.getHead().getTipo(ambiente))
        return result
