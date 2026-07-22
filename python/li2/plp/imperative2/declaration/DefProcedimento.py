from li2.plp.expressions1.util.Tipo import Tipo
from li2.plp.imperative1.command.Comando import Comando
from li2.plp.imperative2.declaration.ListaDeclaracaoParametro import ListaDeclaracaoParametro
from li2.plp.imperative2.util.TipoProcedimento import TipoProcedimento


class DefProcedimento:
    """Uma definicao de procedimento e uma declaracao de parametros formais e um comando."""

    def __init__(self, parametros_formais: ListaDeclaracaoParametro, comando: Comando):
        self._parametros_formais = parametros_formais
        self._comando = comando

    def getComando(self) -> Comando:
        return self._comando

    def getParametrosFormais(self) -> ListaDeclaracaoParametro:
        return self._parametros_formais

    def getTipo(self) -> Tipo:
        return TipoProcedimento(self._parametros_formais.getTipos())
