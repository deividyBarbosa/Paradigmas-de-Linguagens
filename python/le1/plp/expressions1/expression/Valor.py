from abc import ABC

from le1.plp.expressions1.expression.Expressao import Expressao


class Valor(Expressao, ABC):
    """Valor agrupa valores concretos e abstratos."""
