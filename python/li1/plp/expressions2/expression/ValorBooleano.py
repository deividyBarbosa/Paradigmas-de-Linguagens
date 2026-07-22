from li1.plp.expressions1.util.Tipo import Tipo
from li1.plp.expressions1.util.TipoPrimitivo import TipoPrimitivo
from li1.plp.expressions2.expression.ValorConcreto import ValorConcreto


class ValorBooleano(ValorConcreto[bool]):
    """Este valor primitivo encapsula um valor booleano."""

    def __init__(self, valor: bool):
        super().__init__(valor)

    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        return TipoPrimitivo.BOOLEANO

    def clone(self) -> "ValorBooleano":
        return ValorBooleano(self.valor())

    def __str__(self):
        # Java imprime Boolean.toString() como "true"/"false" (minusculo)
        return "true" if self.valor() else "false"
