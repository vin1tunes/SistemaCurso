from limite.tela_atividade_aluno import TelaAtividadeAluno
from entidade.atividade_aluno import AtividadeAluno


class ControladorAtividadesAluno:
    def __init__(self, controlador_sistema):
        self.__atividades_aluno = []
        self.__tela_atividade_aluno = TelaAtividadeAluno()
        self.__controlar_sistema = controlador_sistema

    def pega_atividade_por_matricula(self, matricula: int):
        for atividade_aluno in self.__atividades_aluno:
            if atividade_aluno.aluno.matricula == matricula:
                return atividade_aluno
        return None

    def incluir_atividade_aluno(self):
        self.__controlar_sistema.controlador_disciplinas.lista_disciplina()
        nome_disciplina = self.__tela_atividade_aluno.seleciona_nome_disciplina()
        disciplina = self.__controlar_sistema.controlador_disciplinas.pega_disciplina_por_nome(nome_disciplina)

        self.__controlar_sistema.controlador_alunos.lista_alunos()
        matricula_aluno = self.__tela_atividade_aluno.seleciona_matricula_aluno()
        aluno = self.__controlar_sistema.controlador_alunos.pega_aluno_por_matricula(matricula_aluno)

        self.__controlar_sistema.controlador_atividades.lista_atividades()
        titulo_atividade = self.__tela_atividade_aluno.seleciona_atividade_titulo()
        atividade = self.__controlar_sistema.controlador_atividades.pega_atividade_por_titulo(titulo_atividade)

        dados_atividade_aluno = self.__tela_atividade_aluno.pega_dados_atividade_aluno()

        atividade_aluno = AtividadeAluno(dados_atividade_aluno["nota"], dados_atividade_aluno["data_entrega"],
                                         atividade, aluno, disciplina)
        self.__atividades_aluno.append(atividade_aluno)

    def lista_atividade_aluno(self):
        dados_atividades = []
        for i in self.__atividades_aluno:
            dados_atividades.append({"nota": i.nota, "data_entrega": i.data_entrega,
                                    "titulo_atividade": i.atividade.titulo,
                                    "descricao_atividade": i.atividade.descricao,
                                    "prazo": i.atividade.prazo,
                                    "status": i.atividade.status,
                                    "nome_aluno": i.aluno.nome,
                                    "cpf_aluno": i.aluno.cpf,
                                    "matricula_aluno": i.aluno.matricula,
                                    "nome_disciplina": i.disciplina.nome,
                                    "nome_professor": i.disciplina.professor.nome})

        self.__tela_atividade_aluno.mostra_atividade_aluno(dados_atividades)

    def lista_atividade_de_um_aluno(self):
        self.__controlar_sistema.controlador_alunos.lista_alunos()
        matricula_aluno = self.__tela_atividade_aluno.seleciona_matricula_aluno()
        dados_atividades = []

        for i in self.__atividades_aluno:
            if i.aluno.matricula == matricula_aluno:
                dados_atividades.append({"nota": i.nota, "data_entrega": i.data_entrega,
                                        "titulo_atividade": i.atividade.titulo,
                                        "descricao_atividade": i.atividade.descricao,
                                        "prazo": i.atividade.prazo,
                                        "status": i.atividade.status,
                                        "nome_aluno": i.aluno.nome,
                                        "cpf_aluno": i.aluno.cpf,
                                        "matricula_aluno": i.aluno.matricula,
                                        "nome_disciplina": i.disciplina.nome,
                                        "nome_professor": i.disciplina.professor.nome})

        self.__tela_atividade_aluno.mostra_atividade_aluno(dados_atividades)

    def lista_atividade_aluno_disciplina(self):
        matricula_aluno = self.__tela_atividade_aluno.seleciona_matricula_aluno()
        nome_disciplina = self.__tela_atividade_aluno.seleciona_nome_disciplina()
        dados_atividades = []

        for i in self.__atividades_aluno:
            if i.aluno.matricula == matricula_aluno and i.disciplina.nome == nome_disciplina:
                dados_atividades.append({"nota": i.nota, "data_entrega": i.data_entrega,
                                        "titulo_atividade": i.atividade.titulo,
                                        "descricao_atividade": i.atividade.descricao,
                                        "prazo": i.atividade.prazo,
                                        "status": i.atividade.status,
                                        "nome_aluno": i.aluno.nome,
                                        "cpf_aluno": i.aluno.cpf,
                                        "matricula_aluno": i.aluno.matricula,
                                        "nome_disciplina": i.disciplina.nome,
                                        "nome_professor": i.disciplina.professor.nome})

        self.__tela_atividade_aluno.mostra_atividade_aluno(dados_atividades)

    def media_disciplina(self):
        matricula_aluno = self.__tela_atividade_aluno.seleciona_matricula_aluno()
        nome_disciplina = self.__tela_atividade_aluno.seleciona_nome_disciplina()

        soma_das_notas = 0
        counter = 0

        for i in self.__atividades_aluno:
            if i.aluno.matricula == matricula_aluno and i.disciplina.nome == nome_disciplina:
                soma_das_notas += int(i.nota)
                counter += 1
        media = soma_das_notas / counter
        self.__tela_atividade_aluno.mostra_media(media)

    def alterar_atividade_aluno(self):
        self.lista_atividade_aluno()
        matricula_aluno = self.__tela_atividade_aluno.seleciona_matricula_aluno()
        atividade_aluno = self.pega_atividade_por_matricula(matricula_aluno)

        if atividade_aluno is not None:
            novos_dados_atividade_aluno = self.__tela_atividade_aluno.pega_dados_atividade_aluno()
            atividade_aluno.nota = novos_dados_atividade_aluno["nota"]
            atividade_aluno.data_entrega = novos_dados_atividade_aluno["data_entrega"]
            self.lista_atividade_aluno()
        else:
            self.__tela_atividade_aluno.show_msg("Atividade do aluno não encontrada.")

    def excluir_atividade_aluno(self):
        self.lista_atividade_aluno()
        matricula_aluno = self.__tela_atividade_aluno.seleciona_matricula_aluno()
        atividade_aluno = self.pega_atividade_por_matricula(matricula_aluno)

        if atividade_aluno is not None:
            self.__atividades_aluno.remove(atividade_aluno)
            self.lista_atividade_aluno()
        else:
            self.__tela_atividade_aluno.show_msg("Atividade não encontrada.")

    def find_atividade_aluno(self):
        matricula_aluno = self.__tela_atividade_aluno.seleciona_matricula_aluno()
        titulo_atividade = self.__tela_atividade_aluno.seleciona_atividade_titulo()
        dados_atividade = []

        for i in self.__atividades_aluno:
            if i.atividade.titulo == titulo_atividade and i.aluno.matricula == matricula_aluno:
                dados_atividade.append({"nota": i.nota, "data_entrega": i.data_entrega,
                                        "titulo_atividade": i.atividade.titulo,
                                        "descricao_atividade": i.atividade.descricao,
                                        "prazo": i.atividade.prazo,
                                        "status": i.atividade.status,
                                        "nome_aluno": i.aluno.nome,
                                        "cpf_aluno": i.aluno.cpf,
                                        "matricula_aluno": i.aluno.matricula,
                                        "nome_disciplina": i.disciplina.nome,
                                        "nome_professor": i.disciplina.professor.nome})

        self.__tela_atividade_aluno.mostra_atividade_aluno(dados_atividade)

    def retornar(self):
        self.__controlar_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_atividade_aluno, 2: self.excluir_atividade_aluno,
                        3: self.alterar_atividade_aluno, 4: self.lista_atividade_aluno,
                        5: self.lista_atividade_de_um_aluno, 6: self.lista_atividade_aluno_disciplina,
                        7: self.media_disciplina, 8: self.find_atividade_aluno, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_atividade_aluno.tela_opcoes()]()
