# Relatório — Conversão Java → Python

**Disciplina:** Paradigmas de Linguagens de Programação
**Projeto:** Conversão das linguagens de expressão/imperativas/funcional/OO (le1, le2, lf1, li1, li2, loo1) de Java para Python, incluindo as atividades de cada laboratório.

---

## Introdução

Ao longo da disciplina foram implementadas, em Java, seis linguagens que evoluem umas a partir das outras — cada uma acrescentando um conceito de paradigma novo sobre a anterior:

| Pasta  | Linguagem                          | O que acrescenta                                   |
|--------|-------------------------------------|-----------------------------------------------------|
| `le1`  | Linguagem de Expressão 1            | Expressões constantes, tipos primitivos             |
| `le2`  | Linguagem de Expressão 2            | Variáveis e blocos `let`/escopo                     |
| `lf1`  | Linguagem Funcional 1                | Declaração e aplicação de funções de primeira ordem |
| `li1`  | Linguagem Imperativa 1               | Comandos, atribuição, `while`, `if`, E/S            |
| `li2`  | Linguagem Imperativa 2               | Procedimentos e chamada de procedimento             |
| `loo1` | Linguagem Orientada a Objetos 1       | Classes, objetos, `this`, métodos, referências       |

Nenhuma dessas linguagens possui um *parser*: um "programa" é montado diretamente em código, chamando construtores das classes que representam a árvore sintática (AST) — exatamente como um interpretador *tree-walking* clássico. Isso simplificou a conversão (não há léxico/gramática para portar), mas significa que as "atividades" de cada laboratório também são, na prática, pequenos programas Java (`Exemplo1`, `Exemplo2`, ...) que constroem essa árvore manualmente. Como a pasta do projeto não continha mais esses arquivos de exemplo (haviam sido removidos de uma cópia antiga do repositório), eles foram **recriados diretamente em Python**, seguindo os enunciados dos slides de cada laboratório.

Todo o código convertido está em [`python/`](python/), espelhando a estrutura de pacotes Java original (`python/<linguagem>/plp/...`). Os arquivos `.java` originais foram mantidos intactos em cada pasta (`le1/`, `le2/`, ...) para permitir comparação lado a lado.

### Convenções gerais adotadas na conversão

Estas decisões se repetem em todas as seis linguagens e por isso são explicadas uma única vez aqui:

- **Um arquivo por classe**, com o mesmo nome da classe Java (`ExpSoma.py`, `Contexto.py`, ...), preservando a navegação 1‑para‑1 entre a versão Java e a Python.
- **Interfaces Java → `abc.ABC` + `@abstractmethod`.** `Expressao`, `Comando`, `Ambiente<T>` etc. viram classes abstratas Python; os métodos abstratos usam `raise NotImplementedError` no corpo.
- **Generics (`ValorConcreto<T>`, `Ambiente<T>`) → `typing.Generic`/`TypeVar`.** O parâmetro de tipo é só documentação em Python (não há apagamento de tipo em tempo de execução como em Java, mas também não há verificação), então isso é usado apenas onde ajuda a manter a mesma hierarquia de superclasses (ex.: `AmbienteExecucao(Ambiente[Valor])`).
- **Exceções checked → exceções normais.** Java obriga a declarar `throws X` nas assinaturas; Python não tem esse conceito, então as assinaturas ficam mais limpas e as exceções simplesmente se propagam.
- **Casts explícitos (`(ValorInteiro) x`) foram omitidos.** Python é duck-typed: chamar `.valor()` em um objeto já garante o comportamento esperado se a verificação de tipos (`checaTipo`) tiver sido respeitada — o cast em Java só existia para satisfazer o compilador.
- **`toString()` → `__str__`**, com atenção a casos onde o Java tem formatação especial (`Boolean.toString()` gera `"true"/"false"` minúsculo, não `"True"/"False"`; strings em `li1`/`loo1` aparecem entre aspas).
- **Pilhas de escopo (`Stack<HashMap<Id,T>>`) → `list` de `dict`** Python, com `append`/`pop` no lugar de `push`/`pop`, e busca do topo para a base via `reversed(...)`.
- **Imports absolutos** (`from le1.plp.expressions1.expression.Valor import Valor`), com `python/` funcionando como a raiz do *classpath*. Para executar qualquer script, ele deve rodar a partir da pasta `python/` (ou com `python/` no `PYTHONPATH`), por exemplo:
  ```bash
  cd python
  python3 -m le1.plp.expressions1.Exemplo1
  ```

