from loo1.plp.orientadaObjetos1.declaracao.classe.DecClasse import DecClasse
from loo1.plp.orientadaObjetos1.declaracao.procedimento.DecProcedimento import DecProcedimento
from loo1.plp.orientadaObjetos1.declaracao.variavel.DecVariavel import DecVariavel
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
from loo1.plp.orientadaObjetos1.memoria.DefClasse import DefClasse
from loo1.plp.orientadaObjetos1.util.TipoClasse import TipoClasse


class DecClasseSimples(DecClasse):
    """Representa a declaracao de uma unica classe."""

    def __init__(self, nome_classe: Id, atributos: DecVariavel, metodos: DecProcedimento):
        self._nome_classe = nome_classe
        self._atributos = atributos
        self._metodos = metodos

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        ambiente.mapDefClasse(self._nome_classe, DefClasse(self._nome_classe, self._atributos, self._metodos))
        resposta = False
        ambiente.incrementa()
        if self._atributos.checaTipo(ambiente):
            ambiente.map(Id("this"), TipoClasse(self._nome_classe))
            resposta = self._metodos.checaTipo(ambiente)
        ambiente.restaura()
        return resposta

    def elabora(self, ambiente: "AmbienteExecucaoOO1") -> "AmbienteExecucaoOO1":
        ambiente.mapDefClasse(self._nome_classe, DefClasse(self._nome_classe, self._atributos, self._metodos))
        return ambiente
