from le1.plp.expressions1.expression.Expressao import Expressao
from le1.plp.expressions1.expression.ExpUnaria import ExpUnaria
from le1.plp.expressions1.expression.ValorInteiro import ValorInteiro
from le1.plp.expressions1.util.Tipo import Tipo


class ExpMenos(ExpUnaria):
    """Representa uma Expressao de menos unario."""

    def __init__(self, exp: Expressao):
        super().__init__(exp, "-")

    def avaliar(self) -> ValorInteiro:
        return ValorInteiro(-self.getExp().avaliar().valor())

    def _checaTipoElementoTerminal(self) -> bool:
        return self.getExp().getTipo().eInteiro()

    def getTipo(self) -> Tipo:
        return Tipo.TIPO_INTEIRO
