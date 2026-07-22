from li2.plp.expressions2.expression.Id import Id
from li2.plp.imperative1.declaration.Declaracao import Declaracao
from li2.plp.imperative2.declaration.DefProcedimento import DefProcedimento


class DeclaracaoProcedimento(Declaracao):

    def __init__(self, id_: Id, def_procedimento: DefProcedimento):
        self._id = id_
        self._def_procedimento = def_procedimento

    def elabora(self, ambiente: "AmbienteExecucaoImperativa2") -> "AmbienteExecucaoImperativa2":
        ambiente.mapProcedimento(self._id, self._def_procedimento)
        return ambiente

    def checaTipo(self, ambiente: "AmbienteCompilacaoImperativa") -> bool:
        ambiente.map(self._id, self._def_procedimento.getTipo())

        parametros_formais = self._def_procedimento.getParametrosFormais()
        if parametros_formais.checaTipo(ambiente):
            ambiente.incrementa()
            ambiente = parametros_formais.elabora(ambiente)
            resposta = self._def_procedimento.getComando().checaTipo(ambiente)
            ambiente.restaura()
        else:
            resposta = False
        return resposta
