from loo1.plp.imperative1.util.Lista import Lista
from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao
from loo1.plp.orientadaObjetos1.memoria.colecao.ListaValor import ListaValor
from loo1.plp.orientadaObjetos1.util.ListaTipo import ListaTipo


class ListaExpressao(Lista):
    """Uma lista de expressoes (argumentos reais de uma chamada de procedimento/metodo)."""

    def __init__(self, expressao: Expressao = None, lista_expressao: "ListaExpressao" = None):
        if expressao is None and lista_expressao is None:
            super().__init__()
        elif lista_expressao is None:
            super().__init__(expressao, ListaExpressao())
        else:
            super().__init__(expressao, lista_expressao)

    def avaliar(self, ambiente: "AmbienteExecucaoOO1") -> ListaValor:
        if self.length() >= 2:
            return ListaValor(self.getHead().avaliar(ambiente), self.getTail().avaliar(ambiente))
        elif self.length() == 1:
            return ListaValor(self.getHead().avaliar(ambiente))
        return ListaValor()

    def getTipos(self, ambiente: "AmbienteCompilacaoOO1") -> ListaTipo:
        if self.length() >= 2:
            return ListaTipo(self.getHead().getTipo(ambiente), self.getTail().getTipos(ambiente))
        elif self.length() == 1:
            return ListaTipo(self.getHead().getTipo(ambiente))
        return ListaTipo()
