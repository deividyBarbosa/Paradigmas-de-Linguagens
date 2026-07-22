"""
Atividade 1 (Lab 03 - lf1).

Avalia: let fun f x = x + 1 in f 2
"""
from lf1.plp.expressions2.expression.ExpSoma import ExpSoma
from lf1.plp.expressions2.expression.Id import Id
from lf1.plp.expressions2.expression.ValorInteiro import ValorInteiro
from lf1.plp.functional1.declaration.DecFuncao import DecFuncao
from lf1.plp.functional1.expression.Aplicacao import Aplicacao
from lf1.plp.functional1.expression.ExpDeclaracao import ExpDeclaracao
from lf1.plp.functional1.Programa import Programa
from lf1.plp.functional1.util.ValorFuncao import ValorFuncao


class Exemplo1:

    @staticmethod
    def main():
        x = Id("x")
        f = Id("f")
        fun_f = DecFuncao(f, ValorFuncao([x], ExpSoma(x, ValorInteiro(1))))
        expressao = ExpDeclaracao([fun_f], Aplicacao(f, [ValorInteiro(2)]))
        programa = Programa(expressao)
        if programa.checaTipo():
            print(programa.executar())
        else:
            print("Expressao mal tipada.")


if __name__ == "__main__":
    Exemplo1.main()
