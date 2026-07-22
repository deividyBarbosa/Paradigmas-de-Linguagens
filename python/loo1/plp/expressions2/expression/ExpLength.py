from loo1.plp.expressions1.util.Tipo import Tipo
from loo1.plp.expressions1.util.TipoPrimitivo import TipoPrimitivo
from loo1.plp.expressions2.expression.Expressao import Expressao
from loo1.plp.expressions2.expression.ExpUnaria import ExpUnaria
from loo1.plp.expressions2.expression.ValorInteiro import ValorInteiro


class ExpLength(ExpUnaria):
    """Representa uma Expressao de tamanho de String."""

    def __init__(self, exp: Expressao):
        super().__init__(exp, "length")

    def avaliar(self, amb: "AmbienteExecucao") -> ValorInteiro:
        return ValorInteiro(len(self.getExp().avaliar(amb).valor()))

    def _checaTipoElementoTerminal(self, amb: "AmbienteCompilacao") -> bool:
        return self.getExp().getTipo(amb).eString()

    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        return TipoPrimitivo.INTEIRO

    def clone(self) -> "ExpLength":
        return ExpLength(self._exp.clone())
