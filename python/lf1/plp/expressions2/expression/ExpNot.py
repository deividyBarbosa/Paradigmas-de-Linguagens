from lf1.plp.expressions1.util.Tipo import Tipo
from lf1.plp.expressions2.expression.Expressao import Expressao
from lf1.plp.expressions2.expression.ExpUnaria import ExpUnaria
from lf1.plp.expressions2.expression.ValorBooleano import ValorBooleano


class ExpNot(ExpUnaria):
    """Representa uma Expressao de Negacao logica."""

    def __init__(self, exp: Expressao):
        super().__init__(exp, "~")

    def avaliar(self, amb: "AmbienteExecucao") -> ValorBooleano:
        return ValorBooleano(not self.getExp().avaliar(amb).valor())

    def _checaTipoElementoTerminal(self, amb: "AmbienteCompilacao") -> bool:
        return self.getExp().getTipo(amb).eBooleano()

    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        return Tipo.TIPO_BOOLEANO
