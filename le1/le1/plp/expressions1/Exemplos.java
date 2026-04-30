package le1.plp.expressions1;
import le1.plp.expressions1.expression.*;


public class Exemplos{
    public static void main(String[] args) {
        // Expressão 1: -4 + 12 - 3
        Expressao expr1 = new ExpSub(
            new ExpSoma(
                new ExpMenos(new ValorInteiro(4)), 
                new ValorInteiro(12)
            ), 
            new ValorInteiro(3)
        );
        Programa programa1 = new Programa(expr1);
        System.out.println("Expressão 1: -4 + 12 - 3 = ");
        if (programa1.checaTipo()) {
            programa1.executar();
        } else {
            System.out.println("Erro de tipo!");
        }
        System.out.println();
        
        // Expressão 2: length("abc") + 3
        Expressao expr2 = new ExpSoma(
            new ExpLength(new ValorString("abc")),
            new ValorInteiro(3)
        );
        Programa programa2 = new Programa(expr2);
        System.out.println("Expressão 2: length(\"abc\") + 3 = ");
        if (programa2.checaTipo()) {
            programa2.executar();
        } else {
            System.out.println("Erro de tipo!");
        }
        System.out.println();
        
        // Expressão 3: true and false
        Expressao expr3 = new ExpAnd(
            new ValorBooleano(true),
            new ValorBooleano(false)
        );
        Programa programa3 = new Programa(expr3);
        System.out.println("Expressão 3: true and false = ");
        if (programa3.checaTipo()) {
            programa3.executar();
        } else {
            System.out.println("Erro de tipo!");
        }
        System.out.println();
        
        // Expressão 4: "curso" ++ " de " ++ " paradigmas"
        Expressao expr4 = new ExpConcat(
            new ExpConcat(
                new ValorString("curso"),
                new ValorString(" de ")
            ),
            new ValorString(" paradigmas")
        );
        Programa programa4 = new Programa(expr4);
        System.out.println("Expressão 4: \"curso\" ++ \" de \" ++ \" paradigmas\" = ");
        if (programa4.checaTipo()) {
            programa4.executar();
        } else {
            System.out.println("Erro de tipo!");
        }
        System.out.println();
        
        // Expressão 5: 1 + true (tipo incorreto)
        Expressao expr5 = new ExpSoma(
            new ValorInteiro(1),
            new ValorBooleano(true)
        );
        Programa programa5 = new Programa(expr5);
        System.out.println("Expressão 5: 1 + true = ");
        if (programa5.checaTipo()) {
            programa5.executar();
        } else {
            System.out.println("Erro de tipo! Não é possível somar um inteiro com um booleano");
        }
    }
}
