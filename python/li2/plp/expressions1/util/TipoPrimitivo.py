from enum import Enum

from li2.plp.expressions1.util.Tipo import Tipo


class TipoPrimitivo(Tipo, Enum):
    """Enum que representa os possiveis tipos primitivos de uma expressao."""

    INTEIRO = "INTEIRO"
    BOOLEANO = "BOOLEANO"
    STRING = "STRING"

    def getNome(self) -> str:
        return self.value

    def eInteiro(self) -> bool:
        return self.eIgual(TipoPrimitivo.INTEIRO)

    def eBooleano(self) -> bool:
        return self.eIgual(TipoPrimitivo.BOOLEANO)

    def eString(self) -> bool:
        return self.eIgual(TipoPrimitivo.STRING)

    def eIgual(self, tipo: Tipo) -> bool:
        if self.eValido():
            if tipo.eValido():
                return self.getNome() == tipo.getNome()
            return tipo.eIgual(self)
        return False

    def eValido(self) -> bool:
        return bool(self.getNome())

    def intersecao(self, outro_tipo: Tipo):
        if outro_tipo.eIgual(self):
            return self
        return None

    def __str__(self) -> str:
        return self.getNome()
