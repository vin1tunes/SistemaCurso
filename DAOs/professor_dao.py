from entidade.professor import Professor
from DAOs.dao import DAO


class ProfessorDAO(DAO):
    def __init__(self):
        super().__init__('professores.pkl')

    def add(self, professor: Professor):
        if (professor is not None) and isinstance(professor, Professor) and isinstance(professor.cpf, int):
            super().add(professor.cpf, professor)

    def update(self, professor: Professor):
        if (professor is not None) and isinstance(professor, Professor) and isinstance(professor.cpf, int):
            super().update(professor.cpf, professor)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key):
        if isinstance(key, int):
            return super().remove(key)
