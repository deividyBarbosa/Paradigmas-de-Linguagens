from typing import Iterable


class ToStringProvider:
    """Utilitario para formatar listas como texto, ao estilo do StringBuilder original."""

    @staticmethod
    def listToString(lista: Iterable, before: str = "", after: str = "", separator: str = "") -> str:
        itens = [str(item) for item in lista]
        return before + (separator + " ").join(itens) + after
