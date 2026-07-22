from le2.plp.expressions1.util.Tipo import Tipo
from le2.plp.expressions2.expression.ExpBinaria import ExpBinaria
from le2.plp.expressions2.expression.Expressao import Expressao
from le2.plp.expressions2.expression.ValorInteiro import ValorInteiro


class ExpSub(ExpBinaria):
    """Representa uma Expressao de Subtracao."""

    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "-")

    def avaliar(self, amb: "AmbienteExecucao") -> ValorInteiro:
        return ValorInteiro(self.getEsq().avaliar(amb).valor() - self.getDir().avaliar(amb).valor())

    def _checaTipoElementoTerminal(self, amb: "AmbienteCompilacao") -> bool:
        return self.getEsq().getTipo(amb).eInteiro() and self.getDir().getTipo(amb).eInteiro()

    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        return Tipo.TIPO_INTEIRO
