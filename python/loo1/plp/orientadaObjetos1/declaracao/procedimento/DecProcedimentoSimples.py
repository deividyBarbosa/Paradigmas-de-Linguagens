from loo1.plp.orientadaObjetos1.comando.Comando import Comando
from loo1.plp.orientadaObjetos1.comando.Procedimento import Procedimento
from loo1.plp.orientadaObjetos1.declaracao.procedimento.DecProcedimento import DecProcedimento
from loo1.plp.orientadaObjetos1.declaracao.procedimento.ListaDeclaracaoParametro import ListaDeclaracaoParametro
from loo1.plp.orientadaObjetos1.excecao.declaracao.ProcedimentoNaoDeclaradoException import (
    ProcedimentoNaoDeclaradoException,
)
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id


class DecProcedimentoSimples(DecProcedimento):
    """Representa a declaracao de um unico procedimento (metodo)."""

    def __init__(self, nome: Id, parametros_formais: ListaDeclaracaoParametro, comando: Comando):
        self._nome = nome
        self._parametros_formais = parametros_formais
        self._comando = comando

    def getProcedimento(self, nome: Id) -> Procedimento:
        if self._nome == nome:
            return Procedimento(self._parametros_formais, self._comando)
        raise ProcedimentoNaoDeclaradoException(nome)

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        if self._parametros_formais.checaTipo(ambiente):
            ambiente.mapParametrosProcedimento(self._nome, self._parametros_formais)
            ambiente.incrementa()
            ambiente = self._parametros_formais.declaraParametro(ambiente)
            resposta = self._comando.checaTipo(ambiente)
            ambiente.restaura()
            return resposta
        return False
