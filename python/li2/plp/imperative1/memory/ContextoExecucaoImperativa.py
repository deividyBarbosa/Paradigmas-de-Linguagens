from li2.plp.expressions2.expression.Id import Id
from li2.plp.expressions2.expression.Valor import Valor
from li2.plp.expressions2.memory.ContextoExecucao import ContextoExecucao
from li2.plp.expressions2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from li2.plp.imperative1.memory.AmbienteExecucaoImperativa import AmbienteExecucaoImperativa
from li2.plp.imperative1.memory.EntradaVaziaException import EntradaVaziaException
from li2.plp.imperative1.memory.ListaValor import ListaValor


class ContextoExecucaoImperativa(ContextoExecucao, AmbienteExecucaoImperativa):

    def __init__(self, entrada: ListaValor):
        super().__init__()
        self._entrada = entrada
        self._saida = ListaValor()

    def read(self) -> Valor:
        if self._entrada is None or self._entrada.getHead() is None:
            raise EntradaVaziaException()
        aux = self._entrada.getHead()
        self._entrada = self._entrada.getTail()
        return aux

    def getSaida(self) -> ListaValor:
        return self._saida

    def write(self, v: Valor) -> None:
        self._saida.write(v)

    def changeValor(self, id_arg: Id, valor_id: Valor) -> None:
        """Altera (in-place) o valor mapeado ao id, do bloco mais interno ao mais externo."""
        for bloco in reversed(self.getPilha()):
            if id_arg in bloco:
                bloco[id_arg] = valor_id
                return
        raise VariavelNaoDeclaradaException(id_arg)
