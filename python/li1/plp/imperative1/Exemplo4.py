"""
Atividade 4 (Lab 04 - li1).

Executa:
  {var n = 0, var m = 0;
   n := 2; m := 3;
   if (m == n) then
     write("valores de entrada iguais")
   else
     write("valores de entrada diferentes")
  }
"""
from li1.plp.expressions2.expression.ExpEquals import ExpEquals
from li1.plp.expressions2.expression.Id import Id
from li1.plp.expressions2.expression.ValorInteiro import ValorInteiro
from li1.plp.expressions2.expression.ValorString import ValorString
from li1.plp.imperative1.command.Atribuicao import Atribuicao
from li1.plp.imperative1.command.ComandoDeclaracao import ComandoDeclaracao
from li1.plp.imperative1.command.IfThenElse import IfThenElse
from li1.plp.imperative1.command.SequenciaComando import SequenciaComando
from li1.plp.imperative1.command.Write import Write
from li1.plp.imperative1.declaration.DeclaracaoComposta import DeclaracaoComposta
from li1.plp.imperative1.declaration.DeclaracaoVariavel import DeclaracaoVariavel
from li1.plp.imperative1.memory.ContextoCompilacaoImperativa import ContextoCompilacaoImperativa
from li1.plp.imperative1.memory.ContextoExecucaoImperativa import ContextoExecucaoImperativa
from li1.plp.imperative1.memory.ListaValor import ListaValor
from li1.plp.imperative1.Programa import Programa


class Exemplo4:

    @staticmethod
    def main():
        n = Id("n")
        m = Id("m")

        condicional = IfThenElse(
            ExpEquals(m, n),
            Write(ValorString("valores de entrada iguais")),
            Write(ValorString("valores de entrada diferentes")),
        )
        comando = ComandoDeclaracao(
            DeclaracaoComposta(DeclaracaoVariavel(n, ValorInteiro(0)), DeclaracaoVariavel(m, ValorInteiro(0))),
            SequenciaComando(Atribuicao(n, ValorInteiro(2)), SequenciaComando(Atribuicao(m, ValorInteiro(3)), condicional)),
        )
        programa = Programa(comando)

        if programa.checaTipo(ContextoCompilacaoImperativa(ListaValor())):
            saida = programa.executar(ContextoExecucaoImperativa(ListaValor()))
            print(saida)
        else:
            print("Comando mal tipado.")


if __name__ == "__main__":
    Exemplo4.main()
