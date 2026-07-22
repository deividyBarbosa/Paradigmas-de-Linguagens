from loo1.plp.orientadaObjetos1.comando.Atribuicao import Atribuicao
from loo1.plp.orientadaObjetos1.comando.Comando import Comando
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
from loo1.plp.orientadaObjetos1.expressao.leftExpression.LeftExpression import LeftExpression
from loo1.plp.orientadaObjetos1.memoria.ContextoExecucaoOO1 import ContextoExecucaoOO1
from loo1.plp.orientadaObjetos1.memoria.ContextoObjeto import ContextoObjeto
from loo1.plp.orientadaObjetos1.memoria.Objeto import Objeto
from loo1.plp.orientadaObjetos1.util.TipoClasse import TipoClasse


class New(Comando):
    """Comando de criacao de objeto e atribuicao deste a uma left expression."""

    def __init__(self, av: LeftExpression, classe: Id):
        self._av = av
        self._classe = classe

    def executar(self, ambiente: "AmbienteExecucaoOO1") -> "AmbienteExecucaoOO1":
        def_classe = ambiente.getDefClasse(self._classe)
        dec_variavel = def_classe.getDecVariavel()

        # Cria uma instancia auxiliar do ambiente so para facilitar o elabora
        # da decVariavel (pode ser bem complexo dependendo da declaracao).
        aux = dec_variavel.elabora(ContextoExecucaoOO1(ambiente=ambiente))
        estado_obj = ContextoObjeto(aux.getPilha().pop())
        objeto = Objeto(self._classe, estado_obj)

        # Mapeia o objeto no ambiente.
        vr = ambiente.getProxRef()
        ambiente.mapObjeto(vr, objeto)
        ambiente = Atribuicao(self._av, vr).executar(ambiente)

        return ambiente

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        tp_classe = TipoClasse(self._classe)
        return (
            self._av.checaTipo(ambiente)
            and tp_classe.eValido(ambiente)
            and tp_classe == self._av.getTipo(ambiente)
        )

    def getClasse(self) -> Id:
        return self._classe

    def getAv(self) -> LeftExpression:
        return self._av
