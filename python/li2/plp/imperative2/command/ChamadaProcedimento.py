from li2.plp.expressions2.expression.Id import Id
from li2.plp.imperative1.command.Comando import Comando
from li2.plp.imperative2.command.ListaExpressao import ListaExpressao
from li2.plp.imperative2.util.TipoProcedimento import TipoProcedimento


class ChamadaProcedimento(Comando):

    def __init__(self, nome_procedimento: Id, parametros_reais: ListaExpressao):
        self._nome_procedimento = nome_procedimento
        self._parametros_reais = parametros_reais

    def executar(self, amb: "AmbienteExecucaoImperativa2") -> "AmbienteExecucaoImperativa2":
        ambiente = amb
        procedimento = ambiente.getProcedimento(self._nome_procedimento)

        # o incrementa/restaura aqui criam as variaveis usadas pela execucao do procedimento
        ambiente.incrementa()
        parametros_formais = procedimento.getParametrosFormais()
        aux = self._bindParameters(ambiente, parametros_formais)
        aux = procedimento.getComando().executar(aux)
        aux.restaura()
        return aux

    def _bindParameters(self, ambiente: "AmbienteExecucaoImperativa2", parametros_formais):
        """Insere no contexto a associacao entre cada parametro formal e seu parametro real correspondente."""
        lista_valor = self._parametros_reais.avaliar(ambiente)
        while lista_valor.length() > 0:
            ambiente.map(parametros_formais.getHead().getId(), lista_valor.getHead())
            parametros_formais = parametros_formais.getTail()
            lista_valor = lista_valor.getTail()
        return ambiente

    def checaTipo(self, amb: "AmbienteCompilacaoImperativa") -> bool:
        """Os tipos dos parametros formais devem ser iguais aos dos parametros reais, na ordem em que se apresentam."""
        tipo_procedimento = amb.get(self._nome_procedimento)
        tipo_parametros_reais = TipoProcedimento(self._parametros_reais.getTipos(amb))
        return tipo_procedimento.eIgual(tipo_parametros_reais)
