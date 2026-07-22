from li2.plp.expressions2.expression.Id import Id
from li2.plp.expressions2.memory.Contexto import Contexto
from li2.plp.expressions2.memory.VariavelJaDeclaradaException import VariavelJaDeclaradaException
from li2.plp.expressions2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from li2.plp.imperative1.memory.ContextoExecucaoImperativa import ContextoExecucaoImperativa
from li2.plp.imperative1.memory.ListaValor import ListaValor
from li2.plp.imperative2.memory.AmbienteExecucaoImperativa2 import AmbienteExecucaoImperativa2
from li2.plp.imperative2.memory.ProcedimentoJaDeclaradoException import ProcedimentoJaDeclaradoException
from li2.plp.imperative2.memory.ProcedimentoNaoDeclaradoException import ProcedimentoNaoDeclaradoException


class ContextoExecucaoImperativa2(ContextoExecucaoImperativa, AmbienteExecucaoImperativa2):
    """O contexto de procedimentos funciona como um contexto de execucao paralelo, que armazena apenas procedimentos."""

    def __init__(self, entrada: ListaValor):
        super().__init__(entrada)
        self._contexto_procedimentos: Contexto = Contexto()

    def incrementa(self) -> None:
        super().incrementa()
        self._contexto_procedimentos.incrementa()

    def restaura(self) -> None:
        super().restaura()
        self._contexto_procedimentos.restaura()

    def mapProcedimento(self, id_arg: Id, procedimento_id: "DefProcedimento") -> None:
        try:
            self._contexto_procedimentos.map(id_arg, procedimento_id)
        except VariavelJaDeclaradaException:
            raise ProcedimentoJaDeclaradoException(id_arg)

    def getProcedimento(self, id_arg: Id) -> "DefProcedimento":
        try:
            return self._contexto_procedimentos.get(id_arg)
        except VariavelNaoDeclaradaException:
            raise ProcedimentoNaoDeclaradoException(id_arg)
