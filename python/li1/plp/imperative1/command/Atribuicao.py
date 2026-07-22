from li1.plp.expressions2.expression.Expressao import Expressao
from li1.plp.expressions2.expression.Id import Id
from li1.plp.imperative1.command.Comando import Comando


class Atribuicao(Comando):

    def __init__(self, id_: Id, expressao: Expressao):
        self._id = id_
        self._expressao = expressao

    def executar(self, ambiente: "AmbienteExecucaoImperativa") -> "AmbienteExecucaoImperativa":
        ambiente.changeValor(self._id, self._expressao.avaliar(ambiente))
        return ambiente

    def checaTipo(self, ambiente: "AmbienteCompilacaoImperativa") -> bool:
        """
        Uma atribuicao esta bem tipada se o tipo do identificador e o mesmo
        da expressao (o tipo do identificador foi fixado na sua declaracao).
        """
        return self._expressao.checaTipo(ambiente) and self._id.getTipo(ambiente).eIgual(
            self._expressao.getTipo(ambiente)
        )
