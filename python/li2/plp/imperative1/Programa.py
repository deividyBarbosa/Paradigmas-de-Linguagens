from li2.plp.imperative1.command.Comando import Comando
from li2.plp.imperative1.memory.AmbienteCompilacaoImperativa import AmbienteCompilacaoImperativa
from li2.plp.imperative1.memory.AmbienteExecucaoImperativa import AmbienteExecucaoImperativa
from li2.plp.imperative1.memory.ListaValor import ListaValor


class Programa:
    """Um programa em li2: um comando a ser executado sobre um ambiente imperativo."""

    def __init__(self, comando: Comando):
        self._comando = comando

    def executar(self, ambiente_execucao: AmbienteExecucaoImperativa) -> ListaValor:
        ambiente_execucao = self._comando.executar(ambiente_execucao)
        return ambiente_execucao.getSaida()

    def checaTipo(self, ambiente_compilacao: AmbienteCompilacaoImperativa) -> bool:
        return self._comando.checaTipo(ambiente_compilacao)
