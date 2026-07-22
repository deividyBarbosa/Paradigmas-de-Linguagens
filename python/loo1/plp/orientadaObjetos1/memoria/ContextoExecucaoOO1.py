from typing import Dict, List, Optional

from loo1.plp.expressions2.expression.Id import Id
from loo1.plp.orientadaObjetos1.excecao.declaracao.ClasseJaDeclaradaException import ClasseJaDeclaradaException
from loo1.plp.orientadaObjetos1.excecao.declaracao.ObjetoJaDeclaradoException import ObjetoJaDeclaradoException
from loo1.plp.orientadaObjetos1.excecao.declaracao.ObjetoNaoDeclaradoException import ObjetoNaoDeclaradoException
from loo1.plp.orientadaObjetos1.excecao.declaracao.VariavelJaDeclaradaException import VariavelJaDeclaradaException
from loo1.plp.orientadaObjetos1.excecao.declaracao.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from loo1.plp.orientadaObjetos1.excecao.execucao.EntradaInvalidaException import EntradaInvalidaException
from loo1.plp.orientadaObjetos1.expressao.valor.ValorBooleano import ValorBooleano
from loo1.plp.orientadaObjetos1.expressao.valor.ValorInteiro import ValorInteiro
from loo1.plp.orientadaObjetos1.expressao.valor.ValorString import ValorString
from loo1.plp.orientadaObjetos1.expressao.valor.ValorNull import ValorNull
from loo1.plp.orientadaObjetos1.expressao.valor.ValorRef import ValorRef
from loo1.plp.orientadaObjetos1.memoria.AmbienteExecucaoOO1 import AmbienteExecucaoOO1
from loo1.plp.orientadaObjetos1.memoria.colecao.ListaValor import ListaValor
from loo1.plp.orientadaObjetos1.util.Tipo import Tipo
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo


