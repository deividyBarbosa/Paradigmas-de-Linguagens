from loo1.plp.orientadaObjetos1.comando.Comando import Comando
from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao
from loo1.plp.orientadaObjetos1.expressao.leftExpression.AcessoAtributo import AcessoAtributo
from loo1.plp.orientadaObjetos1.expressao.leftExpression.LeftExpression import LeftExpression
from loo1.plp.orientadaObjetos1.util.TipoClasse import TipoClasse


class Atribuicao(Comando):
    """Representa um comando de atribuicao."""

    def __init__(self, av: LeftExpression, expressao: Expressao):
        self._av = av
        self._expressao = expressao

    def executar(self, ambiente: "AmbienteExecucaoOO1") -> "AmbienteExecucaoOO1":
        id_variavel = self._av.getId()
        if isinstance(self._av, AcessoAtributo):
            # Se for acesso a atributo, precisa alterar o ambiente do objeto.
            exp_av = self._av.getExpressaoObjeto()
            referencia = exp_av.avaliar(ambiente)
            obj = ambiente.getObjeto(referencia)
            obj.changeAtributo(id_variavel, self._expressao.avaliar(ambiente))
        else:
            ambiente.changeValor(id_variavel, self._expressao.avaliar(ambiente))
        return ambiente

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        """
        Uma atribuicao esta bem tipada se o tipo do identificador e o mesmo da
        expressao (o tipo do identificador foi fixado na sua declaracao).
        """
        return self._expressao.checaTipo(ambiente) and (
            self._av.getTipo(ambiente) == self._expressao.getTipo(ambiente)
            or self._expressao.getTipo(ambiente) == TipoClasse.TIPO_NULL
        )
