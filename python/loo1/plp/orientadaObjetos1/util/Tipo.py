class Tipo:
    """Interface representando um tipo (primitivo ou classe) na linguagem OO."""

    def getTipo(self) -> "Id":
        """Obtem o tipo, representado por um identificador."""
        raise NotImplementedError

    def __eq__(self, obj) -> bool:
        raise NotImplementedError

    def eValido(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        """Verifica se o tipo e valido no ambiente dado."""
        raise NotImplementedError
