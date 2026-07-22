class ListaTipo:
    """Lista encadeada contendo tipos."""

    def __init__(self, tipo=None, lista_tipo: "ListaTipo" = None):
        if tipo is None:
            self._tipo = None
            self._lista_tipo = None
        elif lista_tipo is None:
            self._tipo = tipo
            self._lista_tipo = ListaTipo()
        else:
            self._tipo = tipo
            self._lista_tipo = lista_tipo

    def length(self) -> int:
        if self._lista_tipo is None:
            return 0
        return 1 + self._lista_tipo.length()

    def head(self):
        return self._tipo

    def tail(self) -> "ListaTipo":
        return self._lista_tipo

    def __str__(self) -> str:
        partes = []
        self._getString(partes)
        return "".join(partes)

    def _getString(self, partes) -> None:
        if self._tipo is not None:
            if self._lista_tipo is not None:
                self._lista_tipo._getString(partes)
            partes.append(str(self._tipo) + " ")
