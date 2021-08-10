from entidade.professor import Professor
from entidade.aluno import Aluno
from entidade.atividade import Atividade


class Disciplina:
    """Representa uma disciplina.

    aatributos: nome, qtd_max_alunos, professore, alunos, atividades.
    """

    def __init__(self, nome: str, qtd_max_alunos: int, professor: Professor):
        self.__nome = nome
        self.__qtd_max_alunos = qtd_max_alunos
        self.__professor = professor
        self.__alunos = []
        self.__atividades = []

    def inclui_aluno_disciplina(self, aluno: Aluno):
        if isinstance(aluno, Aluno):
            self.__alunos.append(aluno)

    def inclui_atividade_disciplina(self, atividade: Atividade):
        if isinstance(atividade, Atividade):
            self.__atividades.append(atividade)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def qtd_max_alunos(self):
        return self.__qtd_max_alunos

    @qtd_max_alunos.setter
    def qtd_max_alunos(self, qtd_max_alunos):
        self.__qtd_max_alunos = qtd_max_alunos

    @property
    def professor(self):
        return self.__professor

    @property
    def alunos(self):
        return self.__alunos

    @property
    def atividades(self):
        return self.__atividades
