from loo1.plp.orientadaObjetos1.comando.Comando import Comando
from loo1.plp.orientadaObjetos1.declaracao.classe.DecClasse import DecClasse
from loo1.plp.orientadaObjetos1.excecao.execucao.EntradaNaoFornecidaException import EntradaNaoFornecidaException
from loo1.plp.orientadaObjetos1.memoria.AmbienteCompilacaoOO1 import AmbienteCompilacaoOO1
from loo1.plp.orientadaObjetos1.memoria.AmbienteExecucaoOO1 import AmbienteExecucaoOO1
from loo1.plp.orientadaObjetos1.memoria.colecao.ListaValor import ListaValor


class Programa:
    """Representa um programa na linguagem orientada a objetos."""

    def __init__(self, dec_classe: DecClasse, comando: Comando):
        self._dec_classe = dec_classe
        self._comando = comando

    def executar(self, ambiente: AmbienteExecucaoOO1) -> ListaValor:
        if ambiente is None:
            raise EntradaNaoFornecidaException()

        # Nao precisa incrementar no inicio, ja que nao existe a possibilidade
        # de declarar variaveis antes de uma declaracao de classes.
        ambiente = self._comando.executar(self._dec_classe.elabora(ambiente))
        return ambiente.getSaida()

    def checaTipo(self, ambiente: AmbienteCompilacaoOO1) -> bool:
        if ambiente is None:
            raise EntradaNaoFornecidaException()

        return self._dec_classe.checaTipo(ambiente) and self._comando.checaTipo(ambiente)
