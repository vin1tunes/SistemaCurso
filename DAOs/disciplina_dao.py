from entidade.disciplina import Disciplina
from DAOs.dao import DAO


class DisciplinaDAO(DAO):
    def __init__(self):
        super().__init__('disciplinas.pkl')

    def add(self, disciplina: Disciplina):
        if (disciplina is not None) and isinstance(disciplina, Disciplina) and isinstance(disciplina.nome, str):
            super().add(disciplina.nome, disciplina)

    def update(self, disciplina: Disciplina):
        if (disciplina is not None) and isinstance(disciplina, Disciplina) and isinstance(disciplina.nome, str):
            super().update(disciplina.nome, disciplina)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key):
        if isinstance(key, str):
            return super().remove(key)
