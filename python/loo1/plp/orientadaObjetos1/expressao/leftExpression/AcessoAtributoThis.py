from loo1.plp.orientadaObjetos1.excecao.declaracao.ClasseNaoDeclaradaException import ClasseNaoDeclaradaException
from loo1.plp.orientadaObjetos1.excecao.declaracao.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao
from loo1.plp.orientadaObjetos1.expressao.leftExpression.AcessoAtributo import AcessoAtributo
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id


class AcessoAtributoThis(AcessoAtributo):
    """Representa um acesso de atributo a partir do objeto this (this.attr)."""

    def __init__(self, var_this: "This", id_: Id):
        super().__init__(id_)
        self._var_this = var_this

    def avaliar(self, ambiente: "AmbienteExecucaoOO1") -> "Valor":
        return self._obterValorDeIdNoAmbiente(ambiente)

    def getExpressaoObjeto(self) -> Expressao:
        return self._var_this

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        resposta = False
        try:
            resposta = self._var_this.checaTipo(ambiente)
            if resposta:
                tipo = self._var_this.getTipo(ambiente)
                def_classe = ambiente.getDefClasse(tipo.getTipo())
                def_classe.getTipoAtributo(self.getId())
                resposta = True
        except (VariavelNaoDeclaradaException, ClasseNaoDeclaradaException):
            resposta = False
        return resposta

    def getTipo(self, ambiente: "AmbienteCompilacaoOO1"):
        def_classe = ambiente.getDefClasse(self._var_this.getTipo(ambiente).getTipo())
        return def_classe.getTipoAtributo(self.getId())

    def _obterValorDeIdNoAmbiente(self, ambiente: "AmbienteExecucaoOO1") -> "Valor":
        referencia = self._var_this.avaliar(ambiente)
        objeto = ambiente.getObjeto(referencia)
        aux = objeto.getEstado()
        return aux.get(self.getId())
