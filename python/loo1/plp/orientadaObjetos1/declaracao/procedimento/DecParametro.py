from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
from loo1.plp.orientadaObjetos1.util.Tipo import Tipo


class DecParametro:
    """Declaracao de um parametro formal (identificador + tipo)."""

    def __init__(self, id_: Id, tipo: Tipo):
        self._id = id_
        self._tipo = tipo

    def getId(self) -> Id:
        return self._id

    def getTipo(self) -> Tipo:
        return self._tipo

    def elabora(self, ambiente: "AmbienteExecucaoOO1") -> "AmbienteExecucaoOO1":
        return ambiente

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        return self._tipo.eValido(ambiente)

    def declaraParametro(self, ambiente: "AmbienteCompilacaoOO1") -> "AmbienteCompilacaoOO1":
        """Cria um mapeamento do identificador para o tipo do parametro no AmbienteCompilacao."""
        ambiente.map(self._id, self._tipo)
        return ambiente
