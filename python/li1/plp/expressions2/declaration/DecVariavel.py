from li1.plp.expressions2.expression.Expressao import Expressao
from li1.plp.expressions2.expression.Id import Id


class DecVariavel:
    """
    Associa um identificador a expressao que define seu valor/tipo.

    Nota: nenhuma classe de li1 referencia DecVariavel (o 'let' de expressao
    foi substituido, em li1, pelo comando de declaracao imperativo -- veja
    imperative1.declaration.DeclaracaoVariavel). A classe e mantida aqui
    apenas para espelhar fielmente o arquivo homonimo presente no Java
    original.
    """

    def __init__(self, id_arg: Id, expressao_arg: Expressao):
        self._id = id_arg
        self._expressao = expressao_arg

    def getID(self) -> Id:
        return self._id

    def getExpressao(self) -> Expressao:
        return self._expressao
