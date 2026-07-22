from typing import Dict, List

from loo1.plp.expressions2.expression.Id import Id
from loo1.plp.orientadaObjetos1.excecao.declaracao.ClasseJaDeclaradaException import ClasseJaDeclaradaException
from loo1.plp.orientadaObjetos1.excecao.declaracao.ClasseNaoDeclaradaException import ClasseNaoDeclaradaException
from loo1.plp.orientadaObjetos1.excecao.declaracao.ProcedimentoJaDeclaradoException import (
    ProcedimentoJaDeclaradoException,
)
from loo1.plp.orientadaObjetos1.excecao.declaracao.ProcedimentoNaoDeclaradoException import (
    ProcedimentoNaoDeclaradoException,
)
from loo1.plp.orientadaObjetos1.excecao.declaracao.VariavelJaDeclaradaException import VariavelJaDeclaradaException
from loo1.plp.orientadaObjetos1.excecao.declaracao.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from loo1.plp.orientadaObjetos1.memoria.AmbienteCompilacaoOO1 import AmbienteCompilacaoOO1
from loo1.plp.orientadaObjetos1.util.Tipo import Tipo


class ContextoCompilacaoOO1(AmbienteCompilacaoOO1):
    """Representa o contexto de compilacao da linguagem OO."""

    def __init__(self, entrada: "ListaValor"):
        self._pilha: List[Dict[Id, Tipo]] = []
        self._pilha_procedimento: List[Dict[Id, "ListaDeclaracaoParametro"]] = []
        self._map_def_classe: Dict[Id, "DefClasse"] = {}
        self._entrada = entrada

    def incrementa(self) -> None:
        self._pilha.append({})
        self._pilha_procedimento.append({})

    def restaura(self) -> None:
        self._pilha.pop()
        self._pilha_procedimento.pop()

    def map(self, id_arg: Id, tipo_id: Tipo) -> None:
        topo = self._pilha[-1]
        if id_arg in topo:
            raise VariavelJaDeclaradaException(id_arg)
        topo[id_arg] = tipo_id

    def mapParametrosProcedimento(self, id_arg: Id, parametros_id: "ListaDeclaracaoParametro") -> None:
        topo = self._pilha_procedimento[-1]
        if id_arg in topo:
            raise ProcedimentoJaDeclaradoException(id_arg)
        topo[id_arg] = parametros_id

    def mapDefClasse(self, id_arg: Id, def_classe: "DefClasse") -> None:
        if id_arg in self._map_def_classe:
            raise ClasseJaDeclaradaException(id_arg)
        self._map_def_classe[id_arg] = def_classe

    def get(self, id_arg: Id) -> Tipo:
        for bloco in reversed(self._pilha):
            if id_arg in bloco:
                return bloco[id_arg]
        raise VariavelNaoDeclaradaException(id_arg)

    def getParametrosProcedimento(self, id_arg: Id) -> "ListaDeclaracaoParametro":
        for bloco in reversed(self._pilha_procedimento):
            if id_arg in bloco:
                return bloco[id_arg]
        raise ProcedimentoNaoDeclaradoException(id_arg)

    def getDefClasse(self, id_arg: Id) -> "DefClasse":
        result = self._map_def_classe.get(id_arg)
        if result is None:
            raise ClasseNaoDeclaradaException(id_arg)
        return result

    def getTipoEntrada(self) -> Tipo:
        aux = self._entrada.getHead().getTipo(self)
        self._entrada = self._entrada.getTail()
        return aux

    def getTipo(self, id_arg: Id) -> Tipo:
        return self.get(id_arg)
