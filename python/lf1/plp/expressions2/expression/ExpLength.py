from lf1.plp.expressions1.util.Tipo import Tipo
from lf1.plp.expressions2.expression.Expressao import Expressao
from lf1.plp.expressions2.expression.ExpUnaria import ExpUnaria
from lf1.plp.expressions2.expression.ValorInteiro import ValorInteiro


class ExpLength(ExpUnaria):
    """Representa uma Expressao de tamanho de String."""

    def __init__(self, exp: Expressao):
        super().__init__(exp, "length")

    def avaliar(self, amb: "AmbienteExecucao") -> ValorInteiro:
        return ValorInteiro(len(self.getExp().avaliar(amb).valor()))

    def _checaTipoElementoTerminal(self, amb: "AmbienteCompilacao") -> bool:
        return self.getExp().getTipo(amb).eString()

    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        return Tipo.TIPO_INTEIRO
