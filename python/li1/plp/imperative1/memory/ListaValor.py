from li1.plp.expressions2.expression.Valor import Valor
from li1.plp.imperative1.util.Lista import Lista


class ListaValor(Lista[Valor]):
    """Lista encadeada com os valores lidos/escritos pelo programa imperativo."""

    def __init__(self, valor: Valor = None, lista_valor: "ListaValor" = None):
        if valor is None and lista_valor is None:
            super().__init__()
        elif lista_valor is None:
            super().__init__(valor, ListaValor())
        else:
            super().__init__(valor, lista_valor)

    def write(self, valor: Valor) -> None:
        """Enfileira o valor no final da lista."""
        if self.getHead() is None:
            self.head = valor
            self.tail = ListaValor()
        else:
            self.getTail().write(valor)
