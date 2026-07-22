from li1.plp.expressions1.util.Tipo import Tipo
from li1.plp.expressions1.util.TipoPrimitivo import TipoPrimitivo
from li1.plp.expressions2.expression.ExpBinaria import ExpBinaria
from li1.plp.expressions2.expression.Expressao import Expressao
from li1.plp.expressions2.expression.ValorInteiro import ValorInteiro


class ExpSub(ExpBinaria):
    """Representa uma Expressao de Subtracao."""

    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "-")

    def avaliar(self, amb: "AmbienteExecucao") -> ValorInteiro:
        return ValorInteiro(self.getEsq().avaliar(amb).valor() - self.getDir().avaliar(amb).valor())

    def _checaTipoElementoTerminal(self, amb: "AmbienteCompilacao") -> bool:
        return self.getEsq().getTipo(amb).eInteiro() and self.getDir().getTipo(amb).eInteiro()

    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        return TipoPrimitivo.INTEIRO

    def clone(self) -> "ExpSub":
        return ExpSub(self._esq.clone(), self._dir.clone())
