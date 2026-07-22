from lf1.plp.expressions1.util.Tipo import Tipo
from lf1.plp.expressions2.expression.Expressao import Expressao
from lf1.plp.expressions2.expression.Id import Id
from lf1.plp.functional1.declaration.DeclaracaoFuncional import DeclaracaoFuncional
from lf1.plp.functional1.util.ValorFuncao import ValorFuncao


class DecFuncao(DeclaracaoFuncional):
    """Declaracao de funcao (aridade > 0, em geral) num bloco 'let' funcional."""

    def __init__(self, id_fun: Id, valor_funcao: ValorFuncao):
        self._id = id_fun
        self._valor_funcao = valor_funcao

    def __str__(self):
        lista_id = self._valor_funcao.getListaId()
        params = ", ".join(str(i) + ", " for i in lista_id) if lista_id else ""
        return f"fun {self._id} ({params}) = {self._valor_funcao.getExp()}"

    def getID(self) -> Id:
        return self._id

    def getExpressao(self) -> Expressao:
        return self._valor_funcao.getExp()

    def getFuncao(self) -> ValorFuncao:
        return self._valor_funcao

    def getAridade(self) -> int:
        """Retorna a aridade da funcao declarada."""
        return self._valor_funcao.getAridade()

    def checaTipo(self, ambiente: "AmbienteCompilacao") -> bool:
        ambiente.incrementa()
        tipo = Tipo()
        for _ in range(self.getAridade()):
            tipo = Tipo(prox=tipo)
        ambiente.map(self._id, tipo)
        result = self._valor_funcao.checaTipo(ambiente)
        ambiente.restaura()
        return result

    def getTipo(self, amb: "AmbienteCompilacao") -> Tipo:
        amb.incrementa()
        tipo = Tipo()
        for _ in range(self.getAridade()):
            tipo = Tipo(prox=tipo)
        amb.map(self._id, tipo)
        result = self._valor_funcao.getTipo(amb)
        amb.restaura()
        return result
