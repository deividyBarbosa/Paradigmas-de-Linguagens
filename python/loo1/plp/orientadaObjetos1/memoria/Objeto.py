from loo1.plp.expressions2.expression.Id import Id
from loo1.plp.orientadaObjetos1.excecao.declaracao.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id as IdLeft
from loo1.plp.orientadaObjetos1.expressao.valor.Valor import Valor
from loo1.plp.orientadaObjetos1.expressao.valor.ValorRef import ValorRef
from loo1.plp.orientadaObjetos1.memoria.ContextoObjeto import ContextoObjeto


class Objeto:
    """Conjunto formado pelo nome da classe de um objeto e o seu estado (atributos)."""

    def __init__(self, classe_objeto: Id, estado_obj: ContextoObjeto):
        self._classe_objeto = classe_objeto
        self._estado = estado_obj

    def getClasse(self) -> Id:
        return self._classe_objeto

    def getEstado(self) -> ContextoObjeto:
        return self._estado

    def setEstado(self, novo_estado: ContextoObjeto) -> None:
        self._estado = novo_estado

    def mapThis(self, vr: ValorRef) -> None:
        """Insere e mapeia o atributo 'this' do objeto."""
        id_ = IdLeft("this")
        self.getEstado().remove(id_)
        self.getEstado().put(id_, vr)

    def changeAtributo(self, id_variavel: Id, valor: Valor) -> None:
        if self.getEstado().containsKey(id_variavel):
            self.getEstado().remove(id_variavel)
            self.getEstado().put(id_variavel, valor)
        else:
            raise VariavelNaoDeclaradaException(id_variavel)
