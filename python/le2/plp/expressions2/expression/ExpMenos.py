from le2.plp.expressions1.util.Tipo import Tipo
from le2.plp.expressions2.expression.Expressao import Expressao
from le2.plp.expressions2.expression.ExpUnaria import ExpUnaria
from le2.plp.expressions2.expression.ValorInteiro import ValorInteiro


class ExpMenos(ExpUnaria):
    """Representa uma Expressao de menos unario."""

    def __init__(self, exp: Expressao):
        super().__init__(exp, "-")

    def avaliar(self, amb: "AmbienteExecucao") -> ValorInteiro:
        return ValorInteiro(-self.getExp().avaliar(amb).valor())

    def _checaTipoElementoTerminal(self, amb: "AmbienteCompilacao") -> bool:
        return self.getExp().getTipo(amb).eInteiro()

    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        return Tipo.TIPO_INTEIRO
