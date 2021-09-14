import PySimpleGUI as sg


class TelaAluno:
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
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('Dark Brown')
        layout = [
            [sg.Text('******** ALUNOS *******', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção:', font=("Helvica", 15))],
            [sg.Radio('Incluir Aluno', "RD1", key='1')],
            [sg.Radio('Alterar Aluno', "RD1", key='2')],
            [sg.Radio('Listar Alunos', "RD1", key='3')],
            [sg.Radio('Excluir Aluno', "RD1", key='4')],
            [sg.Radio('Buscar Aluno', "RD1", key='5')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window('Sistema Curso').Layout(layout)

    def pega_dados_aluno(self):
        sg.ChangeLookAndFeel('Dark Brown')
        layout = [
            [sg.Text("******** DADOS ALUNO ********", font=("Helvica", 25))],
            [sg.Text("Nome:", size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text("CPF:", size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text("Matrícula:", size=(15, 1)), sg.InputText('', key='matricula')],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window('Sistema Curso').Layout(layout)

        button, values = self.open()

        try:
            nome = values['nome']
            cpf = int(values['cpf'])
            matricula = int(values['matricula'])
            return {"nome": nome, "cpf": cpf, "matricula": matricula}
        except ValueError as e:
            self.show_msg(e)

        #finally:
        #    self.close()



        # self.close()
        # return {"nome": nome, "cpf": cpf, "matricula": matricula}

    def mostra_aluno(self, dados_aluno):
        string_todos_alunos = ''
        for dado in dados_aluno:
            string_todos_alunos = string_todos_alunos + "Nome do aluno: " + dado["nome"] + '\n'
            string_todos_alunos = string_todos_alunos + "CPF do aluno: " + str(dado["cpf"]) + '\n'
            string_todos_alunos = string_todos_alunos + "Matrícula do aluno: " + str(dado["matricula"]) + '\n\n'

            sg.Popup('******** LISTA DE ALUNOS DO CURSO ********', string_todos_alunos)

    def seleciona_aluno(self):
        sg.ChangeLookAndFeel('Dark Brown')
        layout = [
            [sg.Text("******** SELECIONAR ALUNO ********", font=("Helvica", 25))],
            [sg.Text("Digite a matrícula do aluno que deseja selecionar:", font=("Helvica", 25))],
            [sg.Text("Matrícula:", size=(15, 1)), sg.InputText('', key='matricula')],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window('Seleciona Aluno').Layout(layout)

        button, values = self.open()
        matricula = values['matricula']
        self.close()
        return matricula

    def show_msg(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
