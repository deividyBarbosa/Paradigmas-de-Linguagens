from loo1.plp.orientadaObjetos1.declaracao.variavel.DecVariavel import DecVariavel
from loo1.plp.orientadaObjetos1.declaracao.variavel.SimplesDecVariavel import SimplesDecVariavel
from loo1.plp.orientadaObjetos1.excecao.declaracao.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
from loo1.plp.orientadaObjetos1.expressao.valor.ValorNull import ValorNull
from loo1.plp.orientadaObjetos1.util.Tipo import Tipo
from loo1.plp.orientadaObjetos1.util.TipoClasse import TipoClasse


class DecVariavelObjeto(DecVariavel):
    """Representa a declaracao de uma variavel do tipo objeto."""

    def __init__(self, tipo: Tipo, objeto: Id, classe: Id):
        self._tipo = tipo
        self._objeto = objeto
        self._classe = classe

    def getTipo(self, id_: Id) -> Tipo:
        if self._objeto == id_:
            return self._tipo
        raise VariavelNaoDeclaradaException(id_)

    def elabora(self, ambiente: "AmbienteExecucaoOO1") -> "AmbienteExecucaoOO1":
        from loo1.plp.orientadaObjetos1.comando.New import New

        aux = SimplesDecVariavel(self._tipo, self._objeto, ValorNull()).elabora(ambiente)
        aux = New(self._objeto, self._classe).executar(aux)
        return aux

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        resposta = False
        tp_classe = TipoClasse(self._classe)
        if tp_classe.eValido(ambiente) and self._tipo.eValido(ambiente):
            resposta = tp_classe == self._tipo
            ambiente.map(self._objeto, tp_classe)
        return resposta

    def getTipoDeclarado(self) -> Tipo:
        return self._tipo

    def getObjeto(self) -> Id:
        return self._objeto

    def getClasse(self) -> Id:
        return self._classe
