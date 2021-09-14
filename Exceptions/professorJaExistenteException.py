class ProfessorJaExistenteException(Exception):
    def __init__(self):
        super().__init__("Professor já existente!")
