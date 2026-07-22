from le1.plp.expressions1.expression.ExpBinaria import ExpBinaria
from le1.plp.expressions1.expression.Expressao import Expressao
from le1.plp.expressions1.expression.ValorInteiro import ValorInteiro
from le1.plp.expressions1.util.Tipo import Tipo


class ExpSub(ExpBinaria):
    """Representa uma Expressao de Subtracao."""

    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "-")

    def avaliar(self) -> ValorInteiro:
        return ValorInteiro(self.getEsq().avaliar().valor() - self.getDir().avaliar().valor())

    def _checaTipoElementoTerminal(self) -> bool:
        return self.getEsq().getTipo().eInteiro() and self.getDir().getTipo().eInteiro()

    def getTipo(self) -> Tipo:
        return Tipo.TIPO_INTEIRO
