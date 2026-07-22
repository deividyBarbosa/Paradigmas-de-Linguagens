"""
Atividade 2 (Lab 06 - loo1).

Reaproveita a classe Contador (Atividade 1) e executa:
  { Contador c := new Contador,
    Contador c2:= new Contador;
    c.inc();
    c2.inc();
    c2.inc();
    c.print();
    c2.print()
  }
"""
from loo1.plp.orientadaObjetos1.comando.ChamadaMetodo import ChamadaMetodo
from loo1.plp.orientadaObjetos1.comando.ComDeclaracao import ComDeclaracao
from loo1.plp.orientadaObjetos1.comando.Sequencial import Sequencial
from loo1.plp.orientadaObjetos1.declaracao.variavel.CompostaDecVariavel import CompostaDecVariavel
from loo1.plp.orientadaObjetos1.declaracao.variavel.DecVariavelObjeto import DecVariavelObjeto
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
from loo1.plp.orientadaObjetos1.expressao.ListaExpressao import ListaExpressao
from loo1.plp.orientadaObjetos1.Exemplo1 import classe_contador
from loo1.plp.orientadaObjetos1.memoria.ContextoCompilacaoOO1 import ContextoCompilacaoOO1
from loo1.plp.orientadaObjetos1.memoria.ContextoExecucaoOO1 import ContextoExecucaoOO1
from loo1.plp.orientadaObjetos1.memoria.colecao.ListaValor import ListaValor
from loo1.plp.orientadaObjetos1.Programa import Programa
from loo1.plp.orientadaObjetos1.util.TipoClasse import TipoClasse


class Exemplo2:

    @staticmethod
    def main():
        dec_classe, id_contador = classe_contador()

        id_c = Id("c")
        id_c2 = Id("c2")
        declaracoes = CompostaDecVariavel(
            DecVariavelObjeto(TipoClasse(id_contador), id_c, id_contador),
            DecVariavelObjeto(TipoClasse(id_contador), id_c2, id_contador),
        )

        comando = ComDeclaracao(
            declaracoes,
            Sequencial(
                ChamadaMetodo(id_c, Id("inc"), ListaExpressao()),
                Sequencial(
                    ChamadaMetodo(id_c2, Id("inc"), ListaExpressao()),
                    Sequencial(
                        ChamadaMetodo(id_c2, Id("inc"), ListaExpressao()),
                        Sequencial(
                            ChamadaMetodo(id_c, Id("print"), ListaExpressao()),
                            ChamadaMetodo(id_c2, Id("print"), ListaExpressao()),
                        ),
                    ),
                ),
            ),
        )
        programa = Programa(dec_classe, comando)

        if programa.checaTipo(ContextoCompilacaoOO1(ListaValor())):
            # Write ja imprime cada valor no momento da execucao (como no
            # Java original); nao repetimos a impressao aqui.
            programa.executar(ContextoExecucaoOO1(entrada=ListaValor()))
        else:
            print("Programa mal tipado.")


if __name__ == "__main__":
    Exemplo2.main()
