from le1.plp.expressions1.expression.ExpBinaria import ExpBinaria
from le1.plp.expressions1.expression.Expressao import Expressao
from le1.plp.expressions1.expression.ValorString import ValorString
from le1.plp.expressions1.util.Tipo import Tipo


class ExpConcat(ExpBinaria):
    """Representa uma Expressao de Concatenacao entre objetos ValorString."""

    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "++")

    def avaliar(self) -> ValorString:
        return ValorString(self.getEsq().avaliar().valor() + self.getDir().avaliar().valor())

    def _checaTipoElementoTerminal(self) -> bool:
        return self.getEsq().getTipo().eString() and self.getDir().getTipo().eString()

    def getTipo(self) -> Tipo:
        return Tipo.TIPO_STRING
