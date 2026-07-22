from li2.plp.expressions2.expression.Expressao import Expressao
from li2.plp.expressions2.expression.Id import Id
from li2.plp.imperative1.declaration.Declaracao import Declaracao


class DeclaracaoVariavel(Declaracao):
    """Declara uma variavel, mapeando o identificador ao valor de sua expressao de inicializacao."""

    def __init__(self, id_: Id, expressao: Expressao):
        self._id = id_
        self._expressao = expressao

    def elabora(self, ambiente: "AmbienteExecucaoImperativa") -> "AmbienteExecucaoImperativa":
        ambiente.map(self.getId(), self.getExpressao().avaliar(ambiente))
        return ambiente

    def getExpressao(self) -> Expressao:
        return self._expressao

    def getId(self) -> Id:
        return self._id

    def checaTipo(self, ambiente: "AmbienteCompilacaoImperativa") -> bool:
        """O tipo da variavel e o tipo do valor de sua primeira atribuicao (a expressao de inicializacao)."""
        result = self.getExpressao().checaTipo(ambiente)
        if result:
            ambiente.map(self.getId(), self.getExpressao().getTipo(ambiente))
        return result
