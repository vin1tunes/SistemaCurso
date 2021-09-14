from limite.tela_aluno import TelaAluno
from entidade.aluno import Aluno
from DAOs.aluno_dao import AlunoDAO
from Exceptions.alunoJaExistenteException import AlunoJaExistenteException


class ControladorAlunos:
    def __init__(self, controlador_sistema):
        # self.__alunos = []
        self.__aluno_DAO = AlunoDAO()
        self.__tela_aluno = TelaAluno()
        self.__controlador_sistema = controlador_sistema

    def pega_aluno_por_matricula(self, matricula: int):
        # for aluno in self.__alunos:
        for aluno in self.__aluno_DAO.get_all():
            if aluno.matricula == matricula:
                return aluno
        return None

    def pega_aluno_por_cpf(self, cpf: int):
        # for aluno in self.__alunos:
        for aluno in self.__aluno_DAO.get_all():
            if aluno.cpf == cpf:
                return aluno
        return None

    def incluir_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno()
        try:
            if self.pega_aluno_por_cpf(dados_aluno["cpf"]) != None:
                raise AlunoJaExistenteException
            else:
                aluno = Aluno(dados_aluno["nome"], (dados_aluno["cpf"]), dados_aluno["matricula"])
                self.__aluno_DAO.add(aluno)
        except AlunoJaExistenteException as e:
            self.__tela_aluno.show_msg(e)
        except ValueError as e:
            self.__tela_aluno.show_msg(e)

        # try:
        #    self.__alunos.append(aluno)
        # except AlunoJaExistenteException as e:
        #    print(e)

    def lista_alunos(self):
        dados_alunos = []
        # for aluno in self.__alunos:
        for aluno in self.__aluno_DAO.get_all():
            dados_alunos.append({"nome": aluno.nome, "cpf": aluno.cpf, "matricula": aluno.matricula})
        self.__tela_aluno.mostra_aluno(dados_alunos)

    def alterar_aluno(self):
        self.lista_alunos()
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_matricula(matricula_aluno)

        if aluno is not None:
            novos_dados_aluno = self.__tela_aluno.pega_dados_aluno()
            aluno.nome = novos_dados_aluno["nome"]
            aluno.cpf = novos_dados_aluno["cpf"]
            aluno.matricula = novos_dados_aluno["matricula"]
            self.__aluno_DAO.update(aluno)
            self.lista_alunos()
        else:
            self.__tela_aluno.show_msg("Aluno não existente.")

    def excluir_aluno(self):
        self.lista_alunos()
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_matricula(int(matricula_aluno))

        if aluno is not None:
            # self.__alunos.remove(aluno)
            self.__aluno_DAO.remove(aluno.matricula)
            self.lista_alunos()
        else:
            self.__tela_aluno.show_msg("Aluno não existente.")

    def find_student_by_matricula(self):
        dado_aluno = []
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_matricula(matricula_aluno)

        if aluno is not None:
            dado_aluno.append({"nome": aluno.nome, "cpf": aluno.cpf, "matricula": aluno.matricula})
            self.__tela_aluno.mostra_aluno(dado_aluno)
        else:
            self.__tela_aluno.show_msg("Aluno não encontrado.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_aluno, 2: self.alterar_aluno, 3: self.lista_alunos, 4: self.excluir_aluno,
                        5: self.find_student_by_matricula, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_aluno.tela_opcoes()]()
