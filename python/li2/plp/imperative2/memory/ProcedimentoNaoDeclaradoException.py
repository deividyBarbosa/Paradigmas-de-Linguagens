from li2.plp.expressions2.memory.IdentificadorNaoDeclaradoException import IdentificadorNaoDeclaradoException


class ProcedimentoNaoDeclaradoException(IdentificadorNaoDeclaradoException):
    def __init__(self, id):
        super().__init__(f"Procedimento {id} nao declarado.")
