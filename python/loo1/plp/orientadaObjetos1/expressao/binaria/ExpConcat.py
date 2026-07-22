from loo1.plp.orientadaObjetos1.expressao.binaria.ExpBinaria import ExpBinaria
from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao
from loo1.plp.orientadaObjetos1.expressao.valor.ValorString import ValorString
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo


class ExpConcat(ExpBinaria):
    """Representa uma expressao de Concatenacao entre objetos ValorString."""

    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "++")

    def avaliar(self, ambiente: "AmbienteExecucaoOO1") -> ValorString:
        return ValorString(str(self.getEsq().avaliar(ambiente)) + str(self.getDir().avaliar(ambiente)))

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        # Fidelidade: o Java original usa 'ou' aqui (nao 'e'), permitindo concatenar
        # string com nao-string desde que ao menos um dos lados seja string.
        return super().checaTipo(ambiente) and (
            self.getEsq().getTipo(ambiente).eString() or self.getDir().getTipo(ambiente).eString()
        )

    def getTipo(self, ambiente: "AmbienteCompilacaoOO1") -> TipoPrimitivo:
        return TipoPrimitivo.TIPO_STRING
