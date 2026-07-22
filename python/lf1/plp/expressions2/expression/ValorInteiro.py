from lf1.plp.expressions1.util.Tipo import Tipo
from lf1.plp.expressions2.expression.ValorConcreto import ValorConcreto


class ValorInteiro(ValorConcreto[int]):
    """Objetos desta classe encapsulam valor inteiro."""

    def __init__(self, valor: int):
        super().__init__(valor)

    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        return Tipo.TIPO_INTEIRO
