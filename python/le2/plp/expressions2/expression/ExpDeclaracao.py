from typing import Dict, List

from le2.plp.expressions1.util.Tipo import Tipo
from le2.plp.expressions2.declaration.DecVariavel import DecVariavel
from le2.plp.expressions2.expression.Expressao import Expressao
from le2.plp.expressions2.expression.Id import Id
from le2.plp.expressions2.expression.Valor import Valor
from le2.plp.expressions2.memory.VariavelJaDeclaradaException import VariavelJaDeclaradaException


class ExpDeclaracao(Expressao):
    """Expressao 'let': declara variaveis num novo bloco e avalia uma expressao nesse escopo."""

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

    def _includeValueBindings(self, ambiente: "AmbienteExecucao", resolved_values: Dict[Id, Valor]) -> None:
        for id_ in resolved_values:
            ambiente.map(id_, resolved_values[id_])

    def _resolveValueBindings(self, ambiente: "AmbienteExecucao") -> Dict[Id, Valor]:
        resolved_values: Dict[Id, Valor] = {}
        for declaracao in self._seqdec_variavel:
            resolved_values[declaracao.getID()] = declaracao.getExpressao().avaliar(ambiente)
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

    def _includeTypeBindings(self, ambiente: "AmbienteCompilacao", resolved_types: Dict[Id, Tipo]) -> None:
        for id_ in resolved_types:
            ambiente.map(id_, resolved_types[id_])

    def _resolveTypeBindings(self, ambiente: "AmbienteCompilacao") -> Dict[Id, Tipo]:
        resolved_types: Dict[Id, Tipo] = {}
        for declaracao in self._seqdec_variavel:
            id_ = declaracao.getID()
            if id_ in resolved_types:
                raise VariavelJaDeclaradaException(id_)
            resolved_types[id_] = declaracao.getExpressao().getTipo(ambiente)
        return resolved_types

    def _checkTypeBindings(self, ambiente: "AmbienteCompilacao") -> bool:
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
