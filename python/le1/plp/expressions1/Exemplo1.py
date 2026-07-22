"""
Atividade 1 (Lab 01 - le1).

Avalia a expressao: 4 + 12 - 3
"""
from le1.plp.expressions1.Programa import Programa
from le1.plp.expressions1.expression.ExpSoma import ExpSoma
from le1.plp.expressions1.expression.ExpSub import ExpSub
from le1.plp.expressions1.expression.ValorInteiro import ValorInteiro


class Exemplo1:

    @staticmethod
    def main():
        # 4 + 12 - 3
        expressao = ExpSub(ExpSoma(ValorInteiro(4), ValorInteiro(12)), ValorInteiro(3))
        programa = Programa(expressao)
        if programa.checaTipo():
            programa.executar()
        else:
            print("Expressao mal tipada.")


if __name__ == "__main__":
    Exemplo1.main()
