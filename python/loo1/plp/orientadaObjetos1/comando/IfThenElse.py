from loo1.plp.orientadaObjetos1.comando.Comando import Comando
from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao


class IfThenElse(Comando):
    """Comando 'if then else'."""

    def __init__(self, expressao: Expressao, comando_then: Comando, comando_else: Comando):
        self._expressao = expressao
        self._comando_then = comando_then
        self._comando_else = comando_else

    def executar(self, ambiente: "AmbienteExecucaoOO1") -> "AmbienteExecucaoOO1":
        if self._expressao.avaliar(ambiente).valor():
            return self._comando_then.executar(ambiente)
        return self._comando_else.executar(ambiente)

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        return (
            self._expressao.checaTipo(ambiente)
            and self._expressao.getTipo(ambiente).eBooleano()
            and self._comando_then.checaTipo(ambiente)
            and self._comando_else.checaTipo(ambiente)
        )
