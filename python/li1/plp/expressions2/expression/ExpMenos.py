from li1.plp.expressions1.util.Tipo import Tipo
from li1.plp.expressions1.util.TipoPrimitivo import TipoPrimitivo
from li1.plp.expressions2.expression.Expressao import Expressao
from li1.plp.expressions2.expression.ExpUnaria import ExpUnaria
from li1.plp.expressions2.expression.ValorInteiro import ValorInteiro


class ExpMenos(ExpUnaria):
    """Representa uma Expressao de menos unario."""

    def __init__(self, exp: Expressao):
        super().__init__(exp, "-")

    def avaliar(self, amb: "AmbienteExecucao") -> ValorInteiro:
        return ValorInteiro(-self.getExp().avaliar(amb).valor())

    def _checaTipoElementoTerminal(self, amb: "AmbienteCompilacao") -> bool:
        return self.getExp().getTipo(amb).eInteiro()

    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        return TipoPrimitivo.INTEIRO

    def clone(self) -> "ExpMenos":
        return ExpMenos(self._exp.clone())
