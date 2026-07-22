from loo1.plp.orientadaObjetos1.expressao.valor.ValorConcreto import ValorConcreto
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo


class ValorString(ValorConcreto):
    """Este valor primitivo encapsula uma String."""

    def __init__(self, valor: str):
        self._valor = valor

    def __str__(self) -> str:
        return self._valor

    def equalsValor(self, obj: ValorConcreto) -> bool:
        return isinstance(obj, ValorString) and self._valor == obj.valor()

    def avaliar(self, amb: "AmbienteExecucaoOO1") -> "ValorString":
        return self

    def valor(self) -> str:
        return self._valor

    def checaTipo(self, amb: "AmbienteCompilacaoOO1") -> bool:
        return True

    def getTipo(self, amb: "AmbienteCompilacaoOO1"):
        return TipoPrimitivo.TIPO_STRING
