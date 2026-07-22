from le1.plp.expressions1.expression.Expressao import Expressao
from le1.plp.expressions1.expression.ExpUnaria import ExpUnaria
from le1.plp.expressions1.expression.ValorInteiro import ValorInteiro
from le1.plp.expressions1.util.Tipo import Tipo


class ExpLength(ExpUnaria):
    """Representa uma Expressao de tamanho de String."""

    def __init__(self, exp: Expressao):
        super().__init__(exp, "length")

    def avaliar(self) -> ValorInteiro:
        return ValorInteiro(len(self.getExp().avaliar().valor()))

    def _checaTipoElementoTerminal(self) -> bool:
        return self.getExp().getTipo().eString()

    def getTipo(self) -> Tipo:
        return Tipo.TIPO_INTEIRO
