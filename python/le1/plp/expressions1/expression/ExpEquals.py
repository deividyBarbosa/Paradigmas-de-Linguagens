from le1.plp.expressions1.expression.ExpBinaria import ExpBinaria
from le1.plp.expressions1.expression.Expressao import Expressao
from le1.plp.expressions1.expression.ValorBooleano import ValorBooleano
from le1.plp.expressions1.util.Tipo import Tipo


class ExpEquals(ExpBinaria):
    """Representa uma Expressao de Igualdade entre expressoes de mesmo valor primitivo."""

    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "==")

    def avaliar(self) -> ValorBooleano:
        return ValorBooleano(self.getEsq().avaliar().isEquals(self.getDir().avaliar()))

    def _checaTipoElementoTerminal(self) -> bool:
        return self.getEsq().getTipo() == self.getDir().getTipo()

    def getTipo(self) -> Tipo:
        return Tipo.TIPO_BOOLEANO
