from li2.plp.expressions2.expression.Valor import Valor
from li2.plp.expressions2.memory.AmbienteExecucao import AmbienteExecucao
from li2.plp.expressions2.memory.Contexto import Contexto


class ContextoExecucao(Contexto[Valor], AmbienteExecucao):

    def clone(self) -> "ContextoExecucao":
        retorno = ContextoExecucao()
        novo_mapa = {}
        for bloco in self._pilha:
            novo_mapa.update(bloco)
        retorno.setPilha([novo_mapa])
        return retorno
