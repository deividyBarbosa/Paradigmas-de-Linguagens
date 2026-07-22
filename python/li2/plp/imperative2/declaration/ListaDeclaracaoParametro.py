from typing import List, Optional

from li2.plp.expressions1.util.Tipo import Tipo
from li2.plp.imperative1.util.Lista import Lista
from li2.plp.imperative2.declaration.DeclaracaoParametro import DeclaracaoParametro


class ListaDeclaracaoParametro(Lista[DeclaracaoParametro]):

    def __init__(self, declaracao: Optional[DeclaracaoParametro] = None,
                 lista_declaracao: Optional["ListaDeclaracaoParametro"] = None):
        super().__init__(declaracao, lista_declaracao)

    def checaTipo(self, ambiente: "AmbienteCompilacaoImperativa") -> bool:
        if self.getHead() is not None:
            if self.getTail() is not None:
                return self.getHead().checaTipo(ambiente) and self.getTail().checaTipo(ambiente)
            return self.getHead().checaTipo(ambiente)
        return True

    def elabora(self, ambiente: "AmbienteCompilacaoImperativa") -> "AmbienteCompilacaoImperativa":
        """Cria um mapeamento do identificador para o tipo de cada parametro."""
        if self.getHead() is not None:
            if self.getTail() is not None:
                return self.getTail().elabora(self.getHead().elabora(ambiente))
            return self.getHead().elabora(ambiente)
        return ambiente

    def getTipos(self) -> List[Tipo]:
        retorno: List[Tipo] = []
        head_temp = self.head
        tail_temp = self.tail
        while head_temp is not None:
            retorno.append(head_temp.getTipo())
            if tail_temp is not None:
                head_temp = tail_temp.getHead()
                tail_temp = tail_temp.getTail()
            else:
                head_temp = None
        return retorno
