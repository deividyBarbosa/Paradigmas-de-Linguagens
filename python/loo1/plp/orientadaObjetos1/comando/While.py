from loo1.plp.orientadaObjetos1.comando.Comando import Comando
from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao


class While(Comando):
    """Comando 'while'."""

    def __init__(self, expressao: Expressao, comando: Comando):
        self._expressao = expressao
        self._comando = comando

    def executar(self, ambiente: "AmbienteExecucaoOO1") -> "AmbienteExecucaoOO1":
        while self._expressao.avaliar(ambiente).valor():
            ambiente = self._comando.executar(ambiente)
        return ambiente

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        return (
            self._expressao.checaTipo(ambiente)
            and self._expressao.getTipo(ambiente).eBooleano()
            and self._comando.checaTipo(ambiente)
        )
