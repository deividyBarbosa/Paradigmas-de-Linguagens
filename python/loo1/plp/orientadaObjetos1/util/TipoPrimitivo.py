from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
from loo1.plp.orientadaObjetos1.util.Tipo import Tipo


class TipoPrimitivo(Tipo):
    """Classe que representa os possiveis tipos primitivos de uma expressao."""

    INTEIRO = 1
    BOOLEANO = 2
    STRING = 4

    TIPO_ID_int = Id("int")
    TIPO_ID_string = Id("string")
    TIPO_ID_boolean = Id("boolean")

    def __init__(self, tipo: int):
        self._tipo = tipo

    def getTipo(self) -> Id:
        if self._tipo == TipoPrimitivo.INTEIRO:
            return TipoPrimitivo.TIPO_ID_int
        if self._tipo == TipoPrimitivo.BOOLEANO:
            return TipoPrimitivo.TIPO_ID_boolean
        if self._tipo == TipoPrimitivo.STRING:
            return TipoPrimitivo.TIPO_ID_string
        return Id("undefined")

    def eInteiro(self) -> bool:
        return self._tipo == TipoPrimitivo.INTEIRO

    def eBooleano(self) -> bool:
        return self._tipo == TipoPrimitivo.BOOLEANO

    def eString(self) -> bool:
        return self._tipo == TipoPrimitivo.STRING

    def eValido(self, ambiente: "AmbienteCompilacaoOO1" = None) -> bool:
        """
        Metodo implementado para unificar TipoPrimitivo e TipoClasse sob uma
        unica interface (Tipo); nao depende de 'ambiente' (aceito e ignorado
        para compatibilidade com a assinatura comum).
        """
        return self._tipo in (TipoPrimitivo.STRING, TipoPrimitivo.BOOLEANO, TipoPrimitivo.INTEIRO)

    def __eq__(self, obj) -> bool:
        return isinstance(obj, TipoPrimitivo) and obj._tipo == self._tipo

    def __hash__(self):
        return hash(self._tipo)

    def __str__(self) -> str:
        if self._tipo == TipoPrimitivo.INTEIRO:
            return "int"
        if self._tipo == TipoPrimitivo.BOOLEANO:
            return "boolean"
        if self._tipo == TipoPrimitivo.STRING:
            return "string"
        return "undefined"


TipoPrimitivo.TIPO_INTEIRO = TipoPrimitivo(TipoPrimitivo.INTEIRO)
TipoPrimitivo.TIPO_BOOLEANO = TipoPrimitivo(TipoPrimitivo.BOOLEANO)
TipoPrimitivo.TIPO_STRING = TipoPrimitivo(TipoPrimitivo.STRING)
