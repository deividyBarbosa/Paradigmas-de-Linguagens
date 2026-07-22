from typing import Dict, List

from lf1.plp.expressions1.util.Tipo import Tipo
from lf1.plp.expressions2.expression.Expressao import Expressao
from lf1.plp.expressions2.expression.Id import Id
from lf1.plp.expressions2.expression.Valor import Valor


class Aplicacao(Expressao):
    """Representa a aplicacao de uma funcao a uma lista de expressoes-argumento."""

    def __init__(self, f: Id, expressoes: List[Expressao]):
        self._func = f
        self._args_expressao = expressoes

    def __str__(self):
        return f"{self._func} ({self._args_expressao})"

    def avaliar(self, ambiente: "AmbienteExecucaoFuncional") -> Valor:
        funcao = ambiente.getFuncao(self._func)

        map_id_valor = self._resolveParametersBindings(ambiente, funcao)

        ambiente.incrementa()
        self._includeValueBindings(ambiente, map_id_valor)

        vresult = funcao.getExp().avaliar(ambiente)
        ambiente.restaura()
        return vresult

    def _includeValueBindings(self, ambiente, map_id_valor: Dict[Id, Valor]) -> None:
        for id_, valor in map_id_valor.items():
            ambiente.map(id_, valor)

    def _resolveParametersBindings(self, ambiente, funcao) -> Dict[Id, Valor]:
        parametros_id = funcao.getListaId()
        iter_expressoes = iter(self._args_expressao)

        map_id_valor: Dict[Id, Valor] = {}
        for id_ in parametros_id:
            exp = next(iter_expressoes)
            map_id_valor[id_] = exp.avaliar(ambiente)
        return map_id_valor

    def checaTipo(self, ambiente: "AmbienteCompilacao") -> bool:
        tipo_funcao = ambiente.get(self._func)
        return self._checkArgumentListSize(tipo_funcao) and self._checkArgumentTypes(ambiente, tipo_funcao)

    def _checkArgumentTypes(self, ambiente, tipo_funcao: Tipo) -> bool:
        result = True
        for valor_real in self._args_expressao:
            if not valor_real.checaTipo(ambiente):
                result = False
            tipo_arg = valor_real.getTipo(ambiente)
            if tipo_arg.intersecao(tipo_funcao).eVoid():
                result = False
            tipo_funcao = tipo_funcao.getProx()
        return result

    def _checkArgumentListSize(self, tipo_funcao: Tipo) -> bool:
        tamanho_tipo = 0
        aux = tipo_funcao
        while aux is not None:
            tamanho_tipo += 1
            aux = aux.getProx()
        return (tamanho_tipo - 1) == len(self._args_expressao)

    def getTipo(self, ambiente: "AmbienteCompilacao") -> Tipo:
        t = ambiente.get(self._func)
        while t.getProx() is not None:
            t = t.getProx()
        return t

    def getFunc(self) -> Id:
        return self._func

    def getArgsExpressao(self) -> List[Expressao]:
        return self._args_expressao
