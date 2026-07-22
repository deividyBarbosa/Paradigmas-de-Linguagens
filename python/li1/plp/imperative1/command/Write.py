from li1.plp.expressions2.expression.Expressao import Expressao
from li1.plp.imperative1.command.IO import IO


class Write(IO):

    def __init__(self, expressao: Expressao):
        self._expressao = expressao

    def executar(self, ambiente: "AmbienteExecucaoImperativa") -> "AmbienteExecucaoImperativa":
        ambiente.write(self._expressao.avaliar(ambiente))
        return ambiente

    def checaTipo(self, ambiente: "AmbienteCompilacaoImperativa") -> bool:
        return self._expressao.checaTipo(ambiente)
