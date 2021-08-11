from limite.tela_disciplina import TelaDisciplina
from entidade.disciplina import Disciplina


class ControladorDisciplinas:
    def __init__(self, controlador_sistema):
        self.__disciplinas = []
        self.__tela_disciplina = TelaDisciplina()
        self.__controlador_sistema = controlador_sistema

    def pega_disciplina_por_nome(self, nome: str):
        for disciplina in self.__disciplinas:
            if disciplina.nome == nome:
                return disciplina
        return None

    def incluir_disciplina(self):
        dados_disciplina = self.__tela_disciplina.pega_dados_disciplina()
        self.__controlador_sistema.controlador_professores.lista_professores()
        cpf_professor = self.__tela_disciplina.seleciona_cpf_professor()
        professor = self.__controlador_sistema.controlador_professores.pega_professor_por_cpf(cpf_professor)
        disciplina = Disciplina(dados_disciplina["nome"], dados_disciplina["qtd_max_alunos"], professor)
        self.__disciplinas.append(disciplina)

        i = 1
        while i <= int(disciplina.qtd_max_alunos):
            self.__controlador_sistema.controlador_alunos.lista_alunos()
            matricula_aluno = self.__tela_disciplina.seleciona_matricula_aluno()
            aluno = self.__controlador_sistema.controlador_alunos.pega_aluno_por_matricula(matricula_aluno)
            disciplina.inclui_aluno_disciplina(aluno)
            i += 1

        self.__controlador_sistema.controlador_atividades.lista_atividades()
        titulo_atividade = self.__tela_disciplina.seleciona_titulo_atividade()
        atividade = self.__controlador_sistema.controlador_atividades.pega_atividade_por_titulo(titulo_atividade)
        disciplina.inclui_atividade_disciplina(atividade)

        #for j in disciplina.alunos:
        #    self.__tela_disciplina.mostra_aluno_disciplina({"nome": j.nome, "cpf": j.cpf, "matricula": j.matricula})
        #    print('\n')

        #for k in disciplina.atividades:
        #    self.__tela_disciplina.mostra_atividade_disciplina({"titulo": k.titulo, "descricao": k.descricao,
        #                                                        "prazo": k.prazo, "status": k.status})

    def lista_disciplina(self):
        for i in self.__disciplinas:
            self.__tela_disciplina.mostra_disciplina({"nome": i.nome, "qtd_max_alunos": i.qtd_max_alunos,
                                                      "nome_professor": i.professor.nome,
                                                      "cpf_professor": i.professor.cpf,
                                                      "departamento_professor": i.professor.departamento})
            for j in i.alunos:
                self.__tela_disciplina.mostra_aluno_disciplina(
                    {"nome": j.nome, "cpf": j.cpf, "matricula": j.matricula})
                print('\n')

            for k in i.atividades:
                self.__tela_disciplina.mostra_atividade_disciplina({"titulo": k.titulo, "descricao": k.descricao,
                                                                    "prazo": k.prazo, "status": k.status})

    def lista_disciplina_selecionada(self):
        self.lista_disciplina()
        nome_disciplina = self.__tela_disciplina.seleciona_disciplina()
        disciplina = self.pega_disciplina_por_nome(nome_disciplina)

        self.__tela_disciplina.mostra_disciplina({"nome": disciplina.nome, "qtd_max_alunos": disciplina.qtd_max_alunos,
                                                      "nome_professor": disciplina.professor.nome,
                                                      "cpf_professor": disciplina.professor.cpf,
                                                      "departamento_professor": disciplina.professor.departamento})
        for j in disciplina.alunos:
                self.__tela_disciplina.mostra_aluno_disciplina(
                    {"nome": j.nome, "cpf": j.cpf, "matricula": j.matricula})
                print('\n')

        for k in disciplina.atividades:
            self.__tela_disciplina.mostra_atividade_disciplina({"titulo": k.titulo, "descricao": k.descricao,
                                                                    "prazo": k.prazo, "status": k.status})

    def alterar_disciplina(self):
        self.lista_disciplina()
        nome_disciplina = self.__tela_disciplina.seleciona_disciplina()
        disciplina = self.pega_disciplina_por_nome(nome_disciplina)

        if disciplina is not None:
            novos_dados_disciplina = self.__tela_disciplina.pega_dados_disciplina()
            disciplina.nome = novos_dados_disciplina["nome"]
            disciplina.qtd_max_alunos = novos_dados_disciplina["qtd_max_alunos"]
            self.lista_disciplina()
        else:
            self.__tela_disciplina.show_msg("Disciplina não existente.")

    def excluir_disciplina(self):
        self.lista_disciplina()
        nome_disciplina = self.__tela_disciplina.seleciona_disciplina()
        disciplina = self.pega_disciplina_por_nome(nome_disciplina)

        if disciplina is not None:
            self.__disciplinas.remove(disciplina)
            self.lista_disciplina()
        else:
            self.__tela_disciplina.show_msg("Disciplina não existente.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_disciplina, 2: self.excluir_disciplina, 3: self.alterar_disciplina,
                        4: self.lista_disciplina, 5: self.lista_disciplina_selecionada, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_disciplina.tela_opcpes()]()
