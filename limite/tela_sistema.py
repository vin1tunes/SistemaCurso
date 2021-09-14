import PySimpleGUI as sg


class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
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
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        sg.ChangeLookAndFeel('Dark Brown')
        layout = [
            [sg.Text("******* BEM-VINDO AO CURSO DE SISTEMAS DE INFORMAÇÃO ********", font=("Helvica", 25))],
            [sg.Text("Escolha sua opção:", font=("Helvica", 15))],
            [sg.Radio('Alunos', "RD1", key='1')],
            [sg.Radio('Professores', "RD1", key='2')],
            [sg.Radio('Disciplinas', "RD1", key='3')],
            [sg.Radio('Atividades', "RD1", key='4')],
            [sg.Radio('Atividades Aluno', "RD1", key='5')],
            [sg.Radio('Finalizar Sistema', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Cursos').Layout(layout)
