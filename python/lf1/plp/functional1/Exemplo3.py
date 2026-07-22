"""
Atividade 3 (Lab 03 - lf1).

Avalia:
  let var y = 3 in
    let fun f x = x + y in
      let var z = "abc" in
        f 3
"""
from lf1.plp.expressions2.declaration.DecVariavel import DecVariavel
from lf1.plp.expressions2.expression.ExpDeclaracao import ExpDeclaracao as ExpDeclaracaoVar
from lf1.plp.expressions2.expression.ExpSoma import ExpSoma
from lf1.plp.expressions2.expression.Id import Id
from lf1.plp.expressions2.expression.ValorInteiro import ValorInteiro
from lf1.plp.expressions2.expression.ValorString import ValorString
from lf1.plp.functional1.declaration.DecFuncao import DecFuncao
from lf1.plp.functional1.expression.Aplicacao import Aplicacao
from lf1.plp.functional1.expression.ExpDeclaracao import ExpDeclaracao
from lf1.plp.functional1.Programa import Programa
from lf1.plp.functional1.util.ValorFuncao import ValorFuncao


class Exemplo3:

    @staticmethod
    def main():
        y = Id("y")
        x = Id("x")
        z = Id("z")
        f = Id("f")

        nivel3 = ExpDeclaracaoVar([DecVariavel(z, ValorString("abc"))], Aplicacao(f, [ValorInteiro(3)]))
        fun_f = DecFuncao(f, ValorFuncao([x], ExpSoma(x, y)))
        nivel2 = ExpDeclaracao([fun_f], nivel3)
        expressao = ExpDeclaracaoVar([DecVariavel(y, ValorInteiro(3))], nivel2)

        programa = Programa(expressao)
        if programa.checaTipo():
            print(programa.executar())
        else:
            print("Expressao mal tipada.")


if __name__ == "__main__":
    Exemplo3.main()
