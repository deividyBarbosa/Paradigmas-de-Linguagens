from loo1.plp.expressions2.memory.IdentificadorJaDeclaradoException import IdentificadorJaDeclaradoException


class VariavelJaDeclaradaException(IdentificadorJaDeclaradoException):
    def __init__(self, id):
        super().__init__(f"Variavel {id} ja declarada.")
