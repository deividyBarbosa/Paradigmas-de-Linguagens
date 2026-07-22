from abc import ABC

from le2.plp.expressions2.expression.Expressao import Expressao


class Valor(Expressao, ABC):
    """Valor agrupa valores concretos e abstratos."""
