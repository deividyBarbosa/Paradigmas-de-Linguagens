from li1.plp.expressions1.util.Tipo import Tipo
from li1.plp.expressions1.util.TipoPrimitivo import TipoPrimitivo
from li1.plp.expressions2.expression.ExpBinaria import ExpBinaria
from li1.plp.expressions2.expression.Expressao import Expressao
from li1.plp.expressions2.expression.ValorBooleano import ValorBooleano


class ExpAnd(ExpBinaria):
    """Representa uma Expressao de Conjuncao logica."""

    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "and")

    def avaliar(self, amb: "AmbienteExecucao") -> ValorBooleano:
        return ValorBooleano(
            self.getEsq().avaliar(amb).valor() and self.getDir().avaliar(amb).valor()
        )

    def _checaTipoElementoTerminal(self, amb: "AmbienteCompilacao") -> bool:
        return self.getEsq().getTipo(amb).eBooleano() and self.getDir().getTipo(amb).eBooleano()

    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        return TipoPrimitivo.BOOLEANO

    def clone(self) -> "ExpAnd":
        return ExpAnd(self._esq.clone(), self._dir.clone())
