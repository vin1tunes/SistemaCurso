from limite.tela_professor import TelaProfessor
from entidade.professor import Professor


class ControladorProfessores:
    def __init__(self, controlador_sistema):
        self.__professores = []
        self.__tela_professor = TelaProfessor()
        self.__controlador_sistema = controlador_sistema

    def pega_professor_por_cpf(self, cpf: int):
        for professor in self.__professores:
            if professor.cpf == cpf:
                return professor
        return None

    def incluir_professor(self):
        dados_professor = self.__tela_professor.pega_dados_professor()
        professor = Professor(dados_professor["nome"], dados_professor["cpf"], dados_professor["departamento"])
        self.__professores.append(professor)

    def lista_professores(self):
        for professor in self.__professores:
            self.__tela_professor.mostra_professor({"nome": professor.nome, "cpf": professor.cpf,
                                                    "departamento": professor.departamento})

    def alterar_professor(self):
        self.lista_professores()
        cpf_professor = self.__tela_professor.seleciona_professor()
        professor = self.pega_professor_por_cpf(cpf_professor)

        if professor is not None:
            novos_dados_professor = self.__tela_professor.pega_dados_professor()
            professor.nome = novos_dados_professor["nome"]
            professor.cpf = novos_dados_professor["cpf"]
            professor.departamento = novos_dados_professor["departamento"]
            self.lista_professores()
        else:
            self.__tela_professor.show_msg("Professor não existente.")

    def excluir_professor(self):
        self.lista_professores()
        cpf_professor = self.__tela_professor.seleciona_professor()
        professor = self.pega_professor_por_cpf(cpf_professor)

        if professor is not None:
            self.__professores.remove(professor)
            self.lista_professores()
        else:
            self.__tela_professor.show_msg("Professor não existente.")

    def find_professor(self):
        cpf_professor = self.__tela_professor.seleciona_professor()
        professor = self.pega_professor_por_cpf(cpf_professor)

        if professor is not None:
            self.__tela_professor.mostra_professor({"nome": professor.nome, "cpf": professor.cpf,
                                                    "departamento": professor.departamento})
        else:
            self.__tela_professor.show_msg("Professor não encontrado.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_professor, 2: self.alterar_professor, 3: self.lista_professores,
                        4: self.excluir_professor, 5: self.find_professor, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_professor.tela_opcoes()]()
