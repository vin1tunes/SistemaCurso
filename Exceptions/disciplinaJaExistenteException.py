class DisciplinaJaExistenteException(Exception):
    def __init__(self):
        super().__init__("Disciplina já existente.")