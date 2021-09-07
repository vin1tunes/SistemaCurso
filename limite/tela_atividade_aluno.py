import PySimpleGUI as sg


class TelaAtividadeAluno:
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
            [sg.Text('******** ATIVIDADES ALUNO *******', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção:', font=("Helvica", 15))],
            [sg.Radio('Incluir atividade', "RD1", key='1')],
            [sg.Radio('Excluir atividade', "RD1", key='2')],
            [sg.Radio('Alterar atividade', "RD1", key='3')],
            [sg.Radio('Listar todas atividades realizadas', "RD1", key='4')],
            [sg.Radio('Listar todas atividades de um aluno', "RD1", key='5')],
            [sg.Radio('Listar todas atividades de um aluno em uma disciplina', "RD1", key='6')],
            [sg.Radio('Calcular a média de um aluno', "RD1", key='7')],
            [sg.Radio('Buscar atividade de um aluno', "RD1", key='8')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window('Sistema Curso').Layout(layout)

    def pega_dados_atividade_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("******** DADOS ATIVIDADE ALUNO ********", font=("Helvica", 25))],
            [sg.Text("Nota:", size=(20, 1)), sg.InputText('', key='nota')],
            [sg.Text("Data da entrega:", size=(20, 1)), sg.InputText('', key='data_entrega')],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window('Sistema Curso').Layout(layout)

        button, values = self.open()
        nota = values['nota']
        data_entrega = values['data_entrega']

        self.close()
        return {"nota": nota, "data_entrega": data_entrega}

    def mostra_atividade_aluno(self, dados_atividade):
        string_todas_atividades_aluno = ''
        for dado in dados_atividade:
            string_todas_atividades_aluno = string_todas_atividades_aluno + "Nota do aluno: " + dado["nota"] + '\n'
            string_todas_atividades_aluno = string_todas_atividades_aluno + "Data da entrega: " + str(dado["data_entrega"]) + '\n'
            string_todas_atividades_aluno = string_todas_atividades_aluno + "Título da atividade: " + dado["titulo_atividade"] + '\n'
            string_todas_atividades_aluno = string_todas_atividades_aluno + "Descrição da atividade: " + str(dado["descricao_atividade"]) + '\n'
            string_todas_atividades_aluno = string_todas_atividades_aluno + "Prazo da atividade: " + str(dado["prazo"]) + '\n'
            string_todas_atividades_aluno = string_todas_atividades_aluno + "Status da atividade: " + str(dado["status"]) + '\n'
            string_todas_atividades_aluno = string_todas_atividades_aluno + "Nome do aluno: " + str(dado["nome_aluno"]) + '\n'
            string_todas_atividades_aluno = string_todas_atividades_aluno + "Cpf do aluno: " + str(dado["cpf_aluno"]) + '\n'
            string_todas_atividades_aluno = string_todas_atividades_aluno + "Matrícula do aluno: " + str(dado["matricula_aluno"]) + '\n'
            string_todas_atividades_aluno = string_todas_atividades_aluno + "Nome da disciplina: " + str(dado["nome_disciplina"]) + '\n'
            string_todas_atividades_aluno = string_todas_atividades_aluno + "Nome do professor: " + str(dado["nome_professor"]) + '\n'

            sg.Popup('******** LISTA DE TODAS ATIVIDADES DOS ALUNOS ********', string_todas_atividades_aluno)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def seleciona_matricula_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("******** SELECIONAR MATRÍCULA ALUNO ********", font=("Helvica", 25))],
            [sg.Text("Digite a matrícula do aluno que deseja selecionar:", font=("Helvica", 25))],
            [sg.Text("Matrícula:", size=(15, 1)), sg.InputText('', key='matricula')],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window('Seleciona Aluno').Layout(layout)

        button, values = self.open()
        matricula = values['matricula']
        self.close()
        return matricula

    def seleciona_atividade_titulo(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("******** SELECIONAR TÍTULO ATIVIDADE ********", font=("Helvica", 25))],
            [sg.Text("Digite o título da atividade que deseja selecionar:", font=("Helvica", 25))],
            [sg.Text("Título:", size=(15, 1)), sg.InputText('', key='titulo')],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window('Seleciona Atividade').Layout(layout)

        button, values = self.open()
        titulo = values['titulo']
        self.close()
        return titulo

    def seleciona_nome_disciplina(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("******** SELECIONAR DISCIPLINA ********", font=("Helvica", 25))],
            [sg.Text("Digite o nome da disciplina que deseja selecionar:", font=("Helvica", 25))],
            [sg.Text("Nome:", size=(15, 1)), sg.InputText('', key='disciplina')],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window('Seleciona Aluno').Layout(layout)

        button, values = self.open()
        disciplina = values['disciplina']
        self.close()
        return disciplina

    def mostra_media(self, media):
        media_aluno = 'Média igual a: ' + str(media)
        sg.popup('******** MÉDIA DO ALUNO ********', media_aluno)

    def show_msg(self, msg):
        sg.popup("", msg)
