class ProcedimentoJaDeclaradoException(Exception):
    """Levantada quando um procedimento esta sendo declarado novamente."""

    def __init__(self, id):
        super().__init__(f"Procedimento {id} ja declarado.")
