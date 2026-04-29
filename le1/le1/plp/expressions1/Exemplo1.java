package le1.plp.expressions1;
import le1.plp.expressions1.expression.*;


public class Exemplo1{
    public static void main(String[] args) {
        
        Expressao expr = new ExpSoma(new ValorInteiro(4), new ExpSub((new ValorInteiro(12)), new ValorInteiro(3)));
        Programa programa = new Programa(expr);
        
        programa.executar();
    }
}
