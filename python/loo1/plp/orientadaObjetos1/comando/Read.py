from loo1.plp.orientadaObjetos1.comando.IO import IO
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id


class Read(IO):
    """Representa um comando de leitura (da entrada padrao)."""

    def __init__(self, id_: Id):
        self._id = id_
        self._tipo_id = None

    def executar(self, ambiente: "AmbienteExecucaoOO1") -> "AmbienteExecucaoOO1":
        ambiente.changeValor(self._id, ambiente.read(self._tipo_id))
        return ambiente

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        # Em tempo de compilacao nao se pode saber o tipo da entrada que sera lida;
        # o tipo e obtido a partir do proprio identificador declarado.
        self._tipo_id = self._id.getTipo(ambiente)
        return self._id.checaTipo(ambiente)
