class Tipo:
    """
    Interface que representa os possiveis tipos de uma expressao.

    Nao usa abc.ABC (que exigiria ABCMeta) porque TipoPrimitivo precisa
    poder herdar de Tipo *e* de enum.Enum ao mesmo tempo; EnumMeta e ABCMeta
    sao metaclasses incompativeis sem uma metaclasse combinada, entao Tipo
    fica como uma classe comum cujos metodos levantam NotImplementedError
    (papel de interface, sem forcar a abstracao via metaclasse).
    """

    def getNome(self) -> str:
        raise NotImplementedError

    def eInteiro(self) -> bool:
        """Indica se este tipo e inteiro."""
        raise NotImplementedError

    def eBooleano(self) -> bool:
        """Indica se este tipo e booleano."""
        raise NotImplementedError

    def eString(self) -> bool:
        """Indica se este tipo e string."""
        raise NotImplementedError

    def eIgual(self, tipo: "Tipo") -> bool:
        """Compara este tipo com o tipo dado. Dois tipos sao iguais se tem o mesmo nome."""
        raise NotImplementedError

    def eValido(self) -> bool:
        """Indica se este tipo e valido. Tipos primitivos sao sempre validos."""
        raise NotImplementedError

    def intersecao(self, outro_tipo: "Tipo") -> "Tipo":
        """Retorna o tipo mais abrangente que engloba este tipo e o tipo dado (ou None se nao houver intersecao)."""
        raise NotImplementedError
