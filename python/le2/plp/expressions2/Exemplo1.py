"""
Atividade 1 (Lab 02 - le2).

Avalia: let var x = 1 in x + 1
"""
from le2.plp.expressions2.Programa import Programa
from le2.plp.expressions2.declaration.DecVariavel import DecVariavel
from le2.plp.expressions2.expression.ExpDeclaracao import ExpDeclaracao
from le2.plp.expressions2.expression.ExpSoma import ExpSoma
from le2.plp.expressions2.expression.Id import Id
from le2.plp.expressions2.expression.ValorInteiro import ValorInteiro


class Exemplo1:

    @staticmethod
    def main():
        x = Id("x")
        expressao = ExpDeclaracao(
            [DecVariavel(x, ValorInteiro(1))],
            ExpSoma(x, ValorInteiro(1)),
        )
        programa = Programa(expressao)
        if programa.checaTipo():
            print(programa.executar())
        else:
            print("Expressao mal tipada.")


if __name__ == "__main__":
    Exemplo1.main()
