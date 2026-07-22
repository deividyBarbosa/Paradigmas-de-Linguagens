from loo1.plp.expressions2.expression.Expressao import Expressao


class Id(Expressao):
    """Um identificador (nome de variavel, classe, procedimento etc.), tambem e uma Expressao."""

    def __init__(self, str_name: str):
        self._id_name = str_name

    def __str__(self) -> str:
        return self._id_name

    def avaliar(self, ambiente: "AmbienteExecucao") -> "Valor":
        return ambiente.get(self)

    def checaTipo(self, amb: "AmbienteCompilacao") -> bool:
        """Valida se o identificador estah declarado no ambiente."""
        amb.get(self)  # se nao estiver no ambiente, levanta VariavelNaoDeclaradaException
        return True

    def getTipo(self, amb: "AmbienteCompilacao"):
        return amb.get(self)

    def getIdName(self) -> str:
        return self._id_name

    def setIdName(self, id_name: str) -> None:
        self._id_name = id_name

    def __hash__(self) -> int:
        return hash(self._id_name)

    def __eq__(self, obj) -> bool:
        return isinstance(obj, Id) and obj._id_name == self._id_name

    def reduzir(self, ambiente: "AmbienteExecucao") -> Expressao:
        from loo1.plp.expressions2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
        from loo1.plp.functional2.expression.ValorIrredutivel import ValorIrredutivel

        try:
            valor = ambiente.get(self)
            if isinstance(valor, ValorIrredutivel):
                return self
            return valor.clone()
        except VariavelNaoDeclaradaException:
            return self

    def clone(self) -> "Id":
        return self
