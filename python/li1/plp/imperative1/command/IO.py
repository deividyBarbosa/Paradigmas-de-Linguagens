from abc import ABC

from li1.plp.imperative1.command.Comando import Comando


class IO(Comando, ABC):
    """Marca comandos de entrada/saida (Read, Write)."""
