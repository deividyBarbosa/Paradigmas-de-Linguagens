from le1.plp.expressions1.expression.ExpBinaria import ExpBinaria
from le1.plp.expressions1.expression.Expressao import Expressao
from le1.plp.expressions1.expression.ValorBooleano import ValorBooleano
from le1.plp.expressions1.util.Tipo import Tipo


class ExpAnd(ExpBinaria):
    """Representa uma Expressao de Conjuncao logica."""

    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "and")

    def avaliar(self) -> ValorBooleano:
        return ValorBooleano(
            self.getEsq().avaliar().valor() and self.getDir().avaliar().valor()
        )

    def _checaTipoElementoTerminal(self) -> bool:
        return self.getEsq().getTipo().eBooleano() and self.getDir().getTipo().eBooleano()

    def getTipo(self) -> Tipo:
        return Tipo.TIPO_BOOLEANO
