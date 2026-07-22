from li1.plp.expressions2.expression.Expressao import Expressao
from li1.plp.imperative1.command.Comando import Comando


class While(Comando):

    def __init__(self, expressao: Expressao, comando: Comando):
        self._expressao = expressao
        self._comando = comando

    def executar(self, ambiente: "AmbienteExecucaoImperativa") -> "AmbienteExecucaoImperativa":
        while self._expressao.avaliar(ambiente).valor():
            ambiente = self._comando.executar(ambiente)
        return ambiente

    def checaTipo(self, ambiente: "AmbienteCompilacaoImperativa") -> bool:
        return (
            self._expressao.checaTipo(ambiente)
            and self._expressao.getTipo(ambiente).eBooleano()
            and self._comando.checaTipo(ambiente)
        )
