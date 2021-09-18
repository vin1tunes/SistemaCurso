from limite.tela_professor import TelaProfessor
from entidade.professor import Professor
from DAOs.professor_dao import ProfessorDAO
from Exceptions.professorJaExistenteException import ProfessorJaExistenteException


class ControladorProfessores:
    def __init__(self, controlador_sistema):
        self.__professor_DAO = ProfessorDAO()
        self.__tela_professor = TelaProfessor()
        self.__controlador_sistema = controlador_sistema

    def pega_professor_por_cpf(self, cpf: int):
        for professor in self.__professor_DAO.get_all():
            if professor.cpf == cpf:
                return professor
        return None

    def incluir_professor(self):
        dados_professor = self.__tela_professor.pega_dados_professor()
        if dados_professor is not None:
            try:
                if self.pega_professor_por_cpf(dados_professor["cpf"]) is not None:
                    raise ProfessorJaExistenteException
            except ProfessorJaExistenteException as e:
                self.__tela_professor.show_msg(e)
            else:
                professor = Professor(dados_professor["nome"], dados_professor["cpf"], dados_professor["departamento"])
                self.__professor_DAO.add(professor)

    def lista_professores(self):
        dados_professores = []
        for professor in self.__professor_DAO.get_all():
            dados_professores.append({"nome": professor.nome, "cpf": professor.cpf, "departamento": professor.departamento})

        self.__tela_professor.mostra_professor(dados_professores)

    def alterar_professor(self):
        self.lista_professores()
        cpf_professor = self.__tela_professor.seleciona_professor()
        professor = self.pega_professor_por_cpf(cpf_professor)

        if professor is not None:
            novos_dados_professor = self.__tela_professor.pega_dados_professor()
            professor.nome = novos_dados_professor["nome"]
            professor.cpf = novos_dados_professor["cpf"]
            professor.departamento = novos_dados_professor["departamento"]
            self.__professor_DAO.update(professor)
            self.lista_professores()
        else:
            self.__tela_professor.show_msg("ATENÇÃO: Professor não existente.")

    def excluir_professor(self):
        self.lista_professores()
        cpf_professor = self.__tela_professor.seleciona_professor()
        professor = self.pega_professor_por_cpf(cpf_professor)

        if professor is not None:
            self.__professor_DAO.remove(professor.cpf)
            self.lista_professores()
        else:
            self.__tela_professor.show_msg("ATENÇÃO: Professor não existente.")

    def find_professor(self):
        dado_professor = []
        cpf_professor = self.__tela_professor.seleciona_professor()
        professor = self.pega_professor_por_cpf(cpf_professor)

        if professor is not None:
            dado_professor.append({"nome": professor.nome, "cpf": professor.cpf, "departamento": professor.departamento})
            self.__tela_professor.mostra_professor(dado_professor)
        else:
            self.__tela_professor.show_msg("ATENÇÃO: Professor não encontrado.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_professor, 2: self.alterar_professor, 3: self.lista_professores,
                        4: self.excluir_professor, 5: self.find_professor, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_professor.tela_opcoes()]()
