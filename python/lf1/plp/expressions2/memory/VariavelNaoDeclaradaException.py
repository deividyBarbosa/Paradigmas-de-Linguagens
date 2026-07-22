from lf1.plp.expressions2.memory.IdentificadorNaoDeclaradoException import IdentificadorNaoDeclaradoException


class VariavelNaoDeclaradaException(IdentificadorNaoDeclaradoException):
    def __init__(self, id):
        super().__init__(f"Variavel {id} nao declarada.")
