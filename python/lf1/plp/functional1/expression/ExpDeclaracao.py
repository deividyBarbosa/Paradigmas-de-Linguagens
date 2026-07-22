from typing import Dict, List

from lf1.plp.expressions1.util.Tipo import Tipo
from lf1.plp.expressions2.expression.Expressao import Expressao
from lf1.plp.expressions2.expression.Id import Id
from lf1.plp.expressions2.expression.Valor import Valor
from lf1.plp.expressions2.memory.VariavelJaDeclaradaException import VariavelJaDeclaradaException
from lf1.plp.functional1.declaration.DeclaracaoFuncional import DeclaracaoFuncional
from lf1.plp.functional1.util.ValorFuncao import ValorFuncao


class ExpDeclaracao(Expressao):
    """Expressao 'let' que declara variaveis e/ou funcoes locais para uma expressao."""

    def __init__(self, declaracoes_funcionais: List[DeclaracaoFuncional], expressao_arg: Expressao):
        self._seqdec_funcional = declaracoes_funcionais
        self._expressao = expressao_arg

    def __str__(self):
        return f"let {self._seqdec_funcional}\nin\n{self._expressao}"

    def avaliar(self, ambiente: "AmbienteExecucaoFuncional") -> Valor:
        ambiente.incrementa()

        # Declaracoes feitas neste nivel nao devem ter influencia mutua: os
        # valores sao resolvidos numa tabela auxiliar antes de serem mapeados.
        aux_id_valor: Dict[Id, Valor] = {}
        aux_id_valor_funcao: Dict[Id, ValorFuncao] = {}

        self._resolveBindings(ambiente, aux_id_valor, aux_id_valor_funcao)
        self._includeBindings(ambiente, aux_id_valor, aux_id_valor_funcao)

        vresult = self._expressao.avaliar(ambiente)
        ambiente.restaura()
        return vresult

    def _includeBindings(self, ambiente, aux_id_valor: Dict[Id, Valor], aux_id_valor_funcao: Dict[Id, ValorFuncao]) -> None:
        for id_, valor in aux_id_valor.items():
            ambiente.map(id_, valor)
        for id_, valor_funcao in aux_id_valor_funcao.items():
            ambiente.mapFuncao(id_, valor_funcao)

    def _resolveBindings(self, ambiente, aux_id_valor: Dict[Id, Valor], aux_id_valor_funcao: Dict[Id, ValorFuncao]) -> None:
        for dec_funcional in self._seqdec_funcional:
            if dec_funcional.getAridade() == 0:
                aux_id_valor[dec_funcional.getID()] = dec_funcional.getExpressao().avaliar(ambiente)
            else:
                aux_id_valor_funcao[dec_funcional.getID()] = dec_funcional.getFuncao()

    def checaTipo(self, ambiente: "AmbienteCompilacao") -> bool:
        ambiente.incrementa()
        result = False
        try:
            result = self._checkTypeBindings(ambiente)
            if result:
                resolved_types = self._resolveTypeBindings(ambiente)
                self._includeTypeBindings(ambiente, resolved_types)
                result = self._expressao.checaTipo(ambiente)
        finally:
            ambiente.restaura()
        return result

    def _resolveTypeBindings(self, ambiente) -> Dict[Id, Tipo]:
        resolved_types: Dict[Id, Tipo] = {}
        for dec_funcional in self._seqdec_funcional:
            id_ = dec_funcional.getID()
            if id_ in resolved_types:
                raise VariavelJaDeclaradaException(id_)
            resolved_types[id_] = dec_funcional.getTipo(ambiente)
        return resolved_types

    def _checkTypeBindings(self, ambiente) -> bool:
        result = True
        for dec_funcional in self._seqdec_funcional:
            if not dec_funcional.checaTipo(ambiente):
                ambiente.restaura()
                result = False
        return result

    def _includeTypeBindings(self, ambiente, resolved_types: Dict[Id, Tipo]) -> None:
        for id_, tipo in resolved_types.items():
            ambiente.map(id_, tipo)

    def getTipo(self, ambiente: "AmbienteCompilacao") -> Tipo:
        ambiente.incrementa()
        for dec_funcional in self._seqdec_funcional:
            if dec_funcional.getAridade() == 0:
                ambiente.map(dec_funcional.getID(), dec_funcional.getExpressao().getTipo(ambiente))
            else:
                tipo = dec_funcional.getFuncao().getTipo(ambiente)
                if tipo is not Tipo.TIPO_INDEFINIDO:
                    ambiente.map(dec_funcional.getID(), tipo)
        vresult = self._expressao.getTipo(ambiente)
        ambiente.restaura()
        return vresult

    def getSeqdecFuncional(self) -> List[DeclaracaoFuncional]:
        return self._seqdec_funcional

    def getExpressao(self) -> Expressao:
        return self._expressao
