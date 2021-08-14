from limite.tela_atividade import TelaAtividade
from entidade.atividade import Atividade


class ControladorAtividades:
    def __init__(self, controlador_sistema):
        self.__atividades = []
        self.__tela_atividade = TelaAtividade()
        self.__controlador_sistema = controlador_sistema

    def pega_atividade_por_titulo(self, titulo: str):
        for atividade in self.__atividades:
            if atividade.titulo == titulo:
                return atividade
        return None

    def inclui_atividade(self):
        dados_atividade = self.__tela_atividade.pega_dados_atividade()
        atividade = Atividade(dados_atividade["titulo"], dados_atividade["descricao"],
                              dados_atividade["prazo"], dados_atividade["status"])
        self.__atividades.append(atividade)

    def lista_atividades(self):
        for atividade in self.__atividades:
            self.__tela_atividade.mostra_atividade({"titulo": atividade.titulo, "descricao": atividade.descricao,
                                                    "prazo": atividade.prazo, "status": atividade.status})

    def alterar_atividade(self):
        self.lista_atividades()
        titulo_atividade = self.__tela_atividade.seleciona_atividade()
        atividade = self.pega_atividade_por_titulo(titulo_atividade)

        if atividade is not None:
            novos_dados_atividade = self.__tela_atividade.pega_dados_atividade()
            atividade.titulo = novos_dados_atividade["titulo"]
            atividade.descricao = novos_dados_atividade["descricao"]
            atividade.prazo = novos_dados_atividade["prazo"]
            atividade.status = novos_dados_atividade["status"]
            self.lista_atividades()
        else:
            self.__tela_atividade.show_msg("Atividade não existente.")

    def excluir_atividade(self):
        self.lista_atividades()
        titulo_atividade = self.__tela_atividade.seleciona_atividade()
        atividade = self.pega_atividade_por_titulo(titulo_atividade)

        if atividade is not None:
            self.__atividades.remove(atividade)
            self.lista_atividades()
        else:
            self.__tela_atividade.show_msg("Atividade não existente.")

    def find_atividade_by_titulo(self):
        titulo_atividade = self.__tela_atividade.seleciona_atividade()

        for atividade in self.__atividades:
            if atividade.titulo == titulo_atividade:
                self.__tela_atividade.mostra_atividade({"titulo": atividade.titulo, "descricao": atividade.descricao,
                                                        "prazo": atividade.prazo, "status": atividade.status})

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_atividade, 2: self.alterar_atividade, 3: self.lista_atividades,
                        4: self.excluir_atividade, 5: self.find_atividade_by_titulo, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_atividade.tela_opcoes()]()
