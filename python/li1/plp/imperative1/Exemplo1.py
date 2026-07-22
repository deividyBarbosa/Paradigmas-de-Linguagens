"""
Atividade 1 (Lab 04 - li1).

Executa: { var a = 3; write(a) }
"""
from li1.plp.expressions2.expression.Id import Id
from li1.plp.expressions2.expression.ValorInteiro import ValorInteiro
from li1.plp.imperative1.command.Write import Write
from li1.plp.imperative1.command.ComandoDeclaracao import ComandoDeclaracao
from li1.plp.imperative1.declaration.DeclaracaoVariavel import DeclaracaoVariavel
from li1.plp.imperative1.memory.ContextoCompilacaoImperativa import ContextoCompilacaoImperativa
from li1.plp.imperative1.memory.ContextoExecucaoImperativa import ContextoExecucaoImperativa
from li1.plp.imperative1.memory.ListaValor import ListaValor
from li1.plp.imperative1.Programa import Programa


class Exemplo1:

    @staticmethod
    def main():
        a = Id("a")
        comando = ComandoDeclaracao(DeclaracaoVariavel(a, ValorInteiro(3)), Write(a))
        programa = Programa(comando)

        if programa.checaTipo(ContextoCompilacaoImperativa(ListaValor())):
            saida = programa.executar(ContextoExecucaoImperativa(ListaValor()))
            print(saida)
        else:
            print("Comando mal tipado.")


if __name__ == "__main__":
    Exemplo1.main()
