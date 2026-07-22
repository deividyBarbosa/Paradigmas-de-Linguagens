from li2.plp.expressions2.memory.IdentificadorJaDeclaradoException import IdentificadorJaDeclaradoException


class ProcedimentoJaDeclaradoException(IdentificadorJaDeclaradoException):
    def __init__(self, id):
        super().__init__(f"Procedimento {id} ja declarado.")
