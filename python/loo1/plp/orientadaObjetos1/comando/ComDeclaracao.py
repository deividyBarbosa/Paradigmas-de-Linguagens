from loo1.plp.orientadaObjetos1.comando.Comando import Comando
from loo1.plp.orientadaObjetos1.declaracao.Declaracao import Declaracao


class ComDeclaracao(Comando):
    """Representa um comando de declaracao: declara variavel(is) e executa um comando."""

    def __init__(self, declaracao: Declaracao, comando: Comando):
        self._declaracao = declaracao
        self._comando = comando

    def executar(self, ambiente: "AmbienteExecucaoOO1") -> "AmbienteExecucaoOO1":
        ambiente.incrementa()
        ambiente = self._comando.executar(self._declaracao.elabora(ambiente))
        ambiente.restaura()
        return ambiente

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        """Leva em conta que o tipo de uma variavel e o tipo do valor da sua primeira atribuicao."""
        ambiente.incrementa()
        resposta = self._declaracao.checaTipo(ambiente) and self._comando.checaTipo(ambiente)
        ambiente.restaura()
        return resposta
