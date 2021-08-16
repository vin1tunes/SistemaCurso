from limite.tela_aluno import TelaAluno
from entidade.aluno import Aluno


class ControladorAlunos:
    def __init__(self, controlador_sistema):
        self.__alunos = []
        self.__tela_aluno = TelaAluno()
        self.__controlador_sistema = controlador_sistema

    def pega_aluno_por_matricula(self, matricula: int):
        for aluno in self.__alunos:
            if aluno.matricula == matricula:
                return aluno
        return None

    def incluir_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno()
        aluno = Aluno(dados_aluno["nome"], dados_aluno["cpf"], dados_aluno["matricula"])
        self.__alunos.append(aluno)

    def lista_alunos(self):
        for aluno in self.__alunos:
            self.__tela_aluno.mostra_aluno({"nome": aluno.nome, "cpf": aluno.cpf, "matricula": aluno.matricula})

    def alterar_aluno(self):
        self.lista_alunos()
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_matricula(matricula_aluno)

        if aluno is not None:
            novos_dados_aluno = self.__tela_aluno.pega_dados_aluno()
            aluno.nome = novos_dados_aluno["nome"]
            aluno.cpf = novos_dados_aluno["cpf"]
            aluno.matricula = novos_dados_aluno["matricula"]
            self.lista_alunos()
        else:
            self.__tela_aluno.show_msg("Aluno não existente.")

    def excluir_aluno(self):
        self.lista_alunos()
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_matricula(matricula_aluno)

        if aluno is not None:
            self.__alunos.remove(aluno)
            self.lista_alunos()
        else:
            self.__tela_aluno.show_msg("Aluno não existente.")

    def find_student_by_matricula(self):
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_matricula(matricula_aluno)

        if aluno is not None:
            self.__tela_aluno.mostra_aluno({"nome": aluno.nome, "cpf": aluno.cpf, "matricula": aluno.matricula})
        else:
            self.__tela_aluno.show_msg("Aluno não encontrado.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_aluno, 2: self.alterar_aluno, 3: self.lista_alunos, 4: self.excluir_aluno,
                        5: self.find_student_by_matricula, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_aluno.tela_opcoes()]()
