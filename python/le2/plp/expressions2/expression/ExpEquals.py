from le2.plp.expressions1.util.Tipo import Tipo
from le2.plp.expressions2.expression.ExpBinaria import ExpBinaria
from le2.plp.expressions2.expression.Expressao import Expressao
from le2.plp.expressions2.expression.ValorBooleano import ValorBooleano


class ExpEquals(ExpBinaria):
    """Representa uma Expressao de Igualdade entre expressoes de mesmo valor primitivo."""

    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "==")

    def avaliar(self, amb: "AmbienteExecucao") -> ValorBooleano:
        return ValorBooleano(self.getEsq().avaliar(amb).isEquals(self.getDir().avaliar(amb)))

    def _checaTipoElementoTerminal(self, amb: "AmbienteCompilacao") -> bool:
        # Diferente da le1: aqui basta que os tipos possiveis se interceptem,
        # nao que sejam identicos (necessario pois identificadores podem ter
        # tipo indefinido antes de resolvidos).
        return not self.getEsq().getTipo(amb).intersecao(self.getDir().getTipo(amb)).eVoid()

    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        return Tipo.TIPO_BOOLEANO
