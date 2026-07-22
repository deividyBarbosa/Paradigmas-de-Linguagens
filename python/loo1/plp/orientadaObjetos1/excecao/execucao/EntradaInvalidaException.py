class EntradaInvalidaException(Exception):
    """Levantada quando uma entrada fornecida durante a execucao e invalida."""

    def __init__(self, mensagem: str = "A entrada fornecida nao pode ser atribuida a um identificador desse tipo!"):
        super().__init__(mensagem)