Cada seção abaixo segue os tópicos mínimos definidos em `Estrutura do relatório.md`, acrescentando o que foi necessário para explicar a conversão.

---

## Linguagem de Expressão 1 (le1)

### Expressões constantes

A `le1` é a linguagem mais simples: um programa é uma única expressão, e avaliá-lo produz um valor. Os valores são inteiros, booleanos e strings — sempre constantes, sem identificadores.

### BNF

```
Programa      ::= Expressao
Expressao     ::= Valor | ExpUnaria | ExpBinaria
Valor         ::= ValorConcreto
ValorConcreto ::= ValorInteiro | ValorBooleano | ValorString
ExpUnaria     ::= "-" Expressao | "not" Expressao | "length" Expressao
ExpBinaria    ::= Expressao "+" Expressao | Expressao "-" Expressao
                | Expressao "and" Expressao | Expressao "or" Expressao
                | Expressao "==" Expressao | Expressao "++" Expressao
```

### Exemplos de programas

| Expressão                              | Resultado             |
|-----------------------------------------|------------------------|
| `4 + 12 - 3`                             | `13`                   |
| `length("abc") + 3`                      | `6`                     |
| `true and false`                         | `false`                 |
| `"curso" ++ " de " ++ "paradigmas"`      | `"curso de paradigmas"` |
| `1 + true`                                | erro de tipo (`checaTipo() == False`) |

### Diagrama de classes → mapeamento Java/Python

| Java                                   | Python                                      | Observação |
|-----------------------------------------|-----------------------------------------------|------------|
| `interface Expressao`                   | `class Expressao(ABC)`                       | 3 métodos abstratos: `avaliar`, `checaTipo`, `getTipo` |
| `interface Valor extends Expressao`     | `class Valor(Expressao, ABC)`                | marcador, sem métodos novos |
| `abstract class ValorConcreto<T>`       | `class ValorConcreto(Valor, Generic[T])`     | `valor()`, `isEquals()`, `avaliar()` (retorna `self`) |
| `ValorInteiro`, `ValorBooleano`, `ValorString` | idem, herdando de `ValorConcreto[int\|bool\|str]` | `ValorBooleano.__str__` devolve `"true"/"false"` |
| `abstract class ExpUnaria`/`ExpBinaria` | idem, com `_checaTipoElementoTerminal` abstrato (método *template*) | `checaTipo()` concreto delega para a subclasse |
| `ExpAnd, ExpOr, ExpSoma, ExpSub, ExpConcat, ExpEquals` | idem | operadores binários |
| `ExpNot, ExpMenos, ExpLength`            | idem | operadores unários |
| `class Tipo` (com `enum Tipos` interno)  | `class Tipo` + `class Tipos(Enum)`           | o `EnumSet<Tipos>` do Java virou `frozenset[Tipos]` |
| `class Programa`                        | `class Programa`                             | `executar()` imprime e retorna o valor |

### Implementações

O ponto mais interessante da conversão é a classe `Tipo`: no Java ela guarda um `EnumSet<Tipos>` (podendo representar "qualquer tipo", útil para tipos ainda não resolvidos). Em Python isso virou um `frozenset` imutável, com `Tipo.TIPO_INTEIRO`, `Tipo.TIPO_BOOLEANO`, etc. definidos como constantes de classe logo após a definição (Python não tem "campo estático inicializado com `new` da própria classe" antes da classe existir, então as constantes são atribuídas depois, fora do corpo da classe).

