from entidade.abstractPessoa import Pessoa


class Professor(Pessoa):
    """Representa um professor.

    atributos: nome, cpf, departamento.
    """

    def __init__(self, nome: str, cpf: int, departamento: str):
        super().__init__(nome, cpf)
        self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, departamento):
        self.__departamento = departamento
