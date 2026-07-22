from loo1.plp.expressions2.expression.Valor import Valor


class ValorIrredutivel(Valor):
    """Marca um valor que nao deve ser reduzido/substituido por Id.reduzir()."""

    def avaliar(self, amb: "AmbienteExecucao"):
        return None

    def checaTipo(self, amb: "AmbienteCompilacao") -> bool:
        return True

    def getTipo(self, amb: "AmbienteCompilacao"):
        return None

    def reduzir(self, ambiente: "AmbienteExecucao") -> "ValorIrredutivel":
        return self

    def clone(self) -> "ValorIrredutivel":
        return self
