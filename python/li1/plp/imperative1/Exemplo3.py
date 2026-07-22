"""
Atividade 3 (Lab 04 - li1).

Executa:
  { var i = 0;
    while not (i == 3) do
      i := i + 1;
    write("Hello World")
  }

O 'while' vincula apenas o comando 'i := i + 1' (um unico comando); o
'write("Hello World")' e o proximo comando da sequencia, executado uma
unica vez apos o laco terminar (quando i chega a 3).
"""
from li1.plp.expressions2.expression.ExpEquals import ExpEquals
from li1.plp.expressions2.expression.ExpNot import ExpNot
from li1.plp.expressions2.expression.ExpSoma import ExpSoma
from li1.plp.expressions2.expression.Id import Id
from li1.plp.expressions2.expression.ValorInteiro import ValorInteiro
from li1.plp.expressions2.expression.ValorString import ValorString
from li1.plp.imperative1.command.Atribuicao import Atribuicao
from li1.plp.imperative1.command.ComandoDeclaracao import ComandoDeclaracao
from li1.plp.imperative1.command.SequenciaComando import SequenciaComando
from li1.plp.imperative1.command.While import While
from li1.plp.imperative1.command.Write import Write
from li1.plp.imperative1.declaration.DeclaracaoVariavel import DeclaracaoVariavel
from li1.plp.imperative1.memory.ContextoCompilacaoImperativa import ContextoCompilacaoImperativa
from li1.plp.imperative1.memory.ContextoExecucaoImperativa import ContextoExecucaoImperativa
from li1.plp.imperative1.memory.ListaValor import ListaValor
from li1.plp.imperative1.Programa import Programa


class Exemplo3:

    @staticmethod
    def main():
        i = Id("i")
        laco = While(ExpNot(ExpEquals(i, ValorInteiro(3))), Atribuicao(i, ExpSoma(i, ValorInteiro(1))))
        comando = ComandoDeclaracao(
            DeclaracaoVariavel(i, ValorInteiro(0)),
            SequenciaComando(laco, Write(ValorString("Hello World"))),
        )
        programa = Programa(comando)

        if programa.checaTipo(ContextoCompilacaoImperativa(ListaValor())):
            saida = programa.executar(ContextoExecucaoImperativa(ListaValor()))
            print(saida)
        else:
            print("Comando mal tipado.")


if __name__ == "__main__":
    Exemplo3.main()
