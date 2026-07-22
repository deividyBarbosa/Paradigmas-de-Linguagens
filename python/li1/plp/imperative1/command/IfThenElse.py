from li1.plp.expressions2.expression.Expressao import Expressao
from li1.plp.imperative1.command.Comando import Comando


class IfThenElse(Comando):

    def __init__(self, expressao: Expressao, comando_then: Comando, comando_else: Comando):
        self._expressao = expressao
        self._comando_then = comando_then
        self._comando_else = comando_else

    def executar(self, ambiente: "AmbienteExecucaoImperativa") -> "AmbienteExecucaoImperativa":
        if self._expressao.avaliar(ambiente).valor():
            return self._comando_then.executar(ambiente)
        return self._comando_else.executar(ambiente)

    def checaTipo(self, ambiente: "AmbienteCompilacaoImperativa") -> bool:
        return (
            self._expressao.checaTipo(ambiente)
            and self._expressao.getTipo(ambiente).eBooleano()
            and self._comando_then.checaTipo(ambiente)
            and self._comando_else.checaTipo(ambiente)
        )
