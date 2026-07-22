from le1.plp.expressions1.expression.Expressao import Expressao
from le1.plp.expressions1.expression.ExpUnaria import ExpUnaria
from le1.plp.expressions1.expression.ValorBooleano import ValorBooleano
from le1.plp.expressions1.util.Tipo import Tipo


class ExpNot(ExpUnaria):
    """Representa uma Expressao de Negacao logica."""

    def __init__(self, exp: Expressao):
        super().__init__(exp, "~")

    def avaliar(self) -> ValorBooleano:
        return ValorBooleano(not self.getExp().avaliar().valor())

    def _checaTipoElementoTerminal(self) -> bool:
        return self.getExp().getTipo().eBooleano()

    def getTipo(self) -> Tipo:
        return Tipo.TIPO_BOOLEANO
