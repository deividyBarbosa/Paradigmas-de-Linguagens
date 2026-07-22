from loo1.plp.orientadaObjetos1.expressao.binaria.ExpBinaria import ExpBinaria
from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao
from loo1.plp.orientadaObjetos1.expressao.valor.ValorBooleano import ValorBooleano
from loo1.plp.orientadaObjetos1.expressao.valor.ValorConcreto import ValorConcreto
from loo1.plp.orientadaObjetos1.util.TipoClasse import TipoClasse
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo


class ExpEquals(ExpBinaria):
    """Representa uma expressao de Igualdade entre expressoes de mesmo valor primitivo."""

    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "==")

    def avaliar(self, ambiente: "AmbienteExecucaoOO1") -> ValorBooleano:
        return self._verificarIgualdade(ambiente)

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        result = False
        if super().checaTipo(ambiente):
            if isinstance(self.getEsq().getTipo(ambiente), TipoClasse):
                result = self.getDir().getTipo(ambiente) == TipoClasse.TIPO_NULL or self.getEsq().getTipo(
                    ambiente
                ) == self.getDir().getTipo(ambiente)
            else:
                result = self.getEsq().getTipo(ambiente) == self.getDir().getTipo(ambiente)
        return result

    def getTipo(self, ambiente: "AmbienteCompilacaoOO1") -> TipoPrimitivo:
        return TipoPrimitivo.TIPO_BOOLEANO

    def _verificarIgualdade(self, ambiente: "AmbienteExecucaoOO1") -> ValorBooleano:
        v1 = self.getEsq().avaliar(ambiente)
        v2 = self.getDir().avaliar(ambiente)
        if isinstance(v1, ValorConcreto) and isinstance(v2, ValorConcreto):
            compara = v1.equalsValor(v2)
        else:
            # Fidelidade: sem overload de ValorConcreto aplicavel, o Java recorre a
            # Object.equals() (identidade). Ver nota em expressao/valor/Valor.py.
            compara = v1 == v2
        return ValorBooleano(compara)
