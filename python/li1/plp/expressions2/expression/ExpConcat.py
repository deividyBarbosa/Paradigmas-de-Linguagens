from li1.plp.expressions1.util.Tipo import Tipo
from li1.plp.expressions1.util.TipoPrimitivo import TipoPrimitivo
from li1.plp.expressions2.expression.ExpBinaria import ExpBinaria
from li1.plp.expressions2.expression.Expressao import Expressao
from li1.plp.expressions2.expression.ValorString import ValorString


class ExpConcat(ExpBinaria):
    """Representa uma Expressao de Concatenacao entre objetos ValorString."""

    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "++")

    def avaliar(self, amb: "AmbienteExecucao") -> ValorString:
        return ValorString(self.getEsq().avaliar(amb).valor() + self.getDir().avaliar(amb).valor())

    def _checaTipoElementoTerminal(self, amb: "AmbienteCompilacao") -> bool:
        return self.getEsq().getTipo(amb).eString() and self.getDir().getTipo(amb).eString()

    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        return TipoPrimitivo.STRING

    def clone(self) -> "ExpConcat":
        return ExpConcat(self._esq.clone(), self._dir.clone())
