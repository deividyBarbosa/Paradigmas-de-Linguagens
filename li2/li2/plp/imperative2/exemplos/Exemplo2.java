package li2.plp.imperative2.exemplos;

import li2.plp.expressions1.util.TipoPrimitivo;
import li2.plp.expressions2.expression.*;
import li2.plp.imperative1.command.*;
import li2.plp.imperative1.declaration.*;
import li2.plp.imperative1.memory.ListaValor;
import li2.plp.imperative2.Programa;
import li2.plp.imperative2.command.*;
import li2.plp.imperative2.declaration.*;
import li2.plp.imperative2.memory.*;

/**
 * Atividade 2.
 *
 * Ilustra o escopo dinamico da li2, executando:
 *
 *   { var x = 0, proc p (int y) {x := x + y};
 *     { var x = 1; call p(3); write(x) };
 *     call p(4); write(x) }
 *
 * Como o escopo e dinamico, a primeira chamada (dentro do bloco interno onde
 * x = 1) imprime 4; na segunda chamada apenas o x externo (= 0) esta em
 * escopo e o valor produzido tambem e 4.  Saida esperada: 4 4.
 */
public class Exemplo2 {

	public static void main(String[] args) throws Exception {

		// ---------- Declaracoes do bloco externo ----------
		// var x = 0
		Declaracao declaracaoVariavel =
				new DeclaracaoVariavel(new Id("x"), new ValorInteiro(0));

		// proc p (int y) { x := x + y }
		ListaDeclaracaoParametro parametros =
				new ListaDeclaracaoParametro(
						new DeclaracaoParametro(new Id("y"), TipoPrimitivo.INTEIRO));
		DefProcedimento defP = new DefProcedimento(
				parametros,
				new Atribuicao(new Id("x"),
						new ExpSoma(new Id("x"), new Id("y"))));
		Declaracao declaracaoProcedimento =
				new DeclaracaoProcedimento(new Id("p"), defP);

		Declaracao declaracoes =
				new DeclaracaoComposta(declaracaoVariavel, declaracaoProcedimento);

		// ---------- Bloco interno: { var x = 1; call p(3); write(x) } ----------
		Comando blocoInterno = new ComandoDeclaracao(
				new DeclaracaoVariavel(new Id("x"), new ValorInteiro(1)),
				new SequenciaComando(
						new ChamadaProcedimento(new Id("p"),
								new ListaExpressao(new ValorInteiro(3))),
						new Write(new Id("x"))));

		// ---------- Corpo do bloco externo ----------
		// blocoInterno ; call p(4) ; write(x)
		Comando corpo = new SequenciaComando(
				blocoInterno,
				new SequenciaComando(
						new ChamadaProcedimento(new Id("p"),
								new ListaExpressao(new ValorInteiro(4))),
						new Write(new Id("x"))));

		Comando programa = new ComandoDeclaracao(declaracoes, corpo);

		AmbienteExecucaoImperativa2 ambiente =
				new ContextoExecucaoImperativa2(new ListaValor());

		ListaValor saida = new Programa(programa).executar(ambiente);
		System.out.println("Exemplo2 -> saida: " + saida);  // esperado: 4 4
	}
}
