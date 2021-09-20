from limite.tela_disciplina import TelaDisciplina
from entidade.disciplina import Disciplina
from DAOs.disciplina_dao import DisciplinaDAO
from Exceptions.disciplinaJaExistenteException import DisciplinaJaExistenteException


class ControladorDisciplinas:
    def __init__(self, controlador_sistema):
        self.__disciplina_DAO = DisciplinaDAO()
        self.__tela_disciplina = TelaDisciplina()
        self.__controlador_sistema = controlador_sistema

    def pega_disciplina_por_nome(self, nome: str):
        for disciplina in self.__disciplina_DAO.get_all():
            if disciplina.nome == nome:
                return disciplina
        return None

    def incluir_disciplina(self):
        dados_disciplina = self.__tela_disciplina.pega_dados_disciplina()
        if dados_disciplina is not None:
            try:
                if self.pega_disciplina_por_nome(dados_disciplina["nome"]) is not None:
                    raise DisciplinaJaExistenteException
            except DisciplinaJaExistenteException as e:
                self.__tela_disciplina.show_msg(e)
            else:
                self.__controlador_sistema.controlador_professores.lista_professores()
                cpf_professor = self.__tela_disciplina.seleciona_cpf_professor()
                professor = self.__controlador_sistema.controlador_professores.pega_professor_por_cpf(cpf_professor)
                disciplina = Disciplina(dados_disciplina["nome"], dados_disciplina["qtd_max_alunos"], professor)

        i = 1
        while i <= int(disciplina.qtd_max_alunos):
            self.__controlador_sistema.controlador_alunos.lista_alunos()
            matricula_aluno = self.__tela_disciplina.seleciona_matricula_aluno()
            aluno = self.__controlador_sistema.controlador_alunos.pega_aluno_por_matricula(matricula_aluno)
            disciplina.inclui_aluno_disciplina(aluno)
            i += 1

        j = 1
        k = self.__tela_disciplina.atividade_planejada()
        while j <= int(k):
            self.__controlador_sistema.controlador_atividades.lista_atividades()
            titulo_atividade = self.__tela_disciplina.seleciona_titulo_atividade()
            atividade = self.__controlador_sistema.controlador_atividades.pega_atividade_por_titulo(titulo_atividade)
            disciplina.inclui_atividade_disciplina(atividade)
            j += 1

        self.__disciplina_DAO.add(disciplina)
        self.__tela_disciplina.show_msg("Disciplina cadastrada com sucesso!")

    def lista_disciplina(self):
        dados_disciplinas = []
        for i in self.__disciplina_DAO.get_all():
            dados_disciplinas.append({"nome": i.nome, "qtd_max_alunos": i.qtd_max_alunos,
                                     "nome_professor": i.professor.nome,
                                      "cpf_professor": i.professor.cpf,
                                      "departamento_professor": i.professor.departamento})
        self.__tela_disciplina.mostra_disciplina(dados_disciplinas)

    def lista_disciplina_selecionada(self):
        self.lista_disciplina()
        nome_disciplina = self.__tela_disciplina.seleciona_disciplina()
        disciplina = self.pega_disciplina_por_nome(nome_disciplina)
        dados_disciplina = []

        dados_disciplina.append({"nome": disciplina.nome, "qtd_max_alunos": disciplina.qtd_max_alunos,
                                "nome_professor": disciplina.professor.nome,
                                "cpf_professor": disciplina.professor.cpf,
                                "departamento_professor": disciplina.professor.departamento})
        self.__tela_disciplina.mostra_disciplina(dados_disciplina)

        dados_aluno = []
        for i in disciplina.alunos:
            dados_aluno.append({"nome": i.nome, "cpf": i.cpf, "matricula": i.matricula})

        self.__tela_disciplina.mostra_aluno_disciplina(dados_aluno)

        dados_atividade = []
        for k in disciplina.atividades:
            dados_atividade.append({"titulo": k.titulo, "descricao": k.descricao,
                                    "prazo": k.prazo, "status": k.status})

        self.__tela_disciplina.mostra_atividade_disciplina(dados_atividade)

    def alterar_disciplina(self):
        self.lista_disciplina()
        nome_disciplina = self.__tela_disciplina.seleciona_disciplina()
        disciplina = self.pega_disciplina_por_nome(nome_disciplina)

        if disciplina is not None:
            novos_dados_disciplina = self.__tela_disciplina.pega_dados_disciplina()
            disciplina.nome = novos_dados_disciplina["nome"]
            disciplina.qtd_max_alunos = novos_dados_disciplina["qtd_max_alunos"]
            self.__disciplina_DAO.update(disciplina)
            self.lista_disciplina()
        else:
            self.__tela_disciplina.show_msg("Disciplina não existente.")

    def excluir_disciplina(self):
        self.lista_disciplina()
        nome_disciplina = self.__tela_disciplina.seleciona_disciplina()
        disciplina = self.pega_disciplina_por_nome(nome_disciplina)

        if disciplina is not None:
            self.__disciplina_DAO.remove(disciplina.nome)
            self.__tela_disciplina.show_msg("Disciplina removida com sucesso!")
            self.lista_disciplina()
        else:
            self.__tela_disciplina.show_msg("Disciplina não existente.")

    def find_subject(self):
        nome_disciplina = self.__tela_disciplina.seleciona_disciplina()
        disciplina = self.pega_disciplina_por_nome(nome_disciplina)
        dados_disciplina = []

        if disciplina is None:
            self.__tela_disciplina.show_msg("Disciplina não encontrada.")
        else:
            dados_disciplina.append({"nome": disciplina.nome, "qtd_max_alunos": disciplina.qtd_max_alunos,
                                     "nome_professor": disciplina.professor.nome,
                                     "cpf_professor": disciplina.professor.cpf,
                                     "departamento_professor": disciplina.professor.departamento})
            self.__tela_disciplina.mostra_disciplina(dados_disciplina)

    def find_student_by_subject(self):
        self.lista_disciplina()
        nome_disciplina = self.__tela_disciplina.seleciona_disciplina()
        disciplina = self.pega_disciplina_por_nome(nome_disciplina)

        matricula_aluno = self.__tela_disciplina.seleciona_matricula_aluno()

        dados_aluno = []
        for i in disciplina.alunos:
            if i.matricula == matricula_aluno:
                dados_aluno.append({"nome": i.nome, "cpf": i.cpf, "matricula": i.matricula})
        self.__tela_disciplina.mostra_aluno_disciplina(dados_aluno)

    def excluir_aluno_disciplina(self):
        self.lista_disciplina()
        nome_disciplina = self.__tela_disciplina.seleciona_disciplina()
        disciplina = self.pega_disciplina_por_nome(nome_disciplina)

        matricula_aluno = self.__tela_disciplina.seleciona_matricula_aluno()
        aluno = self.__controlador_sistema.controlador_alunos.pega_aluno_por_matricula(matricula_aluno)
        disciplina.alunos.remove(aluno)
        self.__tela_disciplina.show_msg("Aluno removido com sucesso!")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_disciplina, 2: self.excluir_disciplina, 3: self.alterar_disciplina,
                        4: self.lista_disciplina, 5: self.lista_disciplina_selecionada, 6: self.find_student_by_subject,
                        7: self.excluir_aluno_disciplina, 8: self.find_subject, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_disciplina.tela_opcoes()]()
