from entidade.abstractPessoa import Pessoa


class Aluno(Pessoa):
    """Representa um aluno.

    atributos: nome, cpf e matrícula
    """

    def __init__(self, nome: str, cpf: int, matricula: int):
        super().__init__(nome, cpf)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
