from typing import Dict, List, Optional

from lf1.plp.expressions2.expression.Id import Id
from lf1.plp.expressions2.expression.Valor import Valor
from lf1.plp.expressions2.memory.Contexto import Contexto
from lf1.plp.expressions2.memory.ContextoExecucao import ContextoExecucao
from lf1.plp.functional1.memory.AmbienteExecucaoFuncional import AmbienteExecucaoFuncional
from lf1.plp.functional1.util.ValorFuncao import ValorFuncao


class ContextoExecucaoFuncional(AmbienteExecucaoFuncional):
    """
    Combina uma pilha de valores (ContextoExecucao) com uma pilha de funcoes.

    A pilha de funcoes do Contexto[ValorFuncao] e a MESMA lista (por
    referencia) que pilha_funcao: empilhar/desempilhar uma reflete na outra,
    tal como no Java original, onde setPilha() apontava a mesma Stack para
    os dois objetos.
    """

    def __init__(self, pilha_funcao: Optional[List[Dict[Id, ValorFuncao]]] = None,
                 pilha_id_valor: Optional[ContextoExecucao] = None,
                 pilha_id_valor_func: Optional[Contexto] = None):
        if pilha_funcao is None and pilha_id_valor is None and pilha_id_valor_func is None:
            self._pilha_funcao: List[Dict[Id, ValorFuncao]] = []
            self._pilha_id_valor = ContextoExecucao()
            self._pilha_id_valor_func: Contexto = Contexto()
            self._pilha_id_valor_func.setPilha(self._pilha_funcao)
        else:
            self._pilha_funcao = pilha_funcao
            self._pilha_id_valor = pilha_id_valor
            self._pilha_id_valor_func = pilha_id_valor_func

    def incrementa(self) -> None:
        self._pilha_id_valor.incrementa()
        self._pilha_funcao.append({})

    def restaura(self) -> None:
        self._pilha_id_valor.restaura()
        self._pilha_funcao.pop()

    def mapFuncao(self, id_arg: Id, funcao: ValorFuncao) -> None:
        self._pilha_id_valor_func.map(id_arg, funcao)

    def getFuncao(self, id_arg: Id) -> ValorFuncao:
        return self._pilha_id_valor_func.get(id_arg)

    def get(self, id_arg: Id) -> Valor:
        return self._pilha_id_valor.get(id_arg)

    def map(self, id_arg: Id, tipo_id: Valor) -> None:
        self._pilha_id_valor.map(id_arg, tipo_id)

    def getPilhaFuncao(self) -> List[Dict[Id, ValorFuncao]]:
        return self._pilha_funcao

    def getPilhaIdValor(self) -> ContextoExecucao:
        return self._pilha_id_valor

    def getPilhaIdValorFunc(self) -> Contexto:
        return self._pilha_id_valor_func

    def setPilhaFuncao(self, pilha_funcao: List[Dict[Id, ValorFuncao]]) -> None:
        self._pilha_funcao = pilha_funcao

    def setPilhaIdValor(self, pilha_id_valor: ContextoExecucao) -> None:
        self._pilha_id_valor = pilha_id_valor

    def setPilhaIdValorFunc(self, pilha_id_valor_func: Contexto) -> None:
        self._pilha_id_valor_func = pilha_id_valor_func
