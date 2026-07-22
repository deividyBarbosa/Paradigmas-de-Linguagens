from abc import abstractmethod

from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao


class LeftExpression(Expressao):
    """Uma expressao que fica do lado esquerdo de uma atribuicao ou antes de uma chamada de metodo."""

    @abstractmethod
    def getId(self) -> "Id":
        """
        Obtem o identificador dessa expressao. No caso de um acesso de
        atributo, e o proprio atributo acessado; no caso de um Id, e ele mesmo.
        """
        raise NotImplementedError
