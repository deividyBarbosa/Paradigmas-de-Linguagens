"""
Atividade 3 (Lab 05 - li2).

Executa:
  { var b = 3,
    proc escreveRecursivo (int a) {
      if (not (a == 0)) then {
        var x = 0; x := a - 1;
        write("Ola");
        call escreveRecursivo(x)
      } else skip
    };
    call escreveRecursivo(b)
  }
"""
from li2.plp.expressions1.util.TipoPrimitivo import TipoPrimitivo
from li2.plp.expressions2.expression.ExpEquals import ExpEquals
from li2.plp.expressions2.expression.ExpNot import ExpNot
from li2.plp.expressions2.expression.ExpSub import ExpSub
from li2.plp.expressions2.expression.Id import Id
from li2.plp.expressions2.expression.ValorInteiro import ValorInteiro
from li2.plp.expressions2.expression.ValorString import ValorString
from li2.plp.imperative1.command.Atribuicao import Atribuicao
from li2.plp.imperative1.command.ComandoDeclaracao import ComandoDeclaracao
from li2.plp.imperative1.command.IfThenElse import IfThenElse
from li2.plp.imperative1.command.SequenciaComando import SequenciaComando
from li2.plp.imperative1.command.Skip import Skip
from li2.plp.imperative1.command.Write import Write
from li2.plp.imperative1.declaration.DeclaracaoComposta import DeclaracaoComposta
from li2.plp.imperative1.declaration.DeclaracaoVariavel import DeclaracaoVariavel
from li2.plp.imperative1.memory.ContextoCompilacaoImperativa import ContextoCompilacaoImperativa
from li2.plp.imperative1.memory.ListaValor import ListaValor
from li2.plp.imperative2.command.ChamadaProcedimento import ChamadaProcedimento
from li2.plp.imperative2.command.ListaExpressao import ListaExpressao
from li2.plp.imperative2.declaration.DeclaracaoParametro import DeclaracaoParametro
from li2.plp.imperative2.declaration.DeclaracaoProcedimento import DeclaracaoProcedimento
from li2.plp.imperative2.declaration.DefProcedimento import DefProcedimento
from li2.plp.imperative2.declaration.ListaDeclaracaoParametro import ListaDeclaracaoParametro
from li2.plp.imperative2.memory.ContextoExecucaoImperativa2 import ContextoExecucaoImperativa2
from li2.plp.imperative2.Programa import Programa


class Exemplo3:

    @staticmethod
    def main():
        b = Id("b")
        a = Id("a")
        x = Id("x")
        escreve_recursivo = Id("escreveRecursivo")

        corpo_then = ComandoDeclaracao(
            DeclaracaoVariavel(x, ValorInteiro(0)),
            SequenciaComando(
                Atribuicao(x, ExpSub(a, ValorInteiro(1))),
                SequenciaComando(
                    Write(ValorString("Ola")),
                    ChamadaProcedimento(escreve_recursivo, ListaExpressao(x)),
                ),
            ),
        )
        corpo_proc = IfThenElse(ExpNot(ExpEquals(a, ValorInteiro(0))), corpo_then, Skip())

        def_proc = DefProcedimento(
            ListaDeclaracaoParametro(DeclaracaoParametro(a, TipoPrimitivo.INTEIRO)), corpo_proc
        )
        declaracoes = DeclaracaoComposta(
            DeclaracaoVariavel(b, ValorInteiro(3)), DeclaracaoProcedimento(escreve_recursivo, def_proc)
        )

        # call escreveRecursivo(b) -- 'b' esta declarado no escopo externo.
        comando = ComandoDeclaracao(declaracoes, ChamadaProcedimento(escreve_recursivo, ListaExpressao(b)))
        programa = Programa(comando)

        if programa.checaTipo(ContextoCompilacaoImperativa(ListaValor())):
            saida = programa.executar(ContextoExecucaoImperativa2(ListaValor()))
            print(saida)
        else:
            print("Comando mal tipado.")


if __name__ == "__main__":
    Exemplo3.main()
