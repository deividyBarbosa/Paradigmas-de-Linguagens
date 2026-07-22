from loo1.plp.orientadaObjetos1.expressao.valor.ValorConcreto import ValorConcreto
from loo1.plp.orientadaObjetos1.util.TipoClasse import TipoClasse


class ValorNull(ValorConcreto):
    """Este valor primitivo encapsula o valor nulo."""

    def __str__(self) -> str:
        return "null"

    def equalsValor(self, v: ValorConcreto) -> bool:
        return isinstance(v, ValorNull)

    def avaliar(self, amb: "AmbienteExecucaoOO1") -> "ValorNull":
        return self

    def checaTipo(self, amb: "AmbienteCompilacaoOO1") -> bool:
        return True

    def getTipo(self, amb: "AmbienteCompilacaoOO1"):
        return TipoClasse.TIPO_NULL
