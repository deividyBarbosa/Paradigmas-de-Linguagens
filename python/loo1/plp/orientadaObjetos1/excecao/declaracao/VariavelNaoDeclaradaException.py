class VariavelNaoDeclaradaException(Exception):
    """Levantada quando uma variavel referenciada nao foi declarada anteriormente."""

    def __init__(self, id):
        super().__init__(f"Variavel {id} nao declarada.")
