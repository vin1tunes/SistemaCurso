from entidade.aluno import Aluno
from entidade.atividade import Atividade
from entidade.disciplina import Disciplina


class AtividadeAluno:
    """Representa a atividade do aluno.

    atributos: nota, data_entrega, Aluno.
    """

    def __init__(self, nota: int, data_entrega: int, atividade: Atividade, aluno: Aluno, disciplina: Disciplina):
        self.__nota = nota
        self.__data_entrega = data_entrega
        self.__atividade = atividade
        self.__aluno = aluno
        self.__disciplina = disciplina

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nota):
        self.__nota = nota

    @property
    def data_entrega(self):
        return self.__data_entrega

    @data_entrega.setter
    def data_entrega(self, data_entrega):
        self.__data_entrega = data_entrega

    @property
    def atividade(self):
        return self.__atividade

    @property
    def aluno(self):
        return self.__aluno

    @property
    def disciplina(self):
        return self.__disciplina
