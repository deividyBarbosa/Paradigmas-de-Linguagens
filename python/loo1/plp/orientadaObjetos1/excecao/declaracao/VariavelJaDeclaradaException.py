class VariavelJaDeclaradaException(Exception):
    """Levantada quando uma variavel esta sendo declarada mais de uma vez num mesmo escopo."""

    def __init__(self, id):
        super().__init__(f"Variavel {id} ja declarada.")
