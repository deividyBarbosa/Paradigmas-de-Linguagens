package le1.plp.expressions1;
import le1.plp.expressions1.expression.*;


public class Exemplo1{
    public static void main(String[] args) {
        
        Expressao expr = new ExpSoma(new ValorString("abc"), new ExpSub((new ValorInteiro(12)), new ValorInteiro(5)));
        Programa programa = new Programa(expr);
        
        if (programa.checaTipo()) {
            System.out.println("Tipo válido!");
            programa.executar();
        } else {
            System.out.println("Erro de tipo!");
        }
    }
}
