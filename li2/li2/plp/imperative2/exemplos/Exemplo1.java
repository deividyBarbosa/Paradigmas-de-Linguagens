package li2.plp.imperative2.exemplos;

import li2.plp.expressions2.expression.*;
import li2.plp.imperative1.command.*;
import li2.plp.imperative1.declaration.*;
import li2.plp.imperative1.memory.ListaValor;
import li2.plp.imperative2.Programa;
import li2.plp.imperative2.command.*;
import li2.plp.imperative2.declaration.*;
import li2.plp.imperative2.memory.*;

/**
 * Atividade 1.
 *
 * Constroi e executa, usando a arvore sintatica abstrata da li2, o comando:
 *
 *   { var a = 0, proc incA () {a := a + 1};
 *     call incA(); call incA(); write(a) }
 *
 * Saida esperada: 2 (consequencia das duas chamadas ao procedimento).
 */
public class Exemplo1 {

	public static void main(String[] args) throws Exception {

		// ---------- Declaracoes do bloco ----------
		// var a = 0
		Declaracao declaracaoVariavel =
				new DeclaracaoVariavel(new Id("a"), new ValorInteiro(0));

		// proc incA () { a := a + 1 }
		DefProcedimento defIncA = new DefProcedimento(
				new ListaDeclaracaoParametro(),                 // sem parametros
				new Atribuicao(new Id("a"),
						new ExpSoma(new Id("a"), new ValorInteiro(1))));
		Declaracao declaracaoProcedimento =
				new DeclaracaoProcedimento(new Id("incA"), defIncA);

		// var a = 0, proc incA () {...}
		Declaracao declaracoes =
				new DeclaracaoComposta(declaracaoVariavel, declaracaoProcedimento);

		// ---------- Corpo do bloco ----------
		// call incA(); call incA(); write(a)
		Comando corpo = new SequenciaComando(
				new ChamadaProcedimento(new Id("incA"), new ListaExpressao()),
				new SequenciaComando(
						new ChamadaProcedimento(new Id("incA"), new ListaExpressao()),
						new Write(new Id("a"))));

		// ---------- Bloco completo ----------
		Comando programa = new ComandoDeclaracao(declaracoes, corpo);

		AmbienteExecucaoImperativa2 ambiente =
				new ContextoExecucaoImperativa2(new ListaValor());

		ListaValor saida = new Programa(programa).executar(ambiente);
		System.out.println("Exemplo1 -> saida: " + saida);  // esperado: 2
	}
}
