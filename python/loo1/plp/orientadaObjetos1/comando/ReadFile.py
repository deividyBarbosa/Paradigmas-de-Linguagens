import pickle
import traceback

from loo1.plp.orientadaObjetos1.comando.IO import IO
from loo1.plp.orientadaObjetos1.excecao.declaracao.ClasseNaoDeclaradaException import ClasseNaoDeclaradaException
from loo1.plp.orientadaObjetos1.excecao.declaracao.ObjetoJaDeclaradoException import ObjetoJaDeclaradoException
from loo1.plp.orientadaObjetos1.excecao.declaracao.ObjetoNaoDeclaradoException import ObjetoNaoDeclaradoException
from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id


class ReadFile(IO):
    """
    Le um objeto persistido em arquivo (ver nota de adaptacao em WriteFile.py:
    aqui usamos 'pickle' no lugar da serializacao Java, que dependia de uma
    classe auxiliar inexistente no repositorio original).
    """

    def __init__(self, id_: Id, dir_: Expressao, index: Expressao):
        self._id = id_
        self._dir = dir_
        self._index = index
        self._tipo_id = None

    def executar(self, ambiente: "AmbienteExecucaoOO1") -> "AmbienteExecucaoOO1":
        try:
            path = str(self._dir.avaliar(ambiente))
            objetos = []
            with open(path, "rb") as arquivo:
                while True:
                    try:
                        objetos.append(pickle.load(arquivo))
                    except EOFError:
                        break

            prox_ref = ambiente.getProxRef()
            pos = int(str(self._index.avaliar(ambiente)))

            ambiente.mapObjeto(prox_ref, objetos[pos])
            ambiente.changeValor(self._id, prox_ref)
        except (OSError, ObjetoNaoDeclaradoException, ClasseNaoDeclaradaException,
                ObjetoJaDeclaradoException, IndexError, pickle.UnpicklingError):
            traceback.print_exc()

        return ambiente

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        # Em tempo de compilacao nao se pode saber o tipo da entrada que sera lida.
        self._tipo_id = self._id.getTipo(ambiente)
        return self._id.checaTipo(ambiente)