```python
# python/le1/plp/expressions1/expression/ExpSoma.py
class ExpSoma(ExpBinaria):
    def __init__(self, esq: Expressao, dir: Expressao):
        super().__init__(esq, dir, "+")

    def avaliar(self, amb=None) -> ValorInteiro:
        return ValorInteiro(self.getEsq().avaliar().valor() + self.getDir().avaliar().valor())

    def _checaTipoElementoTerminal(self) -> bool:
        return self.getEsq().getTipo().eInteiro() and self.getDir().getTipo().eInteiro()

    def getTipo(self) -> Tipo:
        return Tipo.TIPO_INTEIRO
```

Note a ausência dos *casts* `(ValorInteiro)` presentes no Java: `getEsq().avaliar()` já é chamado apenas quando `checaTipo()` garantiu que o resultado é um `ValorInteiro`.

### Atividades

Implementadas em [`python/le1/plp/expressions1/Exemplo1.py`](python/le1/plp/expressions1/Exemplo1.py) (Atividade 1) e [`Exemplos.py`](python/le1/plp/expressions1/Exemplos.py) (Atividade 2). Saída obtida ao rodar (`python3 -m le1.plp.expressions1.Exemplo1` / `Exemplos`):

```
13                                    # 4 + 12 - 3
--- -4 + 12 - 3 ---
5
--- length("abc") + 3 ---
6
--- true and false ---
false
--- "curso" ++ " de " ++ "paradigmas" ---
curso de paradigmas
--- 1 + true ---
Expressao mal tipada.
```

Todos os resultados batem exatamente com os apresentados nos slides do laboratório.

---

## Linguagem de Expressão 2 (le2)

A `le2` acrescenta a `ExpDeclaracao` (bloco `let var x = ... in ...`) e um `Ambiente` de execução/compilação com pilha de escopos — reaproveitando quase toda a `le1` (o pacote `expressions1.util.Tipo` é literalmente copiado). A principal mudança estrutural é que toda `Expressao` passa a receber um `Ambiente` como parâmetro em `avaliar`/`checaTipo`/`getTipo`.

Em Python, o pacote `memory` reproduz a pilha `Stack<HashMap<Id,T>>` como `List[Dict]`, com `map()`/`get()` percorrendo os blocos do topo para a base:

```python
# python/le2/plp/expressions2/memory/Contexto.py
def get(self, id_arg) -> T:
    try:
        for bloco in reversed(self._pilha):
            if id_arg in bloco:
                return bloco[id_arg]
        raise IdentificadorNaoDeclaradoException()
    except IdentificadorNaoDeclaradoException:
        raise VariavelNaoDeclaradaException(id_arg)
```

Um detalhe de fidelidade: a classe `Id` (identificador) precisou implementar `__eq__`/`__hash__` baseados no nome, pois em Python, sem isso, cada `Id("x")` seria uma chave diferente no dicionário mesmo representando a "mesma" variável.

### Atividades

Implementadas em `python/le2/plp/expressions2/Exemplo1.py` a `Exemplo5.py`, todas envolvendo blocos `let` aninhados e sombreamento (*shadowing*) de variáveis:

| Atividade | Expressão | Resultado |
|-----------|-----------|-----------|
| 1 | `let var x = 1 in x + 1` | `2` |
| 2 | `let var x = 1 in let var x = 2 in x + 1` | `3` |
| 3 | `let var x = 3 in let var y = x + 1 in let var x = 2 in x + y` | `6` |
| 4 | `let var x = 3 in let var y = x + 1 in let var x = 5 in y` | `4` |
| 5 | `let var x = 3 in let var x = x + 1 in let var y = x in x + y` | `8` |

