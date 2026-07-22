from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao
from loo1.plp.orientadaObjetos1.expressao.unaria.ExpUnaria import ExpUnaria
from loo1.plp.orientadaObjetos1.expressao.valor.ValorBooleano import ValorBooleano
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo


class ExpNot(ExpUnaria):
    """Representa uma expressao de Negacao logica."""

    def __init__(self, expressao: Expressao):
        super().__init__(expressao, "~")

    def avaliar(self, ambiente: "AmbienteExecucaoOO1") -> ValorBooleano:
        return ValorBooleano(not self.getExp().avaliar(ambiente).valor())

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        return super().checaTipo(ambiente) and self.getExp().getTipo(ambiente).eBooleano()

    def getTipo(self, ambiente: "AmbienteCompilacaoOO1") -> TipoPrimitivo:
        return TipoPrimitivo.TIPO_BOOLEANO
