from le1.plp.expressions1.expression.ValorConcreto import ValorConcreto
from le1.plp.expressions1.util.Tipo import Tipo


class ValorInteiro(ValorConcreto[int]):
    """Objetos desta classe encapsulam valor inteiro."""

    def __init__(self, valor: int):
        super().__init__(valor)

    def getTipo(self) -> Tipo:
        return Tipo.TIPO_INTEIRO
