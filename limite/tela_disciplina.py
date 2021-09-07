import PySimpleGUI as sg


class TelaDisciplina:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if values['7']:
            opcao = 7
        if values['8']:
            opcao = 8
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('******** DISCIPLINAS *******', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção:', font=("Helvica", 15))],
            [sg.Radio('Incluir Disciplina', "RD1", key='1')],
            [sg.Radio('Excluir Disciplina', "RD1", key='2')],
            [sg.Radio('Alterar Disciplina', "RD1", key='3')],
            [sg.Radio('Listar todas Disciplinas', "RD1", key='4')],
            [sg.Radio('Listar uma disciplina', "RD1", key='5')],
            [sg.Radio('Buscar por um aluno em uma disciplina', "RD1", key='6')],
            [sg.Radio('Excluir aluno de uma disciplina', "RD1", key='7')],
            [sg.Radio('Buscar uma disciplina', "RD1", key='8')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window('Sistema Curso').Layout(layout)

    def pega_dados_disciplina(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("******** DADOS DISCIPLINA ********", font=("Helvica", 25))],
            [sg.Text("Nome da disciplina:", size=(20, 1)), sg.InputText('', key='nome')],
            [sg.Text("Número máximo de alunos:", size=(20, 1)), sg.InputText('', key='qtd_max_alunos')],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window('Sistema Curso').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        qtd_max_alunos = values['qtd_max_alunos']

        self.close()
        return {"nome": nome, "qtd_max_alunos": qtd_max_alunos}

    def mostra_disciplina(self, dados_disciplina):
        string_todas_disciplinas = ''
        for dado in dados_disciplina:
            string_todas_disciplinas = string_todas_disciplinas + "Nome da disciplina: " + dado["nome"] + '\n'
            string_todas_disciplinas = string_todas_disciplinas + "Quantidade máxima de alunos: " + dado["qtd_max_alunos"] + '\n'
            string_todas_disciplinas = string_todas_disciplinas + "Nome do professor: " + dado["nome_professor"] + '\n'
            string_todas_disciplinas = string_todas_disciplinas + "CPF do professor: " + dado["cpf_professor"] + '\n'
            string_todas_disciplinas = string_todas_disciplinas + "Departamento do professor: " + dado["departamento_professor"] + '\n\n'

        sg.popup("******** LISTA DE DISCIPLINAS DO CURSO ********", string_todas_disciplinas)

    def seleciona_cpf_professor(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("******** SELECIONA CPF PROFESSOR ********", font=("Helvica", 25))],
            [sg.Text("Digite o CPF do professor que deseja selecionar:", font=("Helvica", 25))],
            [sg.Text("CPF:", size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window('Seleciona Professor').Layout(layout)

        button, values = self.open()
        cpf = values['cpf']
        self.close()
        return cpf

    def seleciona_matricula_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("******** SELECIONA MATRÍCULA ALUNO ********", font=("Helvica", 25))],
            [sg.Text("Digite a matrícula do aluno que deseja selecionar:", font=("Helvica", 25))],
            [sg.Text("Matrícula:", size=(15, 1)), sg.InputText('', key='matricula')],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window('Seleciona Aluno').Layout(layout)

        button, values = self.open()
        matricula = values['matricula']
        self.close()
        return matricula

    def atividade_planejada(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("******** QUANTIDADE DE ATIVIDADES ********", font=("Helvica", 25))],
            [sg.Text("Quantidade de atividades planejadas para disciplina", font=("Helvica", 25))],
            [sg.Text("Atividades:", size=(15, 1)), sg.InputText('', key='qtd_atividade')],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window('Seleciona Aluno').Layout(layout)

        button, values = self.open()
        qtd_atividade = values['qtd_atividade']
        self.close()
        return qtd_atividade

    def seleciona_titulo_atividade(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("******** SELECIONA ATIVIDADE ********", font=("Helvica", 25))],
            [sg.Text("Título da atividade que deseja selecionar", font=("Helvica", 25))],
            [sg.Text("Atividade:", size=(15, 1)), sg.InputText('', key='titulo_atividade')],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window('Seleciona Atividade').Layout(layout)

        button, values = self.open()
        titulo_atividade = values['titulo_atividade']
        self.close()
        return titulo_atividade

    def seleciona_disciplina(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("******** SELECIONA DISCIPLINA ********", font=("Helvica", 25))],
            [sg.Text("Nome da disciplina que deseja selecionar", font=("Helvica", 25))],
            [sg.Text("Disciplina:", size=(15, 1)), sg.InputText('', key='nome_disciplina')],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window('Seleciona Disciplina').Layout(layout)

        button, values = self.open()
        nome_disciplina = values['nome_disciplina']
        self.close()
        return nome_disciplina

    def mostra_aluno_disciplina(self, dados_aluno):
        string_todos_alunos = ''
        for dado in dados_aluno:
            string_todos_alunos = string_todos_alunos + "Nome do aluno: " + dado["nome"] + '\n'
            string_todos_alunos = string_todos_alunos + "CPF do aluno: " + str(dado["cpf"]) + '\n'
            string_todos_alunos = string_todos_alunos + "Matrícula do aluno: " + str(dado["matricula"]) + '\n\n'

            sg.Popup('******** LISTA DE ALUNOS DA DISCIPLINA ********', string_todos_alunos)

    def mostra_atividade_disciplina(self, dados_atividade):
        string_todos_atividades = ''
        for dado in dados_atividade:
            string_todos_atividades = string_todos_atividades + "Título da atividade: " + dado["titulo"] + '\n'
            string_todos_atividades = string_todos_atividades + "Descrição da atividade: " + str(dado["descricao"]) + '\n'
            string_todos_atividades = string_todos_atividades + "Prazo da atividade: " + str(dado["prazo"]) + '\n'
            string_todos_atividades = string_todos_atividades + "Status da atividade: " + str(dado["status"]) + '\n\n'

            sg.Popup('******** LISTA DE ATIVIDADES DA DISCIPLINA ********', string_todos_atividades)

    def show_msg(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
