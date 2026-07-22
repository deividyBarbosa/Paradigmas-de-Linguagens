from abc import abstractmethod

from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao


class Valor(Expressao):
    """
    Agrupa objetos dos diferentes valores primitivos.

    Nota de fidelidade: esta classe deliberadamente NAO define '__eq__'.
    No Java original, Valor nao sobrescreve equals(Object), entao '=='
    (ou .equals() quando chamado com o tipo estatico Valor) cai no
    comportamento padrao de identidade de objeto. Deixar '__eq__' herdado
    de object (tambem identidade) reproduz esse comportamento -- inclusive
    a peculiaridade de ExpEquals ao comparar Valores que nao sejam
    ValorConcreto (ex.: dois ValorRef "iguais em conteudo" mas gerados em
    momentos diferentes NAO sao considerados iguais nesse caminho).
    """

    @abstractmethod
    def getTipo(self, ambiente: "AmbienteCompilacaoOO1"):
        """Retorna o tipo do valor."""
        raise NotImplementedError
