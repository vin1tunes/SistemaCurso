from entidade.atividade_aluno import AtividadeAluno
from DAOs.dao import DAO


class AtividadeAlunoDAO(DAO):
    def __init__(self):
        super().__init__('atividadesAlunos.pkl')

    def add(self, atividade_aluno: AtividadeAluno):
        if (atividade_aluno is not None) and isinstance(atividade_aluno, AtividadeAluno) and isinstance(atividade_aluno.aluno.matricula, int):
            super().add(atividade_aluno.aluno.matricula, atividade_aluno)

    def update(self, atividade_aluno: AtividadeAluno):
        if (atividade_aluno is not None) and isinstance(atividade_aluno, AtividadeAluno) and isinstance(atividade_aluno.aluno.matricula, int):
            super().update(atividade_aluno.aluno.matricula, atividade_aluno)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key):
        if isinstance(key, int):
            return super().remove(key)
