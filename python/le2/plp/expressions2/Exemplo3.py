"""
Atividade 3 (Lab 02 - le2).

Avalia:
  let var x = 3 in
    let var y = x + 1 in
      let var x = 2 in
        x + y

y captura o valor de x=3 antes do x ser redeclarado como 2 -- resultado esperado: 2 + 4 = 6.
"""
from le2.plp.expressions2.Programa import Programa
from le2.plp.expressions2.declaration.DecVariavel import DecVariavel
from le2.plp.expressions2.expression.ExpDeclaracao import ExpDeclaracao
from le2.plp.expressions2.expression.ExpSoma import ExpSoma
from le2.plp.expressions2.expression.Id import Id
from le2.plp.expressions2.expression.ValorInteiro import ValorInteiro


class Exemplo3:

    @staticmethod
    def main():
        x = Id("x")
        y = Id("y")
        nivel3 = ExpDeclaracao([DecVariavel(x, ValorInteiro(2))], ExpSoma(x, y))
        nivel2 = ExpDeclaracao([DecVariavel(y, ExpSoma(x, ValorInteiro(1)))], nivel3)
        expressao = ExpDeclaracao([DecVariavel(x, ValorInteiro(3))], nivel2)
        programa = Programa(expressao)
        if programa.checaTipo():
            print(programa.executar())
        else:
            print("Expressao mal tipada.")


if __name__ == "__main__":
    Exemplo3.main()
