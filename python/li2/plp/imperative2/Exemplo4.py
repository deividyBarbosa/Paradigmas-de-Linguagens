"""
Atividade 4 (Lab 05 - li2).

Executa:
  { var b = 3,
    proc escreveRecursivo (int a) {
      if (not (a == 0)) then {
        var x = 0; x := a - 1;
        write("Ola");
        call escreveRecursivo(x)
      } else skip
    };
    call escreveRecursivo(a)
  }

Nota de fidelidade: o slide original desta atividade e identico ao da
Atividade 3, exceto pela chamada final usar 'escreveRecursivo(a)' em vez de
'escreveRecursivo(b)'. Como 'a' e apenas o parametro formal do procedimento
(visivel somente dentro do seu proprio corpo) e nao ha nenhuma variavel 'a'
declarada no escopo onde a chamada ocorre, essa chamada, tal como
literalmente especificada no slide, referencia um identificador nao
declarado. Mantivemos o enunciado tal como apresentado (nao trocamos por
'b') para reportar fielmente o resultado: uma VariavelNaoDeclaradaException
na checagem de tipos.
"""
from li2.plp.expressions1.util.TipoPrimitivo import TipoPrimitivo
from li2.plp.expressions2.expression.ExpEquals import ExpEquals
from li2.plp.expressions2.expression.ExpNot import ExpNot
from li2.plp.expressions2.expression.ExpSub import ExpSub
from li2.plp.expressions2.expression.Id import Id
from li2.plp.expressions2.expression.ValorInteiro import ValorInteiro
from li2.plp.expressions2.expression.ValorString import ValorString
from li2.plp.expressions2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
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


class Exemplo4:

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

        # call escreveRecursivo(a) -- exatamente como no slide (veja nota acima).
        comando = ComandoDeclaracao(declaracoes, ChamadaProcedimento(escreve_recursivo, ListaExpressao(a)))
        programa = Programa(comando)

        try:
            bem_tipado = programa.checaTipo(ContextoCompilacaoImperativa(ListaValor()))
        except VariavelNaoDeclaradaException as e:
            print(f"Comando mal tipado: {e}")
            return

        if bem_tipado:
            saida = programa.executar(ContextoExecucaoImperativa2(ListaValor()))
            print(saida)
        else:
            print("Comando mal tipado.")


if __name__ == "__main__":
    Exemplo4.main()
