import PySimpleGUI as sg


class TelaProfessor:
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
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('******** PROFESSORES *******', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção:', font=("Helvica", 15))],
            [sg.Radio('Incluir Professor', "RD1", key='1')],
            [sg.Radio('Alterar Professor', "RD1", key='2')],
            [sg.Radio('Listar Professor', "RD1", key='3')],
            [sg.Radio('Excluir Professor', "RD1", key='4')],
            [sg.Radio('Buscar Professor', "RD1", key='5')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window('Sistema Curso').Layout(layout)

    def pega_dados_professor(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("******** DADOS PROFESSOR ********", font=("Helvica", 25))],
            [sg.Text("Nome:", size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text("CPF:", size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text("Departamento:", size=(15, 1)), sg.InputText('', key='departamento')],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window('Sistema Curso').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        cpf = values['cpf']
        departamento = values['departamento']

        self.close()
        return {"nome": nome, "cpf": cpf, "departamento": departamento}

    def mostra_professor(self, dados_professor):
        string_todos_professores = ''
        for dado in dados_professor:
            string_todos_professores = string_todos_professores + "Nome do professor: " + dado["nome"] + '\n'
            string_todos_professores = string_todos_professores + "CPF do professor: " + str(dado["cpf"]) + '\n'
            string_todos_professores = string_todos_professores + "Departamento do professor: " + str(dado["departamento"]) + '\n\n'

            sg.Popup('******** LISTA DE PROFESSORES DO CURSO ********', string_todos_professores)

    def seleciona_professor(self):
        sg.ChangeLookAndFeel('Dark Brown')
        layout = [
            [sg.Text("******** SELECIONAR PROFESSOR ********", font=("Helvica", 25))],
            [sg.Text("Digite o CPF do professor que deseja selecionar:", font=("Helvica", 25))],
            [sg.Text("CPF:", size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window('Seleciona Professor').Layout(layout)

        button, values = self.open()
        cpf = values['cpf']
        self.close()
        return cpf

    def show_msg(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
