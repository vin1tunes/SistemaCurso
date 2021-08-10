class Atividade:
    """Representa uma atividade.

    atributos: título, descrição, prazo, status.
    """

    def __init__(self, titulo: str, descricao: str, prazo: int, status: str):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__prazo = prazo
        self.__status = status

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def prazo(self):
        return self.__prazo

    @prazo.setter
    def prazo(self, prazo):
        self.__prazo = prazo

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status
