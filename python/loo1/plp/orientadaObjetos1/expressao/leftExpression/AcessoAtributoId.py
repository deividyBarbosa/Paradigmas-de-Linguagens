from loo1.plp.orientadaObjetos1.excecao.declaracao.ClasseNaoDeclaradaException import ClasseNaoDeclaradaException
from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao
from loo1.plp.orientadaObjetos1.expressao.leftExpression.AcessoAtributo import AcessoAtributo
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
from loo1.plp.orientadaObjetos1.expressao.leftExpression.LeftExpression import LeftExpression
from loo1.plp.orientadaObjetos1.excecao.declaracao.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException


class AcessoAtributoId(AcessoAtributo):
    """Representa um acesso de atributo a partir de uma expressao (obj.attr)."""

    def __init__(self, av: LeftExpression, id_: Id):
        super().__init__(id_)
        self._av = av

    def avaliar(self, ambiente: "AmbienteExecucaoOO1") -> "Valor":
        return self._obterValorDeIdNoAmbiente(ambiente)

    def getExpressaoObjeto(self) -> Expressao:
        return self._av

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        resposta = False
        if self._av.checaTipo(ambiente):
            try:
                t = self._av.getTipo(ambiente)
                def_classe = ambiente.getDefClasse(t.getTipo())
                def_classe.getTipoAtributo(self.getId())
                resposta = True
            except (VariavelNaoDeclaradaException, ClasseNaoDeclaradaException):
                resposta = False
        return resposta

    def getTipo(self, ambiente: "AmbienteCompilacaoOO1"):
        # av.getTipo deve retornar uma TipoClasse; TipoClasse.getTipo() retorna
        # o Id (nome da classe) associado, usado para buscar a definicao da classe.
        nome_classe = self._av.getTipo(ambiente).getTipo()
        def_classe = ambiente.getDefClasse(nome_classe)
        return def_classe.getTipoAtributo(self.getId())

    def getAv(self) -> LeftExpression:
        return self._av

    def _obterValorDeIdNoAmbiente(self, ambiente: "AmbienteExecucaoOO1") -> "Valor":
        referencia = self._av.avaliar(ambiente)
        objeto = ambiente.getObjeto(referencia)
        aux = objeto.getEstado()
        return aux.get(self.getId())
