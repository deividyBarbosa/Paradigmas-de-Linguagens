from le2.plp.expressions1.util.Tipo import Tipo
from le2.plp.expressions2.expression.ValorConcreto import ValorConcreto


class ValorBooleano(ValorConcreto[bool]):
    """Este valor primitivo encapsula um valor booleano."""

    def __init__(self, valor: bool):
        super().__init__(valor)

    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        return Tipo.TIPO_BOOLEANO

    def __str__(self):
        return "true" if self.valor() else "false"
