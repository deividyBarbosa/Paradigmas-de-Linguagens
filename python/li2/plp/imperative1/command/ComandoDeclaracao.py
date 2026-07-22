from li2.plp.imperative1.command.Comando import Comando
from li2.plp.imperative1.declaration.Declaracao import Declaracao


class ComandoDeclaracao(Comando):
    """Declara variavel(is) num novo bloco e executa um comando nesse escopo."""

    def __init__(self, declaracao: Declaracao, comando: Comando):
        self._declaracao = declaracao
        self._comando = comando

    def executar(self, ambiente: "AmbienteExecucaoImperativa") -> "AmbienteExecucaoImperativa":
        ambiente.incrementa()
        ambiente = self._comando.executar(self._declaracao.elabora(ambiente))
        ambiente.restaura()
        return ambiente

    def checaTipo(self, ambiente: "AmbienteCompilacaoImperativa") -> bool:
        """Leva em conta que o tipo de uma variavel e o tipo do valor da sua primeira atribuicao."""
        ambiente.incrementa()
        resposta = self._declaracao.checaTipo(ambiente) and self._comando.checaTipo(ambiente)
        ambiente.restaura()
        return resposta
