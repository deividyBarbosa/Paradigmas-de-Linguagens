from loo1.plp.expressions2.expression.Id import Id as IdBase
from loo1.plp.orientadaObjetos1.expressao.leftExpression.LeftExpression import LeftExpression


class Id(IdBase, LeftExpression):
    """
    Um identificador usado como expressao dentro da linguagem OO.

    Estende expressions2.expression.Id (usado para nomes de classe/metodo)
    e implementa LeftExpression (usado como variavel/atribuicao). Os metodos
    avaliar/checaTipo/getTipo abaixo substituem os da superclasse: no Java
    original isso e resolvido por sobrecarga estatica (parametros de tipos
    de ambiente diferentes); em Python, como so o caminho OO e realmente
    usado, a sobrescrita direta e equivalente em efeito.
    """

    def __init__(self, str_name: str):
        super().__init__(str_name)

    def __str__(self) -> str:
        return self.getIdName()

    def avaliar(self, ambiente: "AmbienteExecucaoOO1") -> "Valor":
        return ambiente.get(self)

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        ambiente.get(self)  # verifica se esta no ambiente
        return True

    def getTipo(self, ambiente: "AmbienteCompilacaoOO1"):
        return ambiente.get(self)

    def getId(self) -> "Id":
        return self
