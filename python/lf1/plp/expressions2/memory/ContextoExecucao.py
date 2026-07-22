from lf1.plp.expressions2.expression.Valor import Valor
from lf1.plp.expressions2.memory.AmbienteExecucao import AmbienteExecucao
from lf1.plp.expressions2.memory.Contexto import Contexto


class ContextoExecucao(Contexto[Valor], AmbienteExecucao):

    def clone(self) -> "ContextoExecucao":
        ret = ContextoExecucao()
        ret.setPilha(list(self.getPilha()))
        return ret
