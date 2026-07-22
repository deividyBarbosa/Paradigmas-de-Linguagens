from abc import abstractmethod

from loo1.plp.orientadaObjetos1.expressao.valor.Valor import Valor


class ValorConcreto(Valor):
    """
    Representa um valor concreto (inteiro, booleano, string ou null).

    'equalsValor' e o analogo do metodo Java 'equals(ValorConcreto)' --
    um overload especifico por tipo, distinto da igualdade de identidade
    padrao de Valor (ver nota em Valor.py). Deu-se um nome proprio em vez
    de sobrescrever '__eq__' para nao alterar a semantica de identidade
    herdada de Valor nos pontos do codigo que comparam por '=='.
    """

    @abstractmethod
    def equalsValor(self, valor: "ValorConcreto") -> bool:
        raise NotImplementedError
