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
 * Atividade 3.
 *
 * Ilustra um procedimento recursivo, executando:
 *
 *   { var b = 3,
 *     proc escreveRecursivo (int a) {
 *       if (not (a == 0)) then {
 *         var x = 0; x := a - 1;
 *         write("Ola");
 *         call escreveRecursivo(x)}
 *       else skip
 *     };
 *     call escreveRecursivo(b) }
 *
 * A chamada call escreveRecursivo(b) parte de b = 3, gerando tres ocorrencias
 * de "Ola".  Saida esperada: "Ola" "Ola" "Ola".
 */
public class Exemplo3 {

	public static void main(String[] args) throws Exception {

		// ---------- Corpo do procedimento ----------
		// then: { var x = 0; x := a - 1; write("Ola"); call escreveRecursivo(x) }
		Comando comandoThen = new ComandoDeclaracao(
				new DeclaracaoVariavel(new Id("x"), new ValorInteiro(0)),
				new SequenciaComando(
						new Atribuicao(new Id("x"),
								new ExpSub(new Id("a"), new ValorInteiro(1))),
						new SequenciaComando(
								new Write(new ValorString("Ola")),
								new ChamadaProcedimento(new Id("escreveRecursivo"),
										new ListaExpressao(new Id("x"))))));

		// if (not (a == 0)) then {...} else skip
		Comando corpoProcedimento = new IfThenElse(
				new ExpNot(new ExpEquals(new Id("a"), new ValorInteiro(0))),
				comandoThen,
				new Skip());

		// proc escreveRecursivo (int a) { ... }
		ListaDeclaracaoParametro parametros =
				new ListaDeclaracaoParametro(
						new DeclaracaoParametro(new Id("a"), TipoPrimitivo.INTEIRO));
		DefProcedimento defProc =
				new DefProcedimento(parametros, corpoProcedimento);

		// ---------- Declaracoes do bloco ----------
		// var b = 3, proc escreveRecursivo (int a) {...}
		Declaracao declaracoes = new DeclaracaoComposta(
				new DeclaracaoVariavel(new Id("b"), new ValorInteiro(3)),
				new DeclaracaoProcedimento(new Id("escreveRecursivo"), defProc));

		// ---------- Corpo do bloco: call escreveRecursivo(b) ----------
		Comando corpo = new ChamadaProcedimento(new Id("escreveRecursivo"),
				new ListaExpressao(new Id("b")));

		Comando programa = new ComandoDeclaracao(declaracoes, corpo);

		AmbienteExecucaoImperativa2 ambiente =
				new ContextoExecucaoImperativa2(new ListaValor());

		ListaValor saida = new Programa(programa).executar(ambiente);
		System.out.println("Exemplo3 -> saida: " + saida);  // esperado: "Ola" "Ola" "Ola"
	}
}
