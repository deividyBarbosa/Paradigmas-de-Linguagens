"""
Atividade 2 (Lab 03 - lf1).

Avalia:
  let var x = 3 in
    let fun f y = y + x in
      let var x = 5 in
        f 1

Nota: lf1 resolve identificadores livres no corpo da funcao pelo ambiente de
execucao vigente no momento da CHAMADA (a pilha e compartilhada entre variaveis
e funcoes -- nao ha captura de ambiente/closure). Ou seja, o 'x' usado em
'y + x' e resolvido dinamicamente: como 'f 1' e chamado dentro do escopo onde
x=5 ja foi declarado, esse e o x efetivamente visto (nao o x=3 do momento em
que f foi declarada). Isso contrasta com o escopo lexico usual de linguagens
funcionais e e discutido no relatorio.
"""
from lf1.plp.expressions2.expression.ExpSoma import ExpSoma
from lf1.plp.expressions2.expression.Id import Id
from lf1.plp.expressions2.declaration.DecVariavel import DecVariavel
from lf1.plp.expressions2.expression.ExpDeclaracao import ExpDeclaracao as ExpDeclaracaoVar
from lf1.plp.expressions2.expression.ValorInteiro import ValorInteiro
from lf1.plp.functional1.declaration.DecFuncao import DecFuncao
from lf1.plp.functional1.expression.Aplicacao import Aplicacao
from lf1.plp.functional1.expression.ExpDeclaracao import ExpDeclaracao
from lf1.plp.functional1.Programa import Programa
from lf1.plp.functional1.util.ValorFuncao import ValorFuncao


class Exemplo2:

    @staticmethod
    def main():
        x = Id("x")
        y = Id("y")
        f = Id("f")

        nivel3 = ExpDeclaracaoVar([DecVariavel(x, ValorInteiro(5))], Aplicacao(f, [ValorInteiro(1)]))
        fun_f = DecFuncao(f, ValorFuncao([y], ExpSoma(y, x)))
        nivel2 = ExpDeclaracao([fun_f], nivel3)
        expressao = ExpDeclaracaoVar([DecVariavel(x, ValorInteiro(3))], nivel2)

        programa = Programa(expressao)
        if programa.checaTipo():
            print(programa.executar())
        else:
            print("Expressao mal tipada.")


if __name__ == "__main__":
    Exemplo2.main()
