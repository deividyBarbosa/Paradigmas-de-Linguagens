from le1.plp.expressions1.expression.ValorConcreto import ValorConcreto
from le1.plp.expressions1.util.Tipo import Tipo


class ValorString(ValorConcreto[str]):
    """Este valor primitivo encapsula uma String."""

    def __init__(self, valor: str):
        super().__init__(valor)

    def getTipo(self) -> Tipo:
        return Tipo.TIPO_STRING
