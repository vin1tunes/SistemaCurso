from abc import ABC, abstractmethod


class Pessoa(ABC):
    """Representa uma pessoa.

    atributos: nome, cpf.
    """

    @abstractmethod
    def __init__(self, nome: str, cpf: int):
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
