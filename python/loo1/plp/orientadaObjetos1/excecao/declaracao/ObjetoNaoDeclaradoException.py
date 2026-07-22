class ObjetoNaoDeclaradoException(Exception):
    """Levantada quando o objeto referenciado nao foi declarado."""

    def __init__(self, id):
        super().__init__(f"Objeto{id} nao declarado.")
