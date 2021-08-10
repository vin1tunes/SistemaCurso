class Curso:
    """Representa um curso.

    atributos: nome, instituição, alunos, professores, disciplinas.
    """

    def __init__(self, nome: str, instituicao: str):
        self.__nome = nome
        self.__instituicao = instituicao
        self.__disciplinas = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def instituicao(self):
        return self.__instituicao

    @instituicao.setter
    def instituicao(self, instituicao):
        self.__instituicao = instituicao

    @property
    def disciplinas(self):
        return self.__disciplinas
