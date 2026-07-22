from loo1.plp.orientadaObjetos1.comando.Comando import Comando


class Skip(Comando):
    """Nao realiza nenhuma alteracao no ambiente."""

    def executar(self, ambiente: "AmbienteExecucaoOO1") -> "AmbienteExecucaoOO1":
        return ambiente

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        return True
