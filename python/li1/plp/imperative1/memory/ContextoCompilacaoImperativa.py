from li1.plp.expressions1.util.Tipo import Tipo
from li1.plp.expressions2.memory.ContextoCompilacao import ContextoCompilacao
from li1.plp.imperative1.memory.AmbienteCompilacaoImperativa import AmbienteCompilacaoImperativa
from li1.plp.imperative1.memory.EntradaVaziaException import EntradaVaziaException
from li1.plp.imperative1.memory.ListaValor import ListaValor


class ContextoCompilacaoImperativa(ContextoCompilacao, AmbienteCompilacaoImperativa):

    def __init__(self, entrada: ListaValor):
        super().__init__()
        self._entrada = entrada

    def getTipoEntrada(self) -> Tipo:
        if self._entrada is None or self._entrada.getHead() is None:
            raise EntradaVaziaException()
        aux = self._entrada.getHead().getTipo(self)
        self._entrada = self._entrada.getTail()
        return aux
