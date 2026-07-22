from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id


class This(Expressao):
    """Representa a expressao 'this'."""

    def avaliar(self, ambiente: "AmbienteExecucaoOO1") -> "Valor":
        return ambiente.get(Id("this"))

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        # Como sempre ha uma classe instanciada em orientacao a objetos,
        # o checaTipo() de this retorna sempre true.
        return True

    def getTipo(self, ambiente: "AmbienteCompilacaoOO1"):
        return ambiente.get(Id("this"))