Todos os resultados foram obtidos executando os scripts (`python3 -m le2.plp.expressions2.Exemplo<N>`) e conferem com o comportamento esperado de escopo léxico com sombreamento: cada `let var x = ...` é avaliado no ambiente *anterior* à sua própria declaração, antes de `x` passar a se referir ao novo valor.

---

## Linguagem Funcional 1 (lf1)

### Linguagem Funcional de Primeira Ordem

A `lf1` introduz funções de primeira ordem: `let fun f x = <corpo> in f <arg>`. "Primeira ordem" aqui significa que funções não são valores de primeira classe — não podem ser passadas como argumento nem retornadas —, apenas declaradas e aplicadas pelo nome. Isso simplifica bastante o ambiente de execução: não é preciso capturar um *closure* (par função + ambiente léxico) para representar uma função, basta guardar a lista de parâmetros e a expressão do corpo (`ValorFuncao`).

Ao converter e **testar** essa parte descobri algo relevante sobre o paradigma implementado: **`lf1` resolve identificadores livres no corpo de uma função dinamicamente**, não lexicamente. Como não há captura de ambiente, quando uma função é chamada o interpretador simplesmente empilha um novo bloco de parâmetros sobre a pilha de execução *corrente* — a mesma pilha compartilhada entre variáveis e funções. Qualquer identificador livre no corpo da função (que não seja parâmetro) é procurado nessa pilha no momento da chamada, não no momento em que a função foi declarada. Isso foi comprovado empiricamente pela Atividade 2 (veja abaixo).

### Declarações

`ExpDeclaracao` (funcional) aceita uma lista de `DeclaracaoFuncional` — que pode ser `DecVariavel` (aridade 0) ou `DecFuncao` (aridade > 0, guarda uma `ValorFuncao`). A verificação de tipos de funções é a parte mais sofisticada de todo o projeto: como os parâmetros não têm tipo declarado, `ValorFuncao.getTipo()` executa uma pequena **inferência de tipos por unificação**, implementada em `RestrictTypesVisitor`. Essa classe percorre a árvore da expressão restringindo os tipos possíveis dos identificadores conforme o contexto em que aparecem (ex.: um identificador usado como operando de `+` só pode ser inteiro).

O `RestrictTypesVisitor` original em Java despacha dinamicamente por reflexão (`exp.getClass().getName()` → `_visitNomeDaClasse`). Em Python isso foi preservado quase literalmente, usando `type(exp).__name__` em vez de reflexão:

```python
# python/lf1/plp/functional1/util/RestrictTypesVisitor.py
@staticmethod
def visit(exp, ambiente, tipos, tipo_esperado):
    method_name = "_visit" + type(exp).__name__
    metodo = getattr(RestrictTypesVisitor, method_name, None)
    if metodo is None:
        raise NotImplementedError(f"O metodo visit chamado ({method_name}) nao foi implementado")
    return metodo(exp, ambiente, tipos, tipo_esperado)
```

### Implementações

`ContextoExecucaoFuncional` combina duas pilhas: uma de variáveis (reaproveitando `ContextoExecucao` de `expressions2`) e uma de funções. No Java, as duas pilhas são "amarradas" fazendo a pilha de função apontar para o mesmo objeto `Stack` usado internamente por um `Contexto<ValorFuncao>` genérico — de forma que incrementar/restaurar uma reflete na outra. Em Python isso foi reproduzido da mesma forma, aproveitando que listas são passadas por referência:

```python
self._pilha_funcao: List[Dict[Id, ValorFuncao]] = []
self._pilha_id_valor_func: Contexto = Contexto()
self._pilha_id_valor_func.setPilha(self._pilha_funcao)  # mesma lista, por referência
```

### Atividades

Implementadas em `python/lf1/plp/functional1/Exemplo1.py` a `Exemplo4.py`:

