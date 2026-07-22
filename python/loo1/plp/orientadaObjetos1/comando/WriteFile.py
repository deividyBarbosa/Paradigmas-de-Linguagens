import pickle
import traceback

from loo1.plp.orientadaObjetos1.comando.IO import IO
from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id


class WriteFile(IO):
    """
    Grava (acrescenta) o objeto referenciado por 'id' num arquivo.

    Nota de adaptacao: o Java original usa ObjectOutputStream/ObjectInputStream
    (serializacao binaria da JVM) e importa 'serializable.AppendingObjectOutputStream',
    uma classe auxiliar que nao existe em nenhum lugar deste repositorio -- ou
    seja, o WriteFile.java original nem compila isoladamente. Usamos aqui
    'pickle', o equivalente idiomatico do Python, com a mesma semantica de
    "grava mais um objeto ao final do arquivo" (ver ReadFile.py).
    """

    def __init__(self, id_: Id, dir_: Expressao):
        self._id = id_
        self._dir = dir_

    def executar(self, ambiente: "AmbienteExecucaoOO1") -> "AmbienteExecucaoOO1":
        path = str(self._dir.avaliar(ambiente))
        referencia = self._id.avaliar(ambiente)
        objeto = ambiente.getObjeto(referencia)

        try:
            with open(path, "ab") as arquivo:
                pickle.dump(objeto, arquivo)
        except OSError:
            traceback.print_exc()

        return ambiente

    def checaTipo(self, ambiente: "AmbienteCompilacaoOO1") -> bool:
        return self._id.checaTipo(ambiente)
