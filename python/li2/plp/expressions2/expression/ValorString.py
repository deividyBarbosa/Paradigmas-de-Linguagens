from li2.plp.expressions1.util.Tipo import Tipo
from li2.plp.expressions1.util.TipoPrimitivo import TipoPrimitivo
from li2.plp.expressions2.expression.ValorConcreto import ValorConcreto


class ValorString(ValorConcreto[str]):
    """Este valor primitivo encapsula uma String."""

    def __init__(self, valor: str):
        super().__init__(valor)

    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        return TipoPrimitivo.STRING

    def __str__(self):
        return f'"{super().__str__()}"'

    def clone(self) -> "ValorString":
        return ValorString(self.valor())
