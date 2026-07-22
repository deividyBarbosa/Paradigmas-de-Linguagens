from loo1.plp.orientadaObjetos1.expressao.valor.Valor import Valor
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo


class ValorRef(Valor):
    """Representa a referencia a um objeto no heap de objetos do ambiente."""

    VALOR_INICIAL = 0

    def __init__(self, valor: int):
        self._valor = valor if valor >= ValorRef.VALOR_INICIAL else ValorRef.VALOR_INICIAL

    def valor(self) -> int:
        return self._valor

    def avaliar(self, ambiente: "AmbienteExecucaoOO1") -> "ValorRef":
        return self

    def __hash__(self) -> int:
        return self._valor

    # Os metodos getTipo e checaTipo de ValorRef nao foram utilizados nessa linguagem.
    def getTipo(self, amb: "AmbienteCompilacaoOO1"):
        return TipoPrimitivo.TIPO_INTEIRO

    def checaTipo(self, amb: "AmbienteCompilacaoOO1") -> bool:
        return True

    def equalsValor(self, val: "Valor") -> bool:
        """Compara dois valores-referencia pelo conteudo (equivalente a equals(Valor) no Java)."""
        return isinstance(val, ValorRef) and self._valor == val.valor()

    def incrementa(self) -> "ValorRef":
        self._valor += 1
        return self

    def __str__(self) -> str:
        return str(self._valor)
