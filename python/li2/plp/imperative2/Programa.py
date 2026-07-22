from li2.plp.imperative1.command.Comando import Comando
from li2.plp.imperative1.memory.AmbienteCompilacaoImperativa import AmbienteCompilacaoImperativa
from li2.plp.imperative1.memory.AmbienteExecucaoImperativa import AmbienteExecucaoImperativa
from li2.plp.imperative1.memory.ListaValor import ListaValor


class Programa:
    """Um programa em li2: um comando (possivelmente com procedimentos) a ser executado."""

    def __init__(self, comando: Comando):
        self._comando = comando

    def executar(self, ambiente: AmbienteExecucaoImperativa) -> ListaValor:
        ambiente = self._comando.executar(ambiente)
        return ambiente.getSaida()

    def checaTipo(self, ambiente: AmbienteCompilacaoImperativa) -> bool:
        return self._comando.checaTipo(ambiente)
