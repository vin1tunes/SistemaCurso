import PySimpleGUI as sg


class TelaAtividade:
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
            [sg.Text('******** ATIVIDADES *******', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção:', font=("Helvica", 15))],
            [sg.Radio('Incluir Atividade', "RD1", key='1')],
            [sg.Radio('Alterar Atividade', "RD1", key='2')],
            [sg.Radio('Listar Atividade', "RD1", key='3')],
            [sg.Radio('Excluir Atividade', "RD1", key='4')],
            [sg.Radio('Buscar Atividade', "RD1", key='5')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window('Sistema Curso').Layout(layout)

    def pega_dados_atividade(self):
        sg.ChangeLookAndFeel('Dark Brown')
        layout = [
            [sg.Text("******** DADOS ATIVIDADE ********", font=("Helvica", 25))],
            [sg.Text("Título:", size=(15, 1)), sg.InputText('', key='titulo')],
            [sg.Text("Descrição:", size=(15, 1)), sg.InputText('', key='descricao')],
            [sg.Text("Prazo:", size=(15, 1)), sg.InputText('', key='prazo')],
            [sg.Text("Status:", size=(15, 1)), sg.InputText('', key='status')],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window('Sistema Curso').Layout(layout)

        button, values = self.open()
        titulo = values['titulo']
        descricao = values['descricao']
        prazo = values['prazo']
        status = values['status']

        self.close()
        return {"titulo": titulo, "descricao": descricao, "prazo": prazo, "status": status}

    def mostra_atividade(self, dados_atividade):
        string_todos_atividades = ''
        for dado in dados_atividade:
            string_todos_atividades = string_todos_atividades + "Título da atividade: " + dado["titulo"] + '\n'
            string_todos_atividades = string_todos_atividades + "Descrição da atividade: " + dado["descricao"] + '\n'
            string_todos_atividades = string_todos_atividades + "Prazo da atividade: " + dado["prazo"] + '\n'
            string_todos_atividades = string_todos_atividades + "Status da atividade: " + dado["status"] + '\n\n'

            sg.Popup('******** LISTA DE ATIVIDADES DO CURSO ********', string_todos_atividades)

    def seleciona_atividade(self):
        sg.ChangeLookAndFeel('Dark Brown')
        layout = [
            [sg.Text("******** SELECIONAR ATIVIDADE ********", font=("Helvica", 25))],
            [sg.Text("Digite o título da atividade que deseja selecionar:", font=("Helvica", 25))],
            [sg.Text("Título:", size=(15, 1)), sg.InputText('', key='titulo')],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window('Seleciona Atividade').Layout(layout)

        button, values = self.open()
        titulo = values['titulo']
        self.close()
        return titulo

    def show_msg(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
