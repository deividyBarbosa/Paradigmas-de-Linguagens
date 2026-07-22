"""
Atividade 2 (Lab 04 - li1).

Executa:
  { var a = 3; write(a);
    { var a = 2, var b = 5; write(a); write(b+a) };
    write(a)
  }

O bloco interno sombreia 'a'; ao sair do bloco, o 'a' externo (=3) volta a valer.
"""
from li1.plp.expressions2.expression.ExpSoma import ExpSoma
from li1.plp.expressions2.expression.Id import Id
from li1.plp.expressions2.expression.ValorInteiro import ValorInteiro
from li1.plp.imperative1.command.ComandoDeclaracao import ComandoDeclaracao
from li1.plp.imperative1.command.SequenciaComando import SequenciaComando
from li1.plp.imperative1.command.Write import Write
from li1.plp.imperative1.declaration.DeclaracaoComposta import DeclaracaoComposta
from li1.plp.imperative1.declaration.DeclaracaoVariavel import DeclaracaoVariavel
from li1.plp.imperative1.memory.ContextoCompilacaoImperativa import ContextoCompilacaoImperativa
from li1.plp.imperative1.memory.ContextoExecucaoImperativa import ContextoExecucaoImperativa
from li1.plp.imperative1.memory.ListaValor import ListaValor
from li1.plp.imperative1.Programa import Programa


class Exemplo2:

    @staticmethod
    def main():
        a = Id("a")
        b = Id("b")

        bloco_interno = ComandoDeclaracao(
            DeclaracaoComposta(DeclaracaoVariavel(a, ValorInteiro(2)), DeclaracaoVariavel(b, ValorInteiro(5))),
            SequenciaComando(Write(a), Write(ExpSoma(b, a))),
        )

        comando = ComandoDeclaracao(
            DeclaracaoVariavel(a, ValorInteiro(3)),
            SequenciaComando(Write(a), SequenciaComando(bloco_interno, Write(a))),
        )
        programa = Programa(comando)

        if programa.checaTipo(ContextoCompilacaoImperativa(ListaValor())):
            saida = programa.executar(ContextoExecucaoImperativa(ListaValor()))
            print(saida)
        else:
            print("Comando mal tipado.")


if __name__ == "__main__":
    Exemplo2.main()
