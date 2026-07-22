from typing import Dict

from lf1.plp.expressions1.util.Tipo import Tipo
from lf1.plp.expressions2.memory.VariavelJaDeclaradaException import VariavelJaDeclaradaException
from lf1.plp.expressions2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException


class RestrictTypesVisitor:
    """
    Visitor que percorre uma expressao e restringe (por unificacao simples) os
    tipos possiveis dos identificadores livres nela, dado um tipo esperado.

    O despacho para '_visit<NomeDaClasse>' e feito dinamicamente a partir do
    nome da classe da expressao (type(exp).__name__), espelhando o uso de
    reflection (Class.getMethod) do codigo Java original.
    """

    @staticmethod
    def visit(exp, ambiente, tipos: Dict, tipo_esperado: Tipo) -> Dict:
        method_name = "_visit" + type(exp).__name__
        metodo = getattr(RestrictTypesVisitor, method_name, None)
        if metodo is None:
            raise NotImplementedError(f"O metodo visit chamado ({method_name}) nao foi implementado")
        return metodo(exp, ambiente, tipos, tipo_esperado)

    @staticmethod
    def _visitAplicacao(aplicacao, ambiente, tipos: Dict, tipo_esperado: Tipo) -> Dict:
        try:
            t = ambiente.get(aplicacao.getFunc())
            map_id_tipo = tipos
            for exp in aplicacao.getArgsExpressao():
                t_arg = Tipo(t.get())  # pega o tipo apenas do argumento.
                map_id_tipo = RestrictTypesVisitor.visit(exp, ambiente, map_id_tipo, t_arg)
                t = t.getProx()
            return map_id_tipo
        except VariavelNaoDeclaradaException:
            # se a funcao nao estiver declarada, tenta restringir apenas as expressoes.
            map_id_tipo = tipos
            tudo = Tipo()
            for exp in aplicacao.getArgsExpressao():
                map_id_tipo = RestrictTypesVisitor.visit(exp, ambiente, map_id_tipo, tudo)
            return map_id_tipo

    @staticmethod
    def _visitExpAnd(expressao, ambiente, map_id_tipo: Dict, tipo_esperado: Tipo) -> Dict:
        aux = RestrictTypesVisitor.visit(expressao.getEsq(), ambiente, map_id_tipo, Tipo.TIPO_BOOLEANO)
        aux = RestrictTypesVisitor.visit(expressao.getDir(), ambiente, aux, Tipo.TIPO_BOOLEANO)
        return aux

    @staticmethod
    def _visitExpConcat(expressao, ambiente, map_id_tipo: Dict, tipo_esperado: Tipo) -> Dict:
        aux = RestrictTypesVisitor.visit(expressao.getEsq(), ambiente, map_id_tipo, Tipo.TIPO_STRING)
        aux = RestrictTypesVisitor.visit(expressao.getDir(), ambiente, aux, Tipo.TIPO_STRING)
        return aux

    @staticmethod
    def _visitExpDeclaracao(expressao, ambiente, tipos: Dict, tipo_esperado: Tipo) -> Dict:
        ambiente.incrementa()
        mapa = tipos
        for dec_funcional in expressao.getSeqdecFuncional():
            tipo_procurado = None
            try:
                if dec_funcional.getAridade() == 0:
                    tipo_procurado = dec_funcional.getExpressao().getTipo(ambiente)
                    ambiente.map(dec_funcional.getID(), tipo_procurado)
                else:
                    tipo = dec_funcional.getFuncao().getTipo(ambiente)
                    tipo_procurado = tipo
                    if tipo is not Tipo.TIPO_INDEFINIDO:
                        ambiente.map(dec_funcional.getID(), tipo)
            except (VariavelJaDeclaradaException, VariavelNaoDeclaradaException):
                pass  # nao deve ocorrer

            mapa = RestrictTypesVisitor.visit(dec_funcional.getExpressao(), ambiente, mapa, tipo_procurado)
        mapa = RestrictTypesVisitor.visit(expressao.getExpressao(), ambiente, mapa, tipo_esperado)
        ambiente.restaura()
        return mapa

    @staticmethod
    def _visitExpEquals(expressao, ambiente, tipos: Dict, tipo_esperado: Tipo) -> Dict:
        return tipos

    @staticmethod
    def _visitExpLength(expressao, ambiente, tipos: Dict, tipo_esperado: Tipo) -> Dict:
        return RestrictTypesVisitor.visit(expressao.getExp(), ambiente, tipos, Tipo.TIPO_STRING)

    @staticmethod
    def _visitExpMenos(expressao, ambiente, tipos: Dict, tipo_esperado: Tipo) -> Dict:
        return RestrictTypesVisitor.visit(expressao.getExp(), ambiente, tipos, Tipo.TIPO_INTEIRO)

    @staticmethod
    def _visitExpNot(expressao, ambiente, tipos: Dict, tipo_esperado: Tipo) -> Dict:
        return RestrictTypesVisitor.visit(expressao.getExp(), ambiente, tipos, Tipo.TIPO_BOOLEANO)

    @staticmethod
    def _visitExpOr(expressao, ambiente, tipos: Dict, tipo_esperado: Tipo) -> Dict:
        aux = RestrictTypesVisitor.visit(expressao.getEsq(), ambiente, tipos, Tipo.TIPO_BOOLEANO)
        aux = RestrictTypesVisitor.visit(expressao.getDir(), ambiente, aux, Tipo.TIPO_BOOLEANO)
        return aux

    @staticmethod
    def _visitExpSoma(expressao, ambiente, tipos: Dict, tipo_esperado: Tipo) -> Dict:
        aux = RestrictTypesVisitor.visit(expressao.getEsq(), ambiente, tipos, Tipo.TIPO_INTEIRO)
        aux = RestrictTypesVisitor.visit(expressao.getDir(), ambiente, aux, Tipo.TIPO_INTEIRO)
        return aux

    @staticmethod
    def _visitExpSub(expressao, ambiente, tipos: Dict, tipo_esperado: Tipo) -> Dict:
        aux = RestrictTypesVisitor.visit(expressao.getEsq(), ambiente, tipos, Tipo.TIPO_INTEIRO)
        aux = RestrictTypesVisitor.visit(expressao.getDir(), ambiente, aux, Tipo.TIPO_INTEIRO)
        return aux

    @staticmethod
    def _visitIfThenElse(expressao, ambiente, tipos: Dict, tipo_esperado: Tipo) -> Dict:
        aux = RestrictTypesVisitor.visit(expressao.getCondicao(), ambiente, tipos, Tipo.TIPO_BOOLEANO)
        aux = RestrictTypesVisitor.visit(expressao.getThen(), ambiente, aux, tipo_esperado)
        aux = RestrictTypesVisitor.visit(expressao.getElseExpressao(), ambiente, aux, tipo_esperado)
        return aux

    @staticmethod
    def _visitId(this_id, ambiente, tipos: Dict, tipo_esperado: Tipo) -> Dict:
        for id_, tipo_atual in list(tipos.items()):
            if id_ == this_id:
                tipos[id_] = tipo_esperado.intersecao(tipo_atual)
        return tipos

    @staticmethod
    def _visitValorInteiro(valor, ambiente, tipos: Dict, tipo_esperado: Tipo) -> Dict:
        return tipos

    @staticmethod
    def _visitValorString(valor, ambiente, tipos: Dict, tipo_esperado: Tipo) -> Dict:
        return tipos

    @staticmethod
    def _visitValorBooleano(valor, ambiente, tipos: Dict, tipo_esperado: Tipo) -> Dict:
        return tipos
