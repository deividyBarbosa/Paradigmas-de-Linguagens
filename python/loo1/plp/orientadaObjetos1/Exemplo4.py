"""
Atividade 4 (Lab 06 - loo1).

Executa (classe LValor da Atividade 3, acrescida do metodo remove):
  { classe LValor {
      int valor = -100,
      LValor prox = null;

      proc insere(int v) { ... }  (identico a Atividade 3)
      proc remove(int v) {
        {
          LValor aux = this;
          while(not((aux.prox == null) or (((aux).prox).valor == v))) do {
            aux := aux.prox
          };
          if ( not( aux.prox == null) ) then {
            aux.prox := ((aux).prox).prox
          }
          else { skip}
        }
      },
      proc print() { ... }  (identico a Atividade 3)
    };
    { LValor lv := new LValor;
      lv.insere(2);lv.insere(3);
      lv.insere(4);lv.print();
      lv.remove(3);lv.print()
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
from loo1.plp.orientadaObjetos1.comando.While import While
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
from loo1.plp.orientadaObjetos1.expressao.binaria.ExpOr import ExpOr
from loo1.plp.orientadaObjetos1.expressao.leftExpression.AcessoAtributoId import AcessoAtributoId
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


def classe_lvalor_com_remove():
    """Classe LValor da Atividade 3, acrescida do metodo remove(int v)."""
    id_lvalor = Id("LValor")
    id_valor = Id("valor")
    id_prox = Id("prox")
    id_v = Id("v")
    id_aux = Id("aux")

    atributos = CompostaDecVariavel(
        SimplesDecVariavel(TipoPrimitivo.TIPO_INTEIRO, id_valor, ValorInteiro(-100)),
        SimplesDecVariavel(TipoClasse(id_lvalor), id_prox, ValorNull()),
    )

    # proc insere(int v)  -- identico a Atividade 3.
    then_insere = Sequencial(
        Atribuicao(AcessoAtributoThis(This(), id_valor), id_v),
        New(AcessoAtributoThis(This(), id_prox), id_lvalor),
    )
    else_insere = ChamadaMetodo(AcessoAtributoThis(This(), id_prox), Id("insere"), ListaExpressao(id_v))
    corpo_insere = IfThenElse(
        ExpEquals(AcessoAtributoThis(This(), id_valor), ValorInteiro(-100)), then_insere, else_insere
    )
    proc_insere = DecProcedimentoSimples(
        Id("insere"), ListaDeclaracaoParametro(DecParametro(id_v, TipoPrimitivo.TIPO_INTEIRO)), corpo_insere
    )

    # proc print()  -- identico a Atividade 3.
    corpo_print = Sequencial(
        Write(AcessoAtributoThis(This(), id_valor)),
        IfThenElse(
            ExpNot(ExpEquals(AcessoAtributoThis(This(), id_prox), ValorNull())),
            ChamadaMetodo(AcessoAtributoThis(This(), id_prox), Id("print"), ListaExpressao()),
            Skip(),
        ),
    )
    proc_print = DecProcedimentoSimples(Id("print"), ListaDeclaracaoParametro(), corpo_print)

    # proc remove(int v)
    decl_aux = SimplesDecVariavel(TipoClasse(id_lvalor), id_aux, This())
    cond_while = ExpNot(
        ExpOr(
            ExpEquals(AcessoAtributoId(id_aux, id_prox), ValorNull()),
            ExpEquals(AcessoAtributoId(AcessoAtributoId(id_aux, id_prox), id_valor), id_v),
        )
    )
    laco = While(cond_while, Atribuicao(id_aux, AcessoAtributoId(id_aux, id_prox)))
    cond_if = ExpNot(ExpEquals(AcessoAtributoId(id_aux, id_prox), ValorNull()))
    then_if = Atribuicao(
        AcessoAtributoId(id_aux, id_prox),
        AcessoAtributoId(AcessoAtributoId(id_aux, id_prox), id_prox),
    )
    corpo_remove = ComDeclaracao(decl_aux, Sequencial(laco, IfThenElse(cond_if, then_if, Skip())))
    proc_remove = DecProcedimentoSimples(
        Id("remove"), ListaDeclaracaoParametro(DecParametro(id_v, TipoPrimitivo.TIPO_INTEIRO)), corpo_remove
    )

    metodos = DecProcedimentoComposta(DecProcedimentoComposta(proc_insere, proc_print), proc_remove)
    return DecClasseSimples(id_lvalor, atributos, metodos), id_lvalor


class Exemplo4:

    @staticmethod
    def main():
        dec_classe, id_lvalor = classe_lvalor_com_remove()

        id_lv = Id("lv")
        decl_lv = DecVariavelObjeto(TipoClasse(id_lvalor), id_lv, id_lvalor)

        insere = lambda v: ChamadaMetodo(id_lv, Id("insere"), ListaExpressao(ValorInteiro(v)))
        imprime = ChamadaMetodo(id_lv, Id("print"), ListaExpressao())
        remove_3 = ChamadaMetodo(id_lv, Id("remove"), ListaExpressao(ValorInteiro(3)))

        comando = ComDeclaracao(
            decl_lv,
            Sequencial(
                insere(2),
                Sequencial(
                    insere(3),
                    Sequencial(insere(4), Sequencial(imprime, Sequencial(remove_3, imprime))),
                ),
            ),
        )
        programa = Programa(dec_classe, comando)

        if programa.checaTipo(ContextoCompilacaoOO1(ListaValor())):
            programa.executar(ContextoExecucaoOO1(entrada=ListaValor()))
        else:
            print("Programa mal tipado.")


if __name__ == "__main__":
    Exemplo4.main()
