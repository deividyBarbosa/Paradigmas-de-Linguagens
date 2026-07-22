from enum import Enum, auto
from typing import FrozenSet, Optional


class Tipos(Enum):
    """Equivalente ao enum interno Tipo.Tipos do Java."""
    INTEIRO = auto()
    BOOLEANO = auto()
    STRING = auto()
    PID = auto()
    TUPLA = auto()


class Tipo:
    """
    Classe que representa os possiveis tipos de uma expressao.
    Objetos desta classe sao imutaveis, portanto as vezes as
    instancias sao compartilhadas.
    """

    def __init__(self, tipo: Optional[FrozenSet[Tipos]] = None, prox: "Tipo" = None):
        # Sem argumento de tipo, equivale ao construtor Java Tipo() -> EnumSet.allOf
        self._tipo: FrozenSet[Tipos] = frozenset(Tipos) if tipo is None else frozenset(tipo)
        self._prox = prox

    def get(self) -> FrozenSet[Tipos]:
        """Retorna o tipo da expressao associada (conjunto imutavel)."""
        return self._tipo

    def eInteiro(self) -> bool:
        return Tipos.INTEIRO in self._tipo

    def eBooleano(self) -> bool:
        return Tipos.BOOLEANO in self._tipo

    def eString(self) -> bool:
        return Tipos.STRING in self._tipo

    def ePid(self) -> bool:
        return Tipos.PID in self._tipo

    def eTupla(self) -> bool:
        return Tipos.TUPLA in self._tipo

    def eVoid(self) -> bool:
        """Indica se esta expressao nao pode representar tipo algum."""
        return len(self._tipo) == 0

    def __eq__(self, outro) -> bool:
        return isinstance(outro, Tipo) and outro._tipo == self._tipo

    def __hash__(self):
        return hash(self._tipo)

    def intersecao(self, outro_tipo: "Tipo") -> "Tipo":
        """Retorna o tipo mais abrangente que engloba este tipo e o tipo dado."""
        if self._tipo == outro_tipo._tipo:
            return self
        return Tipo(self._tipo & outro_tipo._tipo)

    def getProx(self) -> Optional["Tipo"]:
        return self._prox

    def setProx(self, novo_prox: "Tipo") -> None:
        self._prox = novo_prox

    def eValido(self) -> bool:
        return len(self._tipo) == 1

    def __repr__(self):
        return f"Tipo({sorted(t.name for t in self._tipo)})"


Tipo.TIPO_INTEIRO = Tipo(frozenset({Tipos.INTEIRO}))
Tipo.TIPO_BOOLEANO = Tipo(frozenset({Tipos.BOOLEANO}))
Tipo.TIPO_STRING = Tipo(frozenset({Tipos.STRING}))
Tipo.TIPO_PID = Tipo(frozenset({Tipos.PID}))
Tipo.TIPO_TUPLA = Tipo(frozenset({Tipos.TUPLA}))
Tipo.TIPO_INDEFINIDO = Tipo(frozenset())
