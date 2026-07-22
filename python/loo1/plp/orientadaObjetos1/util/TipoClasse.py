from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
from loo1.plp.orientadaObjetos1.util.Tipo import Tipo


class TipoClasse(Tipo):
    """Classe que representa o tipo de uma classe declarada pelo usuario (ou o tipo nulo)."""

    NULL = Id("NULL")

    def __init__(self, tipo_classe: Id):
        self._tipo_classe = tipo_classe

    def getTipo(self) -> Id:
        return self._tipo_classe

    def eValido(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        """Uma classe e um tipo valido se ja foi declarada (ou for o tipo NULL)."""
        from loo1.plp.orientadaObjetos1.excecao.declaracao.ClasseNaoDeclaradaException import (
            ClasseNaoDeclaradaException,
        )

        try:
            return self._tipo_classe == TipoClasse.NULL or ambiente.getDefClasse(self._tipo_classe) is not None
        except ClasseNaoDeclaradaException:
            return False

    def __eq__(self, obj) -> bool:
        return isinstance(obj, TipoClasse) and obj._tipo_classe == self._tipo_classe

    def __hash__(self):
        return hash(self._tipo_classe)

    def __str__(self) -> str:
        return str(self._tipo_classe)


TipoClasse.TIPO_NULL = TipoClasse(TipoClasse.NULL)
