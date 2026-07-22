class ClasseNaoDeclaradaException(Exception):
    """Levantada quando uma classe referenciada nao foi declarada anteriormente."""

    def __init__(self, id):
        super().__init__(f"Classe {id} nao declarada.")
