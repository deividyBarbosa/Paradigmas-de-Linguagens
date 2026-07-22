from typing import Dict, List

from loo1.plp.expressions1.util.Tipo import Tipo
from loo1.plp.expressions2.declaration.DecVariavel import DecVariavel
from loo1.plp.expressions2.expression.Expressao import Expressao
from loo1.plp.expressions2.expression.Id import Id
from loo1.plp.expressions2.expression.Valor import Valor
from loo1.plp.expressions2.memory.VariavelJaDeclaradaException import VariavelJaDeclaradaException


class ExpDeclaracao(Expressao):
    """Expressao 'let' que declara variaveis e avalia uma expressao nesse escopo."""

    def __init__(self, declarations: List[DecVariavel], expressao_arg: Expressao):
        self._seqdec_variavel = declarations
        self._expressao = expressao_arg

    def avaliar(self, ambiente: "AmbienteExecucao") -> Valor:
        ambiente.incrementa()
        resolved_values = self._resolveValueBindings(ambiente)
        self._includeValueBindings(ambiente, resolved_values)
        result = self._expressao.avaliar(ambiente)
        ambiente.restaura()
        return result

    def _includeValueBindings(self, ambiente, resolved_values: Dict[Id, Valor]) -> None:
        for id_, valor in resolved_values.items():
            ambiente.map(id_, valor)

    def _resolveValueBindings(self, ambiente) -> Dict[Id, Valor]:
        resolved_values: Dict[Id, Valor] = {}
        for declaracao in self._seqdec_variavel:
            resolved_values[declaracao.getId()] = declaracao.getExpressao().avaliar(ambiente)
        return resolved_values

    def checaTipo(self, ambiente: "AmbienteCompilacao") -> bool:
        ambiente.incrementa()
        try:
            if self._checkTypeBindings(ambiente):
                resolved_types = self._resolveTypeBindings(ambiente)
                self._includeTypeBindings(ambiente, resolved_types)
                result = self._expressao.checaTipo(ambiente)
            else:
                result = False
        finally:
            ambiente.restaura()
        return result

    def _includeTypeBindings(self, ambiente, resolved_types: Dict[Id, Tipo]) -> None:
        for id_, tipo in resolved_types.items():
            ambiente.map(id_, tipo)

    def _resolveTypeBindings(self, ambiente) -> Dict[Id, Tipo]:
        resolved_types: Dict[Id, Tipo] = {}
        for declaracao in self._seqdec_variavel:
            id_ = declaracao.getId()
            if id_ in resolved_types:
                raise VariavelJaDeclaradaException(id_)
            resolved_types[id_] = declaracao.getExpressao().getTipo(ambiente)
        return resolved_types

    def _checkTypeBindings(self, ambiente) -> bool:
        for declaracao in self._seqdec_variavel:
            if not declaracao.getExpressao().checaTipo(ambiente):
                return False
        return True

    def getTipo(self, ambiente: "AmbienteCompilacao") -> Tipo:
        ambiente.incrementa()
        resolved_types = self._resolveTypeBindings(ambiente)
        self._includeTypeBindings(ambiente, resolved_types)
        result = self._expressao.getTipo(ambiente)
        ambiente.restaura()
        return result

    def reduzir(self, ambiente: "AmbienteExecucao") -> "ExpDeclaracao":
        ambiente.incrementa()
        for dec in self._seqdec_variavel:
            ambiente.map(dec.getId(), None)
        self._expressao = self._expressao.reduzir(ambiente)
        ambiente.restaura()
        return self

    def clone(self) -> "ExpDeclaracao":
        nova_lista = [DecVariavel(dec.getId().clone(), dec.getExpressao().clone()) for dec in self._seqdec_variavel]
        return ExpDeclaracao(nova_lista, self._expressao.clone())
