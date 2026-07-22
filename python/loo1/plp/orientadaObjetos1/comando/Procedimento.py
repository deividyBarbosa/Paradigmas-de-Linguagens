class Procedimento:
    """Representa um procedimento (metodo) ja resolvido: parametros formais + comando."""

    def __init__(self, parametros_formais: "ListaDeclaracaoParametro", comando: "Comando"):
        self._parametros_formais = parametros_formais
        self._comando = comando

    def getParametrosFormais(self) -> "ListaDeclaracaoParametro":
        return self._parametros_formais

    def getComando(self) -> "Comando":
        return self._comando
