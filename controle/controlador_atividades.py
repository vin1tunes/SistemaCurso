from limite.tela_atividade import TelaAtividade
from entidade.atividade import Atividade
from DAOs.atividade_dao import AtividadeDAO
from Exceptions.atividadeJaExistenteException import AtividadeJaExistenteException


class ControladorAtividades:
    def __init__(self, controlador_sistema):
        self.__atividade_DAO = AtividadeDAO()
        self.__tela_atividade = TelaAtividade()
        self.__controlador_sistema = controlador_sistema

    def pega_atividade_por_titulo(self, titulo: str):
        for atividade in self.__atividade_DAO.get_all():
            if atividade.titulo == titulo:
                return atividade
        return None

    def inclui_atividade(self):
        dados_atividade = self.__tela_atividade.pega_dados_atividade()
        try:
            if self.pega_atividade_por_titulo(dados_atividade["titulo"]) is not None:
                raise AtividadeJaExistenteException
        except AtividadeJaExistenteException as e:
            self.__tela_atividade.show_msg(e)
        else:
            atividade = Atividade(dados_atividade["titulo"], dados_atividade["descricao"],
                                  dados_atividade["prazo"], dados_atividade["status"])
            self.__atividade_DAO.add(atividade)

    def lista_atividades(self):
        dados_atividades = []
        for atividade in self.__atividade_DAO.get_all():
            dados_atividades.append({"titulo": atividade.titulo, "descricao": atividade.descricao,
                                    "prazo": atividade.prazo, "status": atividade.status})
        self.__tela_atividade.mostra_atividade(dados_atividades)

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
            self.__atividade_DAO.update(atividade)
            self.lista_atividades()
        else:
            self.__tela_atividade.show_msg("ATENÇÃO: Atividade não existente.")

    def excluir_atividade(self):
        self.lista_atividades()
        titulo_atividade = self.__tela_atividade.seleciona_atividade()
        atividade = self.pega_atividade_por_titulo(titulo_atividade)

        if atividade is not None:
            self.__atividade_DAO.remove(atividade.titulo)
            self.lista_atividades()
        else:
            self.__tela_atividade.show_msg("ATENÇÃO: Atividade não existente.")

    def find_atividade_by_titulo(self):
        dado_atividade = []
        titulo_atividade = self.__tela_atividade.seleciona_atividade()
        atividade = self.pega_atividade_por_titulo(titulo_atividade)

        if atividade is not None:
            dado_atividade.append({"titulo": atividade.titulo, "descricao": atividade.descricao,
                                  "prazo": atividade.prazo, "status": atividade.status})
            self.__tela_atividade.mostra_atividade(dado_atividade)
        else:
            self.__tela_atividade.show_msg("ATENÇÃO: Atividade não encontrada.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_atividade, 2: self.alterar_atividade, 3: self.lista_atividades,
                        4: self.excluir_atividade, 5: self.find_atividade_by_titulo, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_atividade.tela_opcoes()]()
