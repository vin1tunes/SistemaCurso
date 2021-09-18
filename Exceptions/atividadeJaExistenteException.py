class AtividadeJaExistenteException(Exception):
    def __init__(self):
        super().__init__("Atividade já existente.")
