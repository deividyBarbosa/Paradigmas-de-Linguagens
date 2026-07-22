"""
Atividade 2 (Lab 01 - le1).

Avalia as expressoes:
  -4 + 12 - 3
  length("abc") + 3
  true and false
  "curso" ++ " de " ++ "paradigmas"
  1 + true          (mal tipada)
"""
from le1.plp.expressions1.Programa import Programa
from le1.plp.expressions1.expression.ExpAnd import ExpAnd
from le1.plp.expressions1.expression.ExpConcat import ExpConcat
from le1.plp.expressions1.expression.ExpLength import ExpLength
from le1.plp.expressions1.expression.ExpMenos import ExpMenos
from le1.plp.expressions1.expression.ExpSoma import ExpSoma
from le1.plp.expressions1.expression.ExpSub import ExpSub
from le1.plp.expressions1.expression.ValorBooleano import ValorBooleano
from le1.plp.expressions1.expression.ValorInteiro import ValorInteiro
from le1.plp.expressions1.expression.ValorString import ValorString


class Exemplos:

    @staticmethod
    def _executar(nome, expressao):
        print(f"--- {nome} ---")
        programa = Programa(expressao)
        if programa.checaTipo():
            programa.executar()
        else:
            print("Expressao mal tipada.")

    @staticmethod
    def main():
        # -4 + 12 - 3
        Exemplos._executar(
            '-4 + 12 - 3',
            ExpSub(ExpSoma(ExpMenos(ValorInteiro(4)), ValorInteiro(12)), ValorInteiro(3)),
        )

        # length("abc") + 3
        Exemplos._executar(
            'length("abc") + 3',
            ExpSoma(ExpLength(ValorString("abc")), ValorInteiro(3)),
        )

        # true and false
        Exemplos._executar(
            "true and false",
            ExpAnd(ValorBooleano(True), ValorBooleano(False)),
        )

        # "curso" ++ " de " ++ "paradigmas"
        Exemplos._executar(
            '"curso" ++ " de " ++ "paradigmas"',
            ExpConcat(ExpConcat(ValorString("curso"), ValorString(" de ")), ValorString("paradigmas")),
        )

        # 1 + true (mal tipada)
        Exemplos._executar(
            "1 + true",
            ExpSoma(ValorInteiro(1), ValorBooleano(True)),
        )


if __name__ == "__main__":
    Exemplos.main()
