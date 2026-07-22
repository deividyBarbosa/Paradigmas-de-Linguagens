from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao
from loo1.plp.orientadaObjetos1.expressao.unaria.ExpUnaria import ExpUnaria
from loo1.plp.orientadaObjetos1.expressao.valor.ValorInteiro import ValorInteiro
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo


class ExpMenos(ExpUnaria):
    """Representa uma expressao de menos unario."""

    def __init__(self, expressao: Expressao):
        super().__init__(expressao, "-")

    def avaliar(self, ambiente: "AmbienteExecucaoOO1") -> ValorInteiro:
        return ValorInteiro(-self.getExp().avaliar(ambiente).valor())

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        return super().checaTipo(ambiente) and self.getExp().getTipo(ambiente).eInteiro()

    def getTipo(self, ambiente: "AmbienteCompilacaoOO1") -> TipoPrimitivo:
        return TipoPrimitivo.TIPO_INTEIRO