class ContextoExecucaoOO1(AmbienteExecucaoOO1):
    """Contexto de execucao da linguagem OO: variaveis, heap de objetos e E/S."""

    def __init__(self, ambiente: Optional[AmbienteExecucaoOO1] = None, entrada: Optional[ListaValor] = None):
        if ambiente is not None:
            # Construtor "filho": compartilha objetos/classes/entrada/saida com
            # o ambiente dado, mas cria uma pilha nova com apenas o 'this'.
            self._prox_ref = ambiente.getRef()
            self._map_objetos: Dict[ValorRef, "Objeto"] = ambiente.getMapObjetos()
            self._map_def_classe: Dict[Id, "DefClasse"] = ambiente.getMapDefClasse()
            self._entrada = ambiente.getEntrada()
            self._saida = ambiente.getSaida()
            self._pilha: List[Dict[Id, "Valor"]] = [{Id("this"): ValorNull()}]
        else:
            self._pilha = []
            self._map_objetos = {}
            self._map_def_classe = {}
            self._entrada = entrada
            self._saida = ListaValor()
            self._prox_ref = None

    def getPilha(self) -> List[Dict[Id, "Valor"]]:
        return self._pilha

    def setPilha(self, pilha: List[Dict[Id, "Valor"]]) -> None:
        self._pilha = pilha

    def setSaida(self, saida: ListaValor) -> None:
        self._saida = saida

    def getMapDefClasse(self) -> Dict[Id, "DefClasse"]:
        return self._map_def_classe

    def getMapObjetos(self) -> Dict[ValorRef, "Objeto"]:
        return self._map_objetos

    def read(self, tipo_id_lido: Tipo) -> "Valor":
        valor_lido = self._leEntrada()
        if valor_lido is not None:
            valor_lido = valor_lido.strip()
            if isinstance(tipo_id_lido, TipoPrimitivo):
                try:
                    if tipo_id_lido.eBooleano():
                        return ValorBooleano(valor_lido.lower() == "true")
                    elif tipo_id_lido.eInteiro():
                        return ValorInteiro(int(valor_lido))
                    elif tipo_id_lido.eString():
                        return ValorString(valor_lido)
                except ValueError:
                    raise EntradaInvalidaException(
                        "O tipo da entrada e o da variavel a ser lida sao diferentes!"
                    )
        raise EntradaInvalidaException("O tipo da variavel a ser lida nao e um tipo Primitivo!")

    def _leEntrada(self) -> str:
        if self._entrada is None:
            return self._leDaEntradaPadrao()
        if self._entrada.length() == 0:
            raise EntradaInvalidaException("Numero de argumentos menor do que o numero de reads!")
        return self._leDaListaValor()

    def _leDaEntradaPadrao(self) -> str:
        try:
            return input()
        except EOFError:
            print("Erro no valor lido da entrada padrao")
            return ""

    def _leDaListaValor(self) -> str:
        retorno = str(self._entrada.getHead())
        self._entrada = self._entrada.getTail()
        return retorno

    def getSaida(self) -> ListaValor:
        return self._saida

    def getEntrada(self) -> ListaValor:
        return self._entrada

    def write(self, v: "Valor") -> "ContextoExecucaoOO1":
        self._saida.write(v)
        return self

    def incrementa(self) -> None:
        self._pilha.append({})

    def restaura(self) -> None:
        self._pilha.pop()

    def map(self, id_arg: Id, valor_id: "Valor") -> None:
        topo = self._pilha[-1]
        if id_arg in topo:
            raise VariavelJaDeclaradaException(id_arg)
        topo[id_arg] = valor_id

    def mapDefClasse(self, id_arg: Id, def_classe: "DefClasse") -> None:
        if id_arg in self._map_def_classe:
            raise ClasseJaDeclaradaException(id_arg)
        self._map_def_classe[id_arg] = def_classe

    def mapObjeto(self, valor_ref: ValorRef, objeto: "Objeto") -> None:
        if valor_ref in self._map_objetos:
            raise ObjetoJaDeclaradoException(objeto.getClasse())
        self._map_objetos[valor_ref] = objeto

    def changeValor(self, id_arg: Id, valor_id: "Valor") -> None:
        for bloco in reversed(self._pilha):
            if id_arg in bloco:
                bloco[id_arg] = valor_id
                return
        raise VariavelNaoDeclaradaException(id_arg)

    def get(self, id_arg: Id) -> "Valor":
        for bloco in reversed(self._pilha):
            if id_arg in bloco:
                return bloco[id_arg]
        raise VariavelNaoDeclaradaException(id_arg)

    def getDefClasse(self, id_arg: Id) -> "DefClasse":
        # Fidelidade: diferente de ContextoCompilacaoOO1, aqui NAO se levanta
        # ClasseNaoDeclaradaException -- retorna None se a classe nao existir
        # (assim TipoClasse.eValido() pode checar "!= null").
        return self._map_def_classe.get(id_arg)

    def getObjeto(self, valor_ref: ValorRef) -> "Objeto":
        result = self._map_objetos.get(valor_ref)
        if result is None:
            raise ObjetoNaoDeclaradoException(Id(str(valor_ref)))
        return result

    def getProxRef(self) -> ValorRef:
        aux = ValorRef(self._prox_ref.valor())
        self._prox_ref = self._prox_ref.incrementa()
        return aux

    def getRef(self) -> ValorRef:
        if self._prox_ref is None:
            self._prox_ref = ValorRef(ValorRef.VALOR_INICIAL)
        return self._prox_ref

    def __str__(self) -> str:
        resposta = None
        for bloco in self._pilha:
            for id_, valor in bloco.items():
                resposta = f"{id_} {valor}\n"
        for valor_ref, objeto in self._map_objetos.items():
            resposta = f"{valor_ref} {objeto}\n"
        return resposta

    def getContextoIdValor(self) -> "ContextoExecucaoOO1":
        ambiente = ContextoExecucaoOO1(entrada=self.getEntrada())
        ambiente._pilha = self._pilha
        ambiente._saida = self._saida
        return ambiente

    def getValor(self, id_arg: Id) -> "Valor":
        return self.get(id_arg)
