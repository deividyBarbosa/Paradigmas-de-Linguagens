from loo1.plp.expressions2.expression.Id import Id


class DefClasse:
    """
    Uma definicao de classe e uma declaracao de variavel (atributos) e uma
    declaracao de procedimento (metodos). Ambas podem ser simples ou compostas.
    """

    def __init__(self, id_classe: Id, dec_variavel: "DecVariavel", dec_procedimento: "DecProcedimento"):
        self._id_classe = id_classe
        self._dec_variavel = dec_variavel
        self._dec_procedimento = dec_procedimento

    def getDecVariavel(self) -> "DecVariavel":
        return self._dec_variavel

    def getMetodo(self, id_metodo: Id) -> "Procedimento":
        return self._dec_procedimento.getProcedimento(id_metodo)

    def getTipoAtributo(self, id_atributo: Id):
        return self._dec_variavel.getTipo(id_atributo)

    def getIdClasse(self) -> Id:
        return self._id_classe
