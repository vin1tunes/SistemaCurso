from limite.tela_sistema import TelaSistema
from controle.controlador_alunos import ControladorAlunos
from controle.controlador_professores import ControladorProfessores
from controle.controlador_disciplinas import ControladorDisciplinas
from controle.controlador_atividades import ControladorAtividades
from controle.controlador_atividades_aluno import ControladorAtividadesAluno
from controle.controlador_cursos import ControladorCursos


class ControladorSistema:
    def __init__(self):
        self.__controlador_alunos = ControladorAlunos(self)
        self.__controlador_professores = ControladorProfessores(self)
        self.__controlador_disciplinas = ControladorDisciplinas(self)
        self.__controlador_atividades = ControladorAtividades(self)
        self.__controlador_atividades_aluno = ControladorAtividadesAluno(self)
        self.__controlador_cursos = ControladorCursos(self)
        self.__tela_sistema = TelaSistema()


    @property
    def controlador_alunos(self):
        return self.__controlador_alunos

    @property
    def controlador_professores(self):
        return self.__controlador_professores

    @property
    def controlador_disciplinas(self):
        return self.__controlador_disciplinas

    @property
    def controlador_atividades(self):
        return self.__controlador_atividades

    @property
    def controlador_atividades_aluno(self):
        return self.__controlador_atividades_aluno

    @property
    def controlador_cursos(self):
        return self.controlador_cursos

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_alunos(self):
        self.__controlador_alunos.abre_tela()

    def cadastra_professores(self):
        self.__controlador_professores.abre_tela()

    def cadastra_disciplinas(self):
        self.__controlador_disciplinas.abre_tela()

    def cadastra_atividades(self):
        self.__controlador_atividades.abre_tela()

    def cadastra_atividade_aluno(self):
        self.__controlador_atividades_aluno.abre_tela()

    def cadastra_curso(self):
        self.__controlador_cursos.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_alunos, 2: self.cadastra_professores, 3: self.cadastra_disciplinas,
                        4: self.cadastra_atividades, 5: self.cadastra_atividade_aluno,
                        6: self.cadastra_curso, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
