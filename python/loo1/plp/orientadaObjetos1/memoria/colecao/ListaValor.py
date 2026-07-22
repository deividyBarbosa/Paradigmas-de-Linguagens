from loo1.plp.imperative1.util.Lista import Lista
from loo1.plp.orientadaObjetos1.expressao.valor.Valor import Valor


class ListaValor(Lista):
    """Lista encadeada com os valores lidos/escritos ou passados como parametros reais."""

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
