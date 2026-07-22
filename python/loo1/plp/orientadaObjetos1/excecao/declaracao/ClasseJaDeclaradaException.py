class ClasseJaDeclaradaException(Exception):
    """Levantada quando a classe que esta sendo declarada ja o foi anteriormente."""

    def __init__(self, id):
        super().__init__(f"Classe {id} ja declarada.")
