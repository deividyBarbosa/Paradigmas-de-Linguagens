from loo1.plp.orientadaObjetos1.declaracao.variavel.DecVariavel import DecVariavel
from loo1.plp.orientadaObjetos1.excecao.declaracao.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
from loo1.plp.orientadaObjetos1.util.Tipo import Tipo


class CompostaDecVariavel(DecVariavel):
    """Declaracao de variavel composta (mais de uma variavel)."""

    def __init__(self, declaracao1: DecVariavel, declaracao2: DecVariavel):
        self._declaracao1 = declaracao1
        self._declaracao2 = declaracao2

    def getTipo(self, id_: Id) -> Tipo:
        try:
            return self._declaracao1.getTipo(id_)
        except VariavelNaoDeclaradaException:
            return self._declaracao2.getTipo(id_)

    def elabora(self, ambiente: "AmbienteExecucaoOO1") -> "AmbienteExecucaoOO1":
        return self._declaracao2.elabora(self._declaracao1.elabora(ambiente))

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        return self._declaracao1.checaTipo(ambiente) and self._declaracao2.checaTipo(ambiente)
