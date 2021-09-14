class AlunoJaExistenteException(Exception):
    def __init__(self):
        super().__init__("Aluno já existente!")