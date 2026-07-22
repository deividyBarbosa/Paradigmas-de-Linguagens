from loo1.plp.orientadaObjetos1.expressao.binaria.ExpBinaria import ExpBinaria
from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao
from loo1.plp.orientadaObjetos1.expressao.valor.ValorInteiro import ValorInteiro
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo


class ExpSoma(ExpBinaria):
    """Representa uma expressao de Soma."""

    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "+")

    def avaliar(self, ambiente: "AmbienteExecucaoOO1") -> ValorInteiro:
        return ValorInteiro(self.getEsq().avaliar(ambiente).valor() + self.getDir().avaliar(ambiente).valor())

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        return (
            super().checaTipo(ambiente)
            and self.getEsq().getTipo(ambiente).eInteiro()
            and self.getDir().getTipo(ambiente).eInteiro()
        )

    def getTipo(self, ambiente: "AmbienteCompilacaoOO1") -> TipoPrimitivo:
        return TipoPrimitivo.TIPO_INTEIRO
