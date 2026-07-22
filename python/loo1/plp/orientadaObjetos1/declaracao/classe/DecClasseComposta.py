from loo1.plp.orientadaObjetos1.declaracao.classe.DecClasse import DecClasse


class DecClasseComposta(DecClasse):
    """Representa a declaracao de mais de uma classe."""

    def __init__(self, declaracao1: DecClasse, declaracao2: DecClasse):
        self._declaracao1 = declaracao1
        self._declaracao2 = declaracao2

    def elabora(self, ambiente: "AmbienteExecucaoOO1") -> "AmbienteExecucaoOO1":
        return self._declaracao2.elabora(self._declaracao1.elabora(ambiente))

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        return self._declaracao1.checaTipo(ambiente) and self._declaracao2.checaTipo(ambiente)
