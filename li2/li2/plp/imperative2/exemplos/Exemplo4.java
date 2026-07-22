package li2.plp.imperative2.exemplos;

import li2.plp.expressions1.util.TipoPrimitivo;
import li2.plp.expressions2.expression.*;
import li2.plp.expressions2.memory.VariavelNaoDeclaradaException;
import li2.plp.imperative1.command.*;
import li2.plp.imperative1.declaration.*;
import li2.plp.imperative1.memory.ListaValor;
import li2.plp.imperative2.Programa;
import li2.plp.imperative2.command.*;
import li2.plp.imperative2.declaration.*;
import li2.plp.imperative2.memory.*;

/**
 * Atividade 4.
 *
 * Igual a Atividade 3, mas a chamada externa passa "a" em vez de "b":
 *
 *   { var b = 3,
 *     proc escreveRecursivo (int a) {
 *       if (not (a == 0)) then {
 *         var x = 0; x := a - 1;
 *         write("Ola");
 *         call escreveRecursivo(x)}
 *       else skip
 *     };
 *     call escreveRecursivo(a) }
 *
 * No bloco externo apenas "b" esta declarado; o identificador "a" e local ao
 * procedimento e NAO esta em escopo no ponto da chamada.  Avaliar o argumento
 * "a" provoca VariavelNaoDeclaradaException -- o programa esta mal formado.
 * Esta classe demonstra/captura esse erro.
 */
public class Exemplo4 {

	public static void main(String[] args) throws Exception {

		// ---------- Corpo do procedimento (identico ao Exemplo3) ----------
		Comando comandoThen = new ComandoDeclaracao(
				new DeclaracaoVariavel(new Id("x"), new ValorInteiro(0)),
				new SequenciaComando(
						new Atribuicao(new Id("x"),
								new ExpSub(new Id("a"), new ValorInteiro(1))),
						new SequenciaComando(
								new Write(new ValorString("Ola")),
								new ChamadaProcedimento(new Id("escreveRecursivo"),
										new ListaExpressao(new Id("x"))))));

		Comando corpoProcedimento = new IfThenElse(
				new ExpNot(new ExpEquals(new Id("a"), new ValorInteiro(0))),
				comandoThen,
				new Skip());

		ListaDeclaracaoParametro parametros =
				new ListaDeclaracaoParametro(
						new DeclaracaoParametro(new Id("a"), TipoPrimitivo.INTEIRO));
		DefProcedimento defProc =
				new DefProcedimento(parametros, corpoProcedimento);

		// ---------- Declaracoes do bloco: var b = 3, proc ... ----------
		Declaracao declaracoes = new DeclaracaoComposta(
				new DeclaracaoVariavel(new Id("b"), new ValorInteiro(3)),
				new DeclaracaoProcedimento(new Id("escreveRecursivo"), defProc));

		// ---------- Corpo do bloco: call escreveRecursivo(a) ----------
		// "a" nao esta declarado neste escopo -> erro em tempo de execucao.
		Comando corpo = new ChamadaProcedimento(new Id("escreveRecursivo"),
				new ListaExpressao(new Id("a")));

		Comando programa = new ComandoDeclaracao(declaracoes, corpo);

		AmbienteExecucaoImperativa2 ambiente =
				new ContextoExecucaoImperativa2(new ListaValor());

		try {
			ListaValor saida = new Programa(programa).executar(ambiente);
			System.out.println("Exemplo4 -> saida: " + saida);
		} catch (VariavelNaoDeclaradaException e) {
			System.out.println("Exemplo4 -> erro esperado: variavel nao declarada -> "
					+ e.getMessage());
		}
	}
}
