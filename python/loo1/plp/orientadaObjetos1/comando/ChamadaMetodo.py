from loo1.plp.orientadaObjetos1.comando.ChamadaProcedimento import ChamadaProcedimento
from loo1.plp.orientadaObjetos1.comando.Comando import Comando
from loo1.plp.orientadaObjetos1.excecao.declaracao.ProcedimentoNaoDeclaradoException import (
    ProcedimentoNaoDeclaradoException,
)
from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao
from loo1.plp.orientadaObjetos1.expressao.ListaExpressao import ListaExpressao
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
from loo1.plp.orientadaObjetos1.memoria.ContextoExecucaoOO1 import ContextoExecucaoOO1


class ChamadaMetodo(Comando):
    """Representa a chamada de um metodo de um objeto."""

    def __init__(self, expressao: Expressao, nome_metodo: Id, parametros_reais: ListaExpressao):
        self._expressao = expressao
        self._nome_metodo = nome_metodo
        self._parametros_reais = parametros_reais

    def executar(self, ambiente: "AmbienteExecucaoOO1") -> "AmbienteExecucaoOO1":
        vr = self._expressao.avaliar(ambiente)  # recupera a referencia do objeto
        objeto = ambiente.getObjeto(vr)  # recupera o objeto
        id_classe = objeto.getClasse()  # recupera o "tipo" (classe) do objeto
        def_classe = ambiente.getDefClasse(id_classe)  # recupera a definicao da classe
        metodo = def_classe.getMetodo(self._nome_metodo)  # recupera o procedimento

        # Cria um novo ambiente para a execucao, pois nao deve levar em conta
        # as variaveis definidas no escopo chamador.
        aux = ContextoExecucaoOO1(ambiente=ambiente)
        aux.changeValor(Id("this"), vr)  # o construtor ja mapeia "this"; aqui so trocamos o valor

        valores_dos_parametros = self._parametros_reais.avaliar(ambiente)
        ChamadaProcedimento(metodo, self._parametros_reais, valores_dos_parametros).executar(aux)
        return ambiente

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        """O tipo do metodo deve estar na definicao da classe obtida a partir de 'expressao'."""
        tipo_classe = self._expressao.getTipo(ambiente)
        def_classe = ambiente.getDefClasse(tipo_classe.getTipo())
        try:
            metodo = def_classe.getMetodo(self._nome_metodo)
            ambiente.incrementa()
            ambiente.map(Id("this"), tipo_classe)
            resposta = ChamadaProcedimento(metodo, self._parametros_reais).checaTipo(ambiente)
            ambiente.restaura()
        except ProcedimentoNaoDeclaradoException:
            resposta = False
        return resposta
