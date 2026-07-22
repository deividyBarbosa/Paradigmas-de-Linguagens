"""
Atividade 1 (Lab 06 - loo1).

Executa (precedido pela declaracao da classe Contador):
  { classe Contador {
      int valor = 1;
      proc print() { write(this.valor) },
      proc inc() { this.valor := this.valor+1 }
    };
    { Contador c:= new Contador;
      c.inc();
      c.print();
    }
  }
"""
from loo1.plp.orientadaObjetos1.comando.Atribuicao import Atribuicao
from loo1.plp.orientadaObjetos1.comando.ChamadaMetodo import ChamadaMetodo
from loo1.plp.orientadaObjetos1.comando.ComDeclaracao import ComDeclaracao
from loo1.plp.orientadaObjetos1.comando.Sequencial import Sequencial
from loo1.plp.orientadaObjetos1.comando.Write import Write
from loo1.plp.orientadaObjetos1.declaracao.classe.DecClasseSimples import DecClasseSimples
from loo1.plp.orientadaObjetos1.declaracao.procedimento.DecProcedimentoComposta import DecProcedimentoComposta
from loo1.plp.orientadaObjetos1.declaracao.procedimento.DecProcedimentoSimples import DecProcedimentoSimples
from loo1.plp.orientadaObjetos1.declaracao.procedimento.ListaDeclaracaoParametro import ListaDeclaracaoParametro
from loo1.plp.orientadaObjetos1.declaracao.variavel.DecVariavelObjeto import DecVariavelObjeto
from loo1.plp.orientadaObjetos1.declaracao.variavel.SimplesDecVariavel import SimplesDecVariavel
from loo1.plp.orientadaObjetos1.expressao.binaria.ExpSoma import ExpSoma
from loo1.plp.orientadaObjetos1.expressao.leftExpression.AcessoAtributoThis import AcessoAtributoThis
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
from loo1.plp.orientadaObjetos1.expressao.ListaExpressao import ListaExpressao
from loo1.plp.orientadaObjetos1.expressao.This import This
from loo1.plp.orientadaObjetos1.expressao.valor.ValorInteiro import ValorInteiro
from loo1.plp.orientadaObjetos1.memoria.ContextoCompilacaoOO1 import ContextoCompilacaoOO1
from loo1.plp.orientadaObjetos1.memoria.ContextoExecucaoOO1 import ContextoExecucaoOO1
from loo1.plp.orientadaObjetos1.memoria.colecao.ListaValor import ListaValor
from loo1.plp.orientadaObjetos1.Programa import Programa
from loo1.plp.orientadaObjetos1.util.TipoClasse import TipoClasse
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo


def classe_contador():
    """Constroi a declaracao da classe Contador, reaproveitada pelas Atividades 1 e 2."""
    id_contador = Id("Contador")
    id_valor = Id("valor")

    atributos = SimplesDecVariavel(TipoPrimitivo.TIPO_INTEIRO, id_valor, ValorInteiro(1))

    proc_print = DecProcedimentoSimples(
        Id("print"), ListaDeclaracaoParametro(), Write(AcessoAtributoThis(This(), id_valor))
    )
    proc_inc = DecProcedimentoSimples(
        Id("inc"),
        ListaDeclaracaoParametro(),
        Atribuicao(
            AcessoAtributoThis(This(), id_valor),
            ExpSoma(AcessoAtributoThis(This(), id_valor), ValorInteiro(1)),
        ),
    )
    metodos = DecProcedimentoComposta(proc_print, proc_inc)

    return DecClasseSimples(id_contador, atributos, metodos), id_contador


class Exemplo1:

    @staticmethod
    def main():
        dec_classe, id_contador = classe_contador()

        id_c = Id("c")
        decl_c = DecVariavelObjeto(TipoClasse(id_contador), id_c, id_contador)
        comando = ComDeclaracao(
            decl_c,
            Sequencial(
                ChamadaMetodo(id_c, Id("inc"), ListaExpressao()),
                ChamadaMetodo(id_c, Id("print"), ListaExpressao()),
            ),
        )
        programa = Programa(dec_classe, comando)

        if programa.checaTipo(ContextoCompilacaoOO1(ListaValor())):
            # Write ja imprime cada valor no momento da execucao (como no
            # Java original); nao repetimos a impressao aqui.
            programa.executar(ContextoExecucaoOO1(entrada=ListaValor()))
        else:
            print("Programa mal tipado.")


if __name__ == "__main__":
    Exemplo1.main()
