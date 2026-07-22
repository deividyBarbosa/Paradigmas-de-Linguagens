from li2.plp.expressions1.util.Tipo import Tipo
from li2.plp.expressions2.expression.Id import Id


class DeclaracaoParametro:

    def __init__(self, id_: Id, tipo: Tipo):
        self._id = id_
        self._tipo = tipo

    def getId(self) -> Id:
        return self._id

    def getTipo(self) -> Tipo:
        return self._tipo

    def checaTipo(self, ambiente: "AmbienteCompilacaoImperativa") -> bool:
        return self._tipo.eValido()

    def elabora(self, ambiente: "AmbienteCompilacaoImperativa") -> "AmbienteCompilacaoImperativa":
        """Cria um mapeamento do identificador para o tipo do parametro."""
        ambiente.map(self._id, self._tipo)
        return ambiente
