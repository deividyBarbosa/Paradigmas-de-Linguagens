from loo1.plp.orientadaObjetos1.comando.IO import IO
from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao


class Write(IO):
    """Comando de escrita (na saida padrao)."""

    def __init__(self, expressao: Expressao):
        self._expressao = expressao

    def executar(self, ambiente: "AmbienteExecucaoOO1") -> "AmbienteExecucaoOO1":
        valor = self._expressao.avaliar(ambiente)
        print(valor)
        return ambiente.write(valor)

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        return self._expressao.checaTipo(ambiente)
