from loo1.plp.orientadaObjetos1.expressao.valor.ValorConcreto import ValorConcreto
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo


class ValorInteiro(ValorConcreto):
    """Objetos desta classe encapsulam valor inteiro."""

    def __init__(self, valor: int):
        self._valor = valor

    def valor(self) -> int:
        return self._valor

    def avaliar(self, amb: "AmbienteExecucaoOO1") -> "ValorInteiro":
        return self

    def equalsValor(self, obj: ValorConcreto) -> bool:
        return isinstance(obj, ValorInteiro) and self._valor == obj.valor()

    def __str__(self) -> str:
        return str(self._valor)

    def checaTipo(self, amb: "AmbienteCompilacaoOO1") -> bool:
        return True

    def getTipo(self, amb: "AmbienteCompilacaoOO1"):
        return TipoPrimitivo.TIPO_INTEIRO