| Atividade | Expressão | Resultado |
|-----------|-----------|-----------|
| 1 | `let fun f x = x + 1 in f 2` | `3` |
| 2 | `let var x = 3 in let fun f y = y + x in let var x = 5 in f 1` | **`6`** |
| 3 | `let var y = 3 in let fun f x = x + y in let var z = "abc" in f 3` | `6` |
| 4 | `let fun mult x y = if (x==0) then 0 else y + mult(x-1,y) in mult(3,4)` | `12` |

O resultado `6` da Atividade 2 é a evidência do escopo dinâmico descrito acima: se `lf1` usasse escopo léxico (como Scheme/ML), `f 1` capturaria `x = 3` no momento da declaração de `f`, dando `1 + 3 = 4`. Como o resultado obtido é `6 = 1 + 5`, fica demonstrado que `f` "enxergou" o `x = 5` declarado depois dela, mas ainda em escopo no momento da chamada — uma boa discussão de paradigmas para o relatório (escopo estático vs. dinâmico).

---

## Linguagem Imperativa 1 (li1)

`li1` substitui expressões por **comandos** com efeito colateral (`Atribuicao`, `SequenciaComando`, `IfThenElse`, `While`, `Read`, `Write`) e um novo sistema de tipos: em vez da classe concreta `Tipo` (baseada em `EnumSet`) usada em `le1/le2/lf1`, o sistema de tipos vira uma **interface** `Tipo` implementada por um enum `TipoPrimitivo` (`INTEIRO`, `BOOLEANO`, `STRING`), preparando o terreno para `li2`/`loo1` adicionarem outros tipos (`TipoProcedimento`, `TipoClasse`) sem tocar no código que já usa `Tipo`.

Essa mudança de arquitetura foi o ponto mais delicado da conversão de `li1`: `TipoPrimitivo` precisa herdar tanto de `Tipo` (a "interface") quanto de `enum.Enum`. Em Python, misturar uma metaclasse `ABCMeta` (de `abc.ABC`) com `EnumMeta` (de `Enum`) gera conflito de metaclasse. A solução foi **não** usar `abc.ABC` para `Tipo` — ele é uma classe comum cujos métodos levantam `NotImplementedError` — o que permite o *mixin* padrão do Python (`class TipoPrimitivo(Tipo, Enum)`), do mesmo jeito que se faz `class Cor(str, Enum)`.

Outra diferença notável de `li1`: `Expressao` ganhou dois métodos novos, `reduzir(ambiente)` e `clone()`, usados por uma semântica de redução (*small-step*) que, ao investigar o código, não é de fato chamada pelo caminho de execução principal (`Programa` continua usando avaliação *big-step*, `avaliar()`). Eles foram implementados fielmente (inclusive a checagem de `instanceof ValorIrredutivel` em `Id.reduzir()`, ausente do próprio projeto `li1` e só disponível a partir de `loo1`), mas documentados como código morto nesta linguagem.

### Atividades

Implementadas em `python/li1/plp/imperative1/Exemplo1.py` a `Exemplo4.py`. A saída de um `Programa` em `li1` é a lista de valores escritos por `write(...)` (`ListaValor`), impressa ao final:

| Atividade | Comando | Saída |
|-----------|---------|-------|
| 1 | `{ var a = 3; write(a) }` | `3` |
| 2 | `{ var a = 3; write(a); { var a = 2, var b = 5; write(a); write(b+a) }; write(a) }` | `3 2 7 3` |
| 3 | `{ var i = 0; while not (i==3) do i:=i+1; write("Hello World") }` | `"Hello World"` |
| 4 | `{var n=0, var m=0; n:=2; m:=3; if (m==n) then write("...iguais") else write("...diferentes") }` | `"valores de entrada diferentes"` |

Na Atividade 3, vale notar que o `while` do BNF de `li1` vincula um **único** comando (`i := i + 1`); o `write("Hello World")` é o próximo comando da sequência, e por isso é executado uma única vez, após o laço terminar.

---

## Linguagem Imperativa 2 (li2)

### Procedimentos

