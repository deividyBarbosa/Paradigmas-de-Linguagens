from li2.plp.imperative1.command.Comando import Comando


class Skip(Comando):
    """Nao realiza nenhuma alteracao no ambiente."""

    def executar(self, ambiente: "AmbienteExecucaoImperativa") -> "AmbienteExecucaoImperativa":
        return ambiente

    def checaTipo(self, ambiente: "AmbienteCompilacaoImperativa") -> bool:
        return True
