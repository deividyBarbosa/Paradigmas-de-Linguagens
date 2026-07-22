"""
Atividade 1 (Lab 05 - li2).

Executa:
  { var a = 0, proc incA () {a := a + 1};
    call incA(); call incA(); write(a)
  }
"""
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
from li2.plp.imperative2.declaration.DeclaracaoProcedimento import DeclaracaoProcedimento
from li2.plp.imperative2.declaration.DefProcedimento import DefProcedimento
from li2.plp.imperative2.declaration.ListaDeclaracaoParametro import ListaDeclaracaoParametro
from li2.plp.imperative2.memory.ContextoExecucaoImperativa2 import ContextoExecucaoImperativa2
from li2.plp.imperative2.Programa import Programa


class Exemplo1:

    @staticmethod
    def main():
        a = Id("a")
        inc_a = Id("incA")

        def_inc_a = DefProcedimento(ListaDeclaracaoParametro(), Atribuicao(a, ExpSoma(a, ValorInteiro(1))))
        declaracoes = DeclaracaoComposta(
            DeclaracaoVariavel(a, ValorInteiro(0)),
            DeclaracaoProcedimento(inc_a, def_inc_a),
        )
        chamadas = SequenciaComando(
            ChamadaProcedimento(inc_a, ListaExpressao()),
            SequenciaComando(ChamadaProcedimento(inc_a, ListaExpressao()), Write(a)),
        )
        comando = ComandoDeclaracao(declaracoes, chamadas)
        programa = Programa(comando)

        if programa.checaTipo(ContextoCompilacaoImperativa(ListaValor())):
            saida = programa.executar(ContextoExecucaoImperativa2(ListaValor()))
            print(saida)
        else:
            print("Comando mal tipado.")


if __name__ == "__main__":
    Exemplo1.main()
