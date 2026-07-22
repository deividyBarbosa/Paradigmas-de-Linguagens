"""
Atividade 2 (Lab 05 - li2).

Executa:
  { var x = 0, proc p (int y) {x := x + y};
    { var x = 1; call p(3); write(x) };
    call p(4); write(x)
  }
"""
from li2.plp.expressions1.util.TipoPrimitivo import TipoPrimitivo
from li2.plp.expressions2.expression.ExpSoma import ExpSoma
from li2.plp.expressions2.expression.Id import Id
from li2.plp.expressions2.expression.ValorInteiro import ValorInteiro
from li2.plp.imperative1.command.Atribuicao import Atribuicao
from li2.plp.imperative1.command.ComandoDeclaracao import ComandoDeclaracao
from li2.plp.imperative1.command.SequenciaComando import SequenciaComando
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


class Exemplo2:

    @staticmethod
    def main():
        x = Id("x")
        y = Id("y")
        p = Id("p")

        def_p = DefProcedimento(
            ListaDeclaracaoParametro(DeclaracaoParametro(y, TipoPrimitivo.INTEIRO)),
            Atribuicao(x, ExpSoma(x, y)),
        )

        bloco_interno = ComandoDeclaracao(
            DeclaracaoVariavel(x, ValorInteiro(1)),
            SequenciaComando(ChamadaProcedimento(p, ListaExpressao(ValorInteiro(3))), Write(x)),
        )

        declaracoes = DeclaracaoComposta(DeclaracaoVariavel(x, ValorInteiro(0)), DeclaracaoProcedimento(p, def_p))
        comando = ComandoDeclaracao(
            declaracoes,
            SequenciaComando(
                bloco_interno,
                SequenciaComando(ChamadaProcedimento(p, ListaExpressao(ValorInteiro(4))), Write(x)),
            ),
        )
        programa = Programa(comando)

        if programa.checaTipo(ContextoCompilacaoImperativa(ListaValor())):
            saida = programa.executar(ContextoExecucaoImperativa2(ListaValor()))
            print(saida)
        else:
            print("Comando mal tipado.")


if __name__ == "__main__":
    Exemplo2.main()