`li2` acrescenta procedimentos (`proc nome(parametros) { corpo }`) e sua chamada (`call nome(argumentos)`), reaproveitando por completo `li1` (idêntico, salvo troca do nome do pacote) mais um pacote novo, `imperative2`. Um procedimento não tem valor de retorno — como em `li1` os comandos só têm efeito colateral, "chamar um procedimento" é executar seu corpo num ambiente novo, com os parâmetros já vinculados.

O tipo de um procedimento é modelado por `TipoProcedimento`, que **também implementa a interface `Tipo`** de `li1` — mais uma prova de que a extração de `Tipo` como interface em `li1` foi desenhada pensando exatamente nessa extensão: `TipoProcedimento` guarda a lista ordenada dos tipos dos parâmetros formais e não é nem inteiro, nem booleano, nem string.

### Exemplos de programa

```
{ var a = 0, proc incA () {a := a + 1};
  call incA(); call incA(); write(a)
}
```
produz `2`.

### Ambiente de execução

`ContextoExecucaoImperativa2` estende `ContextoExecucaoImperativa` (de `li1`) acrescentando um **segundo** `Contexto` paralelo, dedicado a `Id → DefProcedimento`, que cresce/encolhe em sincronia com a pilha de variáveis (o mesmo `incrementa()`/`restaura()` afeta as duas pilhas). A conversão para Python seguiu o mesmo padrão de composição usado em `lf1`.

### Chamada de procedimento

`ChamadaProcedimento.executar()` recupera a definição do procedimento pelo identificador, incrementa o ambiente, associa cada parâmetro formal ao valor do argumento real correspondente, executa o corpo nesse ambiente incrementado e o restaura ao final — devolvendo o ambiente com o efeito colateral já aplicado.

### Atividades

Implementadas em `python/li2/plp/imperative2/Exemplo1.py` a `Exemplo4.py`:

| Atividade | Saída |
|-----------|-------|
| 1 — `proc incA` chamado duas vezes | `2` |
| 2 — `proc p(int y)` chamado dentro e fora de um bloco que sombreia `x` | `4 4` |
| 3 — `proc escreveRecursivo` recursivo, `call escreveRecursivo(b)` | `"Ola" "Ola" "Ola"` |
| 4 — idêntico à 3, mas `call escreveRecursivo(a)` | *erro de tipo* |

A Atividade 4 merece um comentário: o slide original é idêntico ao da Atividade 3, exceto que a chamada final usa `escreveRecursivo(a)` em vez de `escreveRecursivo(b)`. Como `a` é apenas o parâmetro formal do procedimento (só existe dentro do próprio corpo), não há nenhuma variável `a` no escopo em que a chamada ocorre — o que aparenta ser um erro de digitação no material original. Optei por **manter o enunciado exatamente como no slide** em vez de "corrigi-lo" silenciosamente, e o resultado é justamente o esperado nesse caso: a verificação de tipos captura o identificador não declarado e levanta `VariavelNaoDeclaradaException`, o que a implementação Python reporta corretamente:

```
Comando mal tipado: Variavel a nao declarada.
```

Isso também serviu como um bom teste de que a checagem de tipos (`checaTipo`) da conversão está funcionando como esperado, e não apenas os "caminhos felizes".

---

## Linguagem Orientada a Objetos 1 (loo1)

### LOO

`loo1` é, de longe, a linguagem mais complexa do projeto: soma classes, objetos, referências (`this`, acesso a atributo, `new`), métodos e um mecanismo de persistência de objetos em arquivo (`ReadFile`/`WriteFile`). É também onde a conversão exigiu mais decisões de design, por isso destacadas aqui.

