from lf1.plp.expressions1.util.Tipo import Tipo
from lf1.plp.expressions2.expression.Expressao import Expressao
from lf1.plp.expressions2.expression.Id import Id
from lf1.plp.functional1.declaration.DeclaracaoFuncional import DeclaracaoFuncional


class DecVariavel(DeclaracaoFuncional):
    """Declaracao de variavel (aridade 0) num bloco 'let' funcional."""

    def __init__(self, id_arg: Id, expressao_arg: Expressao):
        self._id = id_arg
        self._expressao = expressao_arg

    def getAridade(self) -> int:
        return 0

    def __str__(self):
        return f"var {self._id} = {self._expressao}"

    def getExpressao(self) -> Expressao:
        return self._expressao

    def getID(self) -> Id:
        return self._id

    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        return self._expressao.getTipo(amb)

    def checaTipo(self, ambiente: "AmbienteCompilacao") -> bool:
        return self._expressao.checaTipo(ambiente)
