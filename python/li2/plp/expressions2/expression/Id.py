from li2.plp.expressions2.expression.Expressao import Expressao
from li2.plp.expressions2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException


class Id(Expressao):
    """Um identificador (nome de variavel), tambem e uma Expressao."""

    def __init__(self, str_name: str):
        self._id_name = str_name

    def __str__(self) -> str:
        return self._id_name

    def avaliar(self, ambiente: "AmbienteExecucao") -> "Valor":
        return ambiente.get(self)

    def checaTipo(self, amb: "AmbienteCompilacao") -> bool:
        """Valida se o identificador estah declarado no ambiente."""
        amb.get(self)  # se estiver no ambiente, entao esta ok.
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
        if not isinstance(obj, Id):
            return False
        return self._id_name == obj._id_name

    def reduzir(self, ambiente: "AmbienteExecucao") -> Expressao:
        """
        O Java original checa `instanceof ValorIrredutivel`, tipo que so
        existe em estagios posteriores (loo1.functional2), fora do escopo
        de li2. Como esse tipo nao existe aqui, a reducao sempre retorna
        uma copia do valor encontrado no ambiente.
        """
        try:
            valor = ambiente.get(self)
            return valor.clone()
        except VariavelNaoDeclaradaException:
            return self

    def clone(self) -> "Id":
        return self