**Reorganização de pacotes.** Diferente das linguagens anteriores, em `loo1` as expressões binárias (`ExpAnd`, `ExpSoma`, `ExpEquals`, ...) saem do pacote `expressions2` e passam a viver dentro de `orientadaObjetos1.expressao.binaria` — o restante de `expressions2` (unárias, `Id`, valores primitivos) permanece, mas agora convive com um **sistema de tipos paralelo**: `expressions1.util.Tipo` (baseado em `EnumSet`, herdado de `le1`) continua sendo usado pelas poucas expressões que restaram em `expressions2`, enquanto `orientadaObjetos1.util.Tipo` (a interface no estilo de `li1`, implementada por `TipoPrimitivo` **e** por `TipoClasse`) é o sistema de tipos "de verdade" usado pela linguagem OO. Os dois foram convertidos como classes Python completamente independentes, com o mesmo nome `Tipo` em módulos diferentes — assim como no Java original.

**Duas classes `Id`.** Da mesma forma, existem duas classes chamadas `Id`: `expressions2.expression.Id` (usada para nomes de classe, de método/procedimento e de objeto) e `orientadaObjetos1.expressao.leftExpression.Id`, que **estende** a primeira e implementa `LeftExpression` (a interface de expressões que podem aparecer do lado esquerdo de uma atribuição). Python reproduz essa herança diretamente:

```python
# python/loo1/plp/orientadaObjetos1/expressao/leftExpression/Id.py
class Id(IdBase, LeftExpression):
    ...
```

Como `IdBase` já define `__eq__`/`__hash__` por nome, um `Id("this")` da subclasse e um `Id("this")` da classe-base **comparam como iguais** — a mesma propriedade que o Java obtém ao herdar `equals()`/`hashCode()`. Isso importa porque o próprio código-fonte mistura as duas classes ao usar `"this"` como chave (`ContextoExecucaoOO1` usa a `Id` base; `Objeto`/`AcessoAtributoThis` usam a `Id` de `leftExpression`) — um detalhe fácil de quebrar numa conversão descuidada, mas que aqui funciona por herança de igualdade, tal como no Java.

**Igualdade de valores e uma peculiaridade preservada de propósito.** Em Java, `Valor` não sobrescreve `equals(Object)` — herda a igualdade por identidade de `Object`. Cada subclasse concreta (`ValorInteiro`, `ValorBooleano`, ...) define, em vez disso, um **overload** `equals(ValorConcreto)`, usado explicitamente pelo interpretador. Como Python não tem sobrecarga de método, batizei esse método de `equalsValor(...)` (em vez de sobrescrever `__eq__`), preservando de propósito o comportamento *default* de `Valor` como identidade de objeto (que em Python já é o comportamento padrão de `__eq__` quando não sobrescrito). O efeito é sutil, mas real: em `ExpEquals`, comparar dois `ValorRef` (referências de objeto) cai no ramo de identidade, não no de conteúdo — reproduzindo fielmente uma peculiaridade (possivelmente não intencional) do código Java original, em vez de "corrigi-la" silenciosamente.

**Persistência em arquivo.** `ReadFile`/`WriteFile` usam, no Java, `ObjectOutputStream`/`ObjectInputStream` e uma classe auxiliar `serializable.AppendingObjectOutputStream` que **não existe em lugar nenhum deste repositório** — ou seja, o `WriteFile.java` original nem compila de forma independente. Na conversão, usei o equivalente idiomático do Python, o módulo `pickle`, com a mesma semântica de "uma lista de objetos gravados em sequência no arquivo" (documentado com uma nota no topo de cada arquivo convertido).

### Exemplo de programa

```
classe Contador {
    int valor = 1;
    proc print() { write(this.valor) },
    proc inc() { this.valor := this.valor + 1 }
};
{ Contador c := new Contador; c.inc(); c.print() }
```
imprime `2`.

### Ambiente de execução

