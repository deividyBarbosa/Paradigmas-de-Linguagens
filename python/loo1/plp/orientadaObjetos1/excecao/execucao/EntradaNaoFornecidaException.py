class EntradaNaoFornecidaException(Exception):
    """Levantada quando uma entrada esperada nao e fornecida."""

    def __init__(self):
        super().__init__("Forneca os valores de entrada do programa!")
