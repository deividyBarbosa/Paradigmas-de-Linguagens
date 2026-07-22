"""
Atividade 3 (Lab 06 - loo1).

Executa (precedido pela declaracao da classe LValor, uma lista encadeada):
  { classe LValor {
      int valor = -100,
      LValor prox = null;

      proc insere(int v) {
        if ((this).valor == -100) then {
          this.valor := v;
          this.prox := new LValor
        } else {(this).prox.insere(v)}
      },
      proc print() {
        write(this.valor);
        if (not(this.prox == null)) then
            {(this).prox.print()}
        else {skip}
      }
    };
    { LValor lv := new LValor;
      lv.insere(3); lv.insere(4);
      lv.print()
    }
  }
"""
from loo1.plp.orientadaObjetos1.comando.Atribuicao import Atribuicao
from loo1.plp.orientadaObjetos1.comando.ChamadaMetodo import ChamadaMetodo
from loo1.plp.orientadaObjetos1.comando.ComDeclaracao import ComDeclaracao
from loo1.plp.orientadaObjetos1.comando.IfThenElse import IfThenElse
from loo1.plp.orientadaObjetos1.comando.New import New
from loo1.plp.orientadaObjetos1.comando.Sequencial import Sequencial
from loo1.plp.orientadaObjetos1.comando.Skip import Skip
from loo1.plp.orientadaObjetos1.comando.Write import Write
from loo1.plp.orientadaObjetos1.declaracao.classe.DecClasseSimples import DecClasseSimples
from loo1.plp.orientadaObjetos1.declaracao.procedimento.DecParametro import DecParametro
from loo1.plp.orientadaObjetos1.declaracao.procedimento.DecProcedimentoComposta import DecProcedimentoComposta
from loo1.plp.orientadaObjetos1.declaracao.procedimento.DecProcedimentoSimples import DecProcedimentoSimples
from loo1.plp.orientadaObjetos1.declaracao.procedimento.ListaDeclaracaoParametro import ListaDeclaracaoParametro
from loo1.plp.orientadaObjetos1.declaracao.variavel.CompostaDecVariavel import CompostaDecVariavel
from loo1.plp.orientadaObjetos1.declaracao.variavel.DecVariavelObjeto import DecVariavelObjeto
from loo1.plp.orientadaObjetos1.declaracao.variavel.SimplesDecVariavel import SimplesDecVariavel
from loo1.plp.orientadaObjetos1.expressao.binaria.ExpEquals import ExpEquals
from loo1.plp.orientadaObjetos1.expressao.leftExpression.AcessoAtributoThis import AcessoAtributoThis
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
from loo1.plp.orientadaObjetos1.expressao.ListaExpressao import ListaExpressao
from loo1.plp.orientadaObjetos1.expressao.This import This
from loo1.plp.orientadaObjetos1.expressao.unaria.ExpNot import ExpNot
from loo1.plp.orientadaObjetos1.expressao.valor.ValorInteiro import ValorInteiro
from loo1.plp.orientadaObjetos1.expressao.valor.ValorNull import ValorNull
from loo1.plp.orientadaObjetos1.memoria.ContextoCompilacaoOO1 import ContextoCompilacaoOO1
from loo1.plp.orientadaObjetos1.memoria.ContextoExecucaoOO1 import ContextoExecucaoOO1
from loo1.plp.orientadaObjetos1.memoria.colecao.ListaValor import ListaValor
from loo1.plp.orientadaObjetos1.Programa import Programa
from loo1.plp.orientadaObjetos1.util.TipoClasse import TipoClasse
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo


def classe_lvalor():
    """Constroi a declaracao da classe LValor (lista encadeada), reaproveitada pelas Atividades 3 e 4."""
    id_lvalor = Id("LValor")
    id_valor = Id("valor")
    id_prox = Id("prox")
    id_v = Id("v")

    atributos = CompostaDecVariavel(
        SimplesDecVariavel(TipoPrimitivo.TIPO_INTEIRO, id_valor, ValorInteiro(-100)),
        SimplesDecVariavel(TipoClasse(id_lvalor), id_prox, ValorNull()),
    )

    # proc insere(int v)
    then_ramo = Sequencial(
        Atribuicao(AcessoAtributoThis(This(), id_valor), id_v),
        New(AcessoAtributoThis(This(), id_prox), id_lvalor),
    )
    else_ramo = ChamadaMetodo(AcessoAtributoThis(This(), id_prox), Id("insere"), ListaExpressao(id_v))
    corpo_insere = IfThenElse(
        ExpEquals(AcessoAtributoThis(This(), id_valor), ValorInteiro(-100)), then_ramo, else_ramo
    )
    proc_insere = DecProcedimentoSimples(
        Id("insere"),
        ListaDeclaracaoParametro(DecParametro(id_v, TipoPrimitivo.TIPO_INTEIRO)),
        corpo_insere,
    )

    # proc print()
    corpo_print = Sequencial(
        Write(AcessoAtributoThis(This(), id_valor)),
        IfThenElse(
            ExpNot(ExpEquals(AcessoAtributoThis(This(), id_prox), ValorNull())),
            ChamadaMetodo(AcessoAtributoThis(This(), id_prox), Id("print"), ListaExpressao()),
            Skip(),
        ),
    )
    proc_print = DecProcedimentoSimples(Id("print"), ListaDeclaracaoParametro(), corpo_print)

    metodos = DecProcedimentoComposta(proc_insere, proc_print)

    return DecClasseSimples(id_lvalor, atributos, metodos), id_lvalor, id_valor, id_prox


class Exemplo3:

    @staticmethod
    def main():
        dec_classe, id_lvalor, _id_valor, _id_prox = classe_lvalor()

        id_lv = Id("lv")
        decl_lv = DecVariavelObjeto(TipoClasse(id_lvalor), id_lv, id_lvalor)
        comando = ComDeclaracao(
            decl_lv,
            Sequencial(
                ChamadaMetodo(id_lv, Id("insere"), ListaExpressao(ValorInteiro(3))),
                Sequencial(
                    ChamadaMetodo(id_lv, Id("insere"), ListaExpressao(ValorInteiro(4))),
                    ChamadaMetodo(id_lv, Id("print"), ListaExpressao()),
                ),
            ),
        )
        programa = Programa(dec_classe, comando)

        if programa.checaTipo(ContextoCompilacaoOO1(ListaValor())):
            programa.executar(ContextoExecucaoOO1(entrada=ListaValor()))
        else:
            print("Programa mal tipado.")


if __name__ == "__main__":
    Exemplo3.main()
