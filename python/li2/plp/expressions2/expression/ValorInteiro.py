from li2.plp.expressions1.util.Tipo import Tipo
from li2.plp.expressions1.util.TipoPrimitivo import TipoPrimitivo
from li2.plp.expressions2.expression.ValorConcreto import ValorConcreto


class ValorInteiro(ValorConcreto[int]):
    """Objetos desta classe encapsulam valor inteiro."""

    def __init__(self, valor: int):
        super().__init__(valor)

    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        return TipoPrimitivo.INTEIRO

    def clone(self) -> "ValorInteiro":
        return ValorInteiro(self.valor())
