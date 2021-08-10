from limite.tela_curso import TelaCurso
from entidade.curso import Curso


class ControladorCursos:
    def __init__(self, controlador_sistema):
        self.__cursos = []
        self.__tela_curso = TelaCurso()
        self.__controlador_sistema = controlador_sistema

    def pega_curso_por_nome(self, nome_curso: str):
        for curso in self.__cursos:
            if curso.nome == nome_curso:
                return curso
        return None

    def incluir_curso(self):
        dados_curso = self.__tela_curso.pega_dados_curso()
        self.__controlador_sistema.controlador_disciplinas.lista_disciplina()
        curso = Curso(dados_curso["nome"], dados_curso["instituicao"])
        nome_disciplina = self.__tela_curso.seleciona_disciplina_curso()
        disciplina = self.__controlador_sistema.controlador_disciplinas.pega_disciplina_por_nome(nome_disciplina)
        curso.disciplinas.append(disciplina)

        self.__cursos.append(curso)

    def lista_cursos(self):
        for i in self.__cursos:
            self.__tela_curso.mostra_curso({"nome": i.nome, "instituicao": i.instituicao})

    def alterar_curso(self):
        self.lista_cursos()
        nome_curso = self.__tela_curso.seleciona_curso()
        curso = self.pega_curso_por_nome(nome_curso)

        if curso is not None:
            novos_dados_curso = self.__tela_curso.pega_dados_curso()
            curso.nome = novos_dados_curso["nome"]
            curso.instituicao = novos_dados_curso["instituicao"]
            self.lista_cursos()
        else:
            self.__tela_curso.show_msg("Curso não existente.")

    def excluir_curso(self):
        self.lista_cursos()
        nome_curso = self.__tela_curso.seleciona_curso()
        curso = self.pega_curso_por_nome(nome_curso)

        if curso is not None:
            self.__cursos.remove(curso)
            self.lista_cursos()
        else:
            self.__tela_curso.show_msg("Curso não existente.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_curso, 2: self.excluir_curso, 3: self.alterar_curso, 4: self.lista_cursos,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_curso.tela_opcoes()]()
