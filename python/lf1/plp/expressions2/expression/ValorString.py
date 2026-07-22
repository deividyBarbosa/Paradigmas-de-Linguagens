from lf1.plp.expressions1.util.Tipo import Tipo
from lf1.plp.expressions2.expression.ValorConcreto import ValorConcreto


class ValorString(ValorConcreto[str]):
    """Este valor primitivo encapsula uma String."""

    def __init__(self, valor: str):
        super().__init__(valor)

    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        return Tipo.TIPO_STRING
