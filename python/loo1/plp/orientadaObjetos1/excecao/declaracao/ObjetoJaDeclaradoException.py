class ObjetoJaDeclaradoException(Exception):
    """Levantada quando o objeto que esta sendo declarado ja o foi anteriormente."""

    def __init__(self, id):
        super().__init__(f"Objeto{id} ja declarado.")
