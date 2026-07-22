class ProcedimentoNaoDeclaradoException(Exception):
    """Levantada quando um procedimento referenciado nao foi declarado."""

    def __init__(self, id):
        super().__init__(f"Procedimento {id} nao declarado.")
