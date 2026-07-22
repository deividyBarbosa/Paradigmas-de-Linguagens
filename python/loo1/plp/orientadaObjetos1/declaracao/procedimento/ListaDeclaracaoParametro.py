from typing import List, Optional

from loo1.plp.imperative1.util.Lista import Lista
from loo1.plp.orientadaObjetos1.declaracao.procedimento.DecParametro import DecParametro
from loo1.plp.orientadaObjetos1.util.Tipo import Tipo


class ListaDeclaracaoParametro(Lista):
    """Um conjunto de declaracoes de parametro."""

    def __init__(self, declaracao: Optional[DecParametro] = None,
                 lista_declaracao: Optional["ListaDeclaracaoParametro"] = None):
        super().__init__(declaracao, lista_declaracao)

    def elabora(self, ambiente: "AmbienteExecucaoOO1") -> "AmbienteExecucaoOO1":
        """Cria um mapeamento do identificador para esta lista de declaracoes de parametro."""
        if self.getHead() is not None:
            if self.getTail() is not None:
                return self.getTail().elabora(self.getHead().elabora(ambiente))
            return self.getHead().elabora(ambiente)
        return ambiente

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        if self.getHead() is not None:
            if self.getTail() is not None:
                return self.getHead().checaTipo(ambiente) and self.getTail().checaTipo(ambiente)
            return self.getHead().checaTipo(ambiente)
        return True

    def declaraParametro(self, ambiente: "AmbienteCompilacaoOO1") -> "AmbienteCompilacaoOO1":
        """Cria um mapeamento do identificador para o tipo do parametro no AmbienteCompilacao."""
        if self.getHead() is not None:
            if self.getTail() is not None:
                return self.getTail().declaraParametro(self.getHead().declaraParametro(ambiente))
            return self.getHead().declaraParametro(ambiente)
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
