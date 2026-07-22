from loo1.plp.orientadaObjetos1.comando.Comando import Comando
from loo1.plp.orientadaObjetos1.comando.Procedimento import Procedimento
from loo1.plp.orientadaObjetos1.expressao.ListaExpressao import ListaExpressao
from loo1.plp.orientadaObjetos1.memoria.colecao.ListaValor import ListaValor


class ChamadaProcedimento(Comando):
    """Representa uma chamada a um procedimento (ja resolvido)."""

    def __init__(self, procedimento: Procedimento, parametros_reais: ListaExpressao,
                 valores_parametros: ListaValor = None):
        self._procedimento = procedimento
        self._parametros_reais = parametros_reais
        self._valores_parametros = valores_parametros

    def executar(self, ambiente: "AmbienteExecucaoOO1") -> "AmbienteExecucaoOO1":
        ambiente.incrementa()
        ambiente = self._bindParameters(ambiente, self._procedimento.getParametrosFormais())
        ambiente = self._procedimento.getComando().executar(ambiente)
        ambiente.restaura()
        return ambiente

    def _bindParameters(self, ambiente: "AmbienteExecucaoOO1", parametros_formais) -> "AmbienteExecucaoOO1":
        """Insere no contexto a associacao entre cada parametro formal e seu parametro real correspondente."""
        lista_valor = self._valores_parametros
        if lista_valor is None:
            lista_valor = self._parametros_reais.avaliar(ambiente)
        while lista_valor.length() > 0:
            ambiente.map(parametros_formais.getHead().getId(), lista_valor.getHead())
            parametros_formais = parametros_formais.getTail()
            lista_valor = lista_valor.getTail()
        return ambiente

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        """Os tipos dos parametros formais devem ser iguais aos dos parametros reais, na ordem em que se apresentam."""
        ambiente.incrementa()
        parametros_formais = self._procedimento.getParametrosFormais()
        lista_tipo = self._parametros_reais.getTipos(ambiente)
        if lista_tipo.length() == parametros_formais.length():
            if lista_tipo.head() is None or parametros_formais.getHead() is None:
                resposta = True
            else:
                resposta = True
                while lista_tipo is not None and parametros_formais is not None:
                    if lista_tipo.head() != parametros_formais.getHead().getTipo():
                        resposta = False
                        break
                    lista_tipo = lista_tipo.tail()
                    parametros_formais = parametros_formais.getTail()
        else:
            resposta = False
        ambiente.restaura()
        return resposta
