from loo1.plp.orientadaObjetos1.expressao.binaria.ExpBinaria import ExpBinaria
from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao
from loo1.plp.orientadaObjetos1.expressao.valor.ValorBooleano import ValorBooleano
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo


class ExpAnd(ExpBinaria):
    """Representa uma expressao de Conjuncao logica."""

    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "and")

    def avaliar(self, ambiente: "AmbienteExecucaoOO1") -> ValorBooleano:
        return ValorBooleano(
            self.getEsq().avaliar(ambiente).valor() and self.getDir().avaliar(ambiente).valor()
        )

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        return (
            super().checaTipo(ambiente)
            and self.getEsq().getTipo(ambiente).eBooleano()
            and self.getDir().getTipo(ambiente).eBooleano()
        )

    def getTipo(self, ambiente: "AmbienteCompilacaoOO1") -> TipoPrimitivo:
        return TipoPrimitivo.TIPO_BOOLEANO
