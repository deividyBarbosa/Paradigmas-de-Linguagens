from li1.plp.expressions1.util.Tipo import Tipo
from li1.plp.expressions1.util.TipoPrimitivo import TipoPrimitivo
from li1.plp.expressions2.expression.ExpBinaria import ExpBinaria
from li1.plp.expressions2.expression.Expressao import Expressao
from li1.plp.expressions2.expression.ValorBooleano import ValorBooleano


class ExpEquals(ExpBinaria):
    """Representa uma Expressao de Igualdade entre expressoes de mesmo valor primitivo."""

    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "==")

    def avaliar(self, amb: "AmbienteExecucao") -> ValorBooleano:
        return ValorBooleano(self.getEsq().avaliar(amb).isEquals(self.getDir().avaliar(amb)))

    def _checaTipoElementoTerminal(self, amb: "AmbienteCompilacao") -> bool:
        return self.getEsq().getTipo(amb).eIgual(self.getDir().getTipo(amb))

    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        return TipoPrimitivo.BOOLEANO

    def clone(self) -> "ExpEquals":
        return ExpEquals(self._esq.clone(), self._dir.clone())
