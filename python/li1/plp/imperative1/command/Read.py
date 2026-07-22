from li1.plp.expressions2.expression.Id import Id
from li1.plp.imperative1.command.IO import IO
from li1.plp.imperative1.memory.ErroTipoEntradaException import ErroTipoEntradaException


class Read(IO):

    def __init__(self, id_: Id):
        self._id = id_

    def executar(self, ambiente: "AmbienteExecucaoImperativa") -> "AmbienteExecucaoImperativa":
        valor_id = ambiente.get(self._id)
        valor_read = ambiente.read()
        if valor_id.getTipo(None).eIgual(valor_read.getTipo(None)):
            ambiente.changeValor(self._id, valor_read)
        else:
            raise ErroTipoEntradaException(
                f"Tipo do valor de entrada lido incompativel com tipo da variavel ({self._id.getIdName()})"
            )
        return ambiente

    def checaTipo(self, ambiente: "AmbienteCompilacaoImperativa") -> bool:
        return True
