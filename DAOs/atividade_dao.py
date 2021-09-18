from entidade.atividade import Atividade
from DAOs.dao import DAO


class AtividadeDAO(DAO):
    def __init__(self):
        super().__init__('atividades.pkl')

    def add(self, atividade: Atividade):
        if (atividade is not None) and isinstance(atividade, Atividade) and isinstance(atividade.titulo, str):
            super().add(atividade.titulo, atividade)

    def update(self, atividade: Atividade):
        if (atividade is not None) and isinstance(atividade, Atividade) and isinstance(atividade.titulo, str):
            super().update(atividade.titulo, atividade)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key):
        if isinstance(key, str):
            return super().remove(key)
