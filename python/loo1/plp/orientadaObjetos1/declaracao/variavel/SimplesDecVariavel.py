from loo1.plp.orientadaObjetos1.declaracao.variavel.DecVariavel import DecVariavel
from loo1.plp.orientadaObjetos1.excecao.declaracao.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
from loo1.plp.orientadaObjetos1.util.Tipo import Tipo
from loo1.plp.orientadaObjetos1.util.TipoClasse import TipoClasse


class SimplesDecVariavel(DecVariavel):
    """Representa uma declaracao de variavel simples."""

    def __init__(self, tipo: Tipo, id_: Id, expressao: Expressao):
        self._tipo = tipo
        self._id = id_
        self._expressao = expressao

    def getTipo(self, id_: Id) -> Tipo:
        if self._id == id_:
            return self._tipo
        raise VariavelNaoDeclaradaException(id_)

    def elabora(self, ambiente: "AmbienteExecucaoOO1") -> "AmbienteExecucaoOO1":
        ambiente.map(self._id, self._expressao.avaliar(ambiente))
        return ambiente

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        resposta = False
        if self._expressao.checaTipo(ambiente):
            if isinstance(self._tipo, TipoClasse):
                resposta = self._expressao.getTipo(ambiente) == TipoClasse.TIPO_NULL or self._expressao.getTipo(
                    ambiente
                ) == self._tipo
            else:
                resposta = self._expressao.getTipo(ambiente) == self._tipo
        if resposta:
            ambiente.map(self._id, self._tipo)
        return resposta
