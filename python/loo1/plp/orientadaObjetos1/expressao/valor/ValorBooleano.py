from loo1.plp.orientadaObjetos1.expressao.valor.ValorConcreto import ValorConcreto
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo


class ValorBooleano(ValorConcreto):
    """Este valor primitivo encapsula um valor booleano."""

    def __init__(self, valor: bool):
        self._valor = valor

    def avaliar(self, amb: "AmbienteExecucaoOO1") -> "ValorBooleano":
        return self

    def valor(self) -> bool:
        return self._valor

    def equalsValor(self, obj: ValorConcreto) -> bool:
        return isinstance(obj, ValorBooleano) and self._valor == obj.valor()

    def __str__(self) -> str:
        return "true" if self._valor else "false"

    def checaTipo(self, amb: "AmbienteCompilacaoOO1") -> bool:
        return True

    def getTipo(self, amb: "AmbienteCompilacaoOO1"):
        return TipoPrimitivo.TIPO_BOOLEANO
