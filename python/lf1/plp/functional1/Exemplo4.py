"""
Atividade 4 (Lab 03 - lf1).

Avalia:
  let fun mult x y = if (x == 0) then (0) else (y + mult (x - 1, y)) in mult (3,4)

mult(x, y) calcula x*y por somas repetidas de y -- resultado esperado: 12.
"""
from lf1.plp.expressions2.expression.ExpEquals import ExpEquals
from lf1.plp.expressions2.expression.ExpSoma import ExpSoma
from lf1.plp.expressions2.expression.ExpSub import ExpSub
from lf1.plp.expressions2.expression.Id import Id
from lf1.plp.expressions2.expression.ValorInteiro import ValorInteiro
from lf1.plp.functional1.declaration.DecFuncao import DecFuncao
from lf1.plp.functional1.expression.Aplicacao import Aplicacao
from lf1.plp.functional1.expression.ExpDeclaracao import ExpDeclaracao
from lf1.plp.functional1.expression.IfThenElse import IfThenElse
from lf1.plp.functional1.Programa import Programa
from lf1.plp.functional1.util.ValorFuncao import ValorFuncao


class Exemplo4:

    @staticmethod
    def main():
        x = Id("x")
        y = Id("y")
        mult = Id("mult")

        corpo = IfThenElse(
            ExpEquals(x, ValorInteiro(0)),
            ValorInteiro(0),
            ExpSoma(y, Aplicacao(mult, [ExpSub(x, ValorInteiro(1)), y])),
        )
        fun_mult = DecFuncao(mult, ValorFuncao([x, y], corpo))
        expressao = ExpDeclaracao([fun_mult], Aplicacao(mult, [ValorInteiro(3), ValorInteiro(4)]))

        programa = Programa(expressao)
        if programa.checaTipo():
            print(programa.executar())
        else:
            print("Expressao mal tipada.")


if __name__ == "__main__":
    Exemplo4.main()
