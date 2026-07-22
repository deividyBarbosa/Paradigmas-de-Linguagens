from lf1.plp.expressions1.util.Tipo import Tipo
from lf1.plp.expressions2.expression.ExpBinaria import ExpBinaria
from lf1.plp.expressions2.expression.Expressao import Expressao
from lf1.plp.expressions2.expression.ValorBooleano import ValorBooleano


class ExpAnd(ExpBinaria):
    """Representa uma Expressao de Conjuncao logica."""

    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "and")

    def avaliar(self, amb: "AmbienteExecucao") -> ValorBooleano:
        return ValorBooleano(
            self.getEsq().avaliar(amb).valor() and self.getDir().avaliar(amb).valor()
        )

    def _checaTipoElementoTerminal(self, amb: "AmbienteCompilacao") -> bool:
        return self.getEsq().getTipo(amb).eBooleano() and self.getDir().getTipo(amb).eBooleano()

    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        return Tipo.TIPO_BOOLEANO