`ContextoExecucaoOO1` guarda, além da pilha de variáveis, um mapa de definições de classe (`Id → DefClasse`), um mapa de objetos vivos (`ValorRef → Objeto`) e um contador de referências (`ValorRef`, incrementado a cada `new`). Um objeto (`Objeto`) é o par (nome da classe, `ContextoObjeto`), e `ContextoObjeto` é apenas um dicionário `Id → Valor` representando os atributos daquela instância — o "heap" da linguagem, essencialmente. Quando um método é chamado (`ChamadaMetodo`), o interpretador cria um **contexto de execução novo** (que compartilha o heap/mapa de classes com o chamador, mas tem pilha de variáveis própria), mapeia `this` para a referência do objeto e executa o procedimento nesse contexto isolado — para que variáveis locais do método chamador não vazem para dentro do método.

### Comando

O comando `New` é o mais elaborado: recupera a definição da classe, cria um ambiente auxiliar só para "elaborar" (`elabora`) os atributos declarados na classe com seus valores iniciais, empacota o resultado num `Objeto`, obtém uma referência nova (`getProxRef()`) e mapeia essa referência para o objeto — finalmente atribuindo essa referência à variável do lado esquerdo do `new`, exatamente como uma atribuição comum.

### Atividades

Implementadas em `python/loo1/plp/orientadaObjetos1/Exemplo1.py` a `Exemplo4.py`.

**Atividades 1 e 2** — classe `Contador` com `inc()`/`print()`, usada por um e por dois objetos independentes:

```
Exemplo1 → 2
Exemplo2 → 2
           3
```

Cada objeto mantém seu próprio estado (`c.inc()` não afeta `c2`), confirmando o isolamento do heap por referência.

**Atividades 3 e 4** — classe `LValor`, uma lista encadeada de inteiros com `insere(int v)` e `print()` (Atividade 3), acrescida de `remove(int v)` (Atividade 4):

```
Exemplo3 (insere 3, insere 4, print):
3
4
-100
```

O `-100` final não é um bug da conversão: é o valor-sentinela (`int valor = -100`) do nó vazio que `insere()` sempre cria como novo `prox` ao inserir o último elemento, e que `print()` imprime porque só verifica `prox == null`, não se o nó é "vazio" — comportamento herdado fielmente do algoritmo tal como especificado no slide.

```
Exemplo4 (insere 2,3,4, print, remove(3), print):
2
3
4
-100
2
4
-100
```

Confirma que `remove(3)` percorre a lista, encontra o nó com `valor == 3` e o desconecta emendando `aux.prox := aux.prox.prox` — a segunda impressão já não contém mais o `3`.

---

## Considerações finais

- As seis linguagens foram convertidas mantendo a arquitetura orientada a objetos original (uma classe por conceito da BNF, hierarquias de herança preservadas), trocando apenas os mecanismos que não têm equivalente direto em Python (interfaces → `ABC`, sobrecarga de método → nomes distintos, exceções *checked* → exceções normais, *casts* → *duck typing*).
- Cada conversão foi testada executando programas de exemplo manualmente construídos (não apenas as atividades pedidas) antes de prosseguir para a linguagem seguinte, e todo o código em `python/` compila (`python -m py_compile`) e importa sem conflitos entre as seis linguagens no mesmo processo.
- Dois achados de implementação valem destaque para quem for revisar o projeto: o **escopo dinâmico** de `lf1` (Atividade 2, seção lf1) e o **erro de tipo intencionalmente preservado** na Atividade 4 de `li2`.
- A única funcionalidade sem equivalente direto em Python foi a serialização binária de objetos (`ReadFile`/`WriteFile` de `loo1`), substituída por `pickle` — funcionalmente equivalente, mas não byte-a-byte compatível com o formato do Java (o que não é um requisito, já que os dois lados nunca precisam trocar arquivos entre si).

### Como executar

```bash
cd python
python3 -m le1.plp.expressions1.Exemplo1
python3 -m le2.plp.expressions2.Exemplo3
python3 -m lf1.plp.functional1.Exemplo2
python3 -m li1.plp.imperative1.Exemplo3
python3 -m li2.plp.imperative2.Exemplo4
python3 -m loo1.plp.orientadaObjetos1.Exemplo4
```
