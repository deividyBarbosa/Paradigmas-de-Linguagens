from le1.plp.expressions1.expression.ValorConcreto import ValorConcreto
from le1.plp.expressions1.util.Tipo import Tipo


class ValorBooleano(ValorConcreto[bool]):
    """Este valor primitivo encapsula um valor booleano."""

    def __init__(self, valor: bool):
        super().__init__(valor)

    def getTipo(self) -> Tipo:
        return Tipo.TIPO_BOOLEANO

    def __str__(self):
        # Java imprime Boolean como "true"/"false" (minusculo)
        return "true" if self.valor() else "false"
