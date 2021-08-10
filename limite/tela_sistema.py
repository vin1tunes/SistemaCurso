class TelaSistema:
    def tela_opcoes(self):
        print("******** BEM-VINDO AO CURSO DE SISTEMAS DE INFORMAÇÃO ********")
        print("Selecione o que deseja acessar: ")
        print("1 - Alunos")
        print("2 - Professores")
        print("3 - Disciplinas")
        print("4 - Atividades")
        print("5 - Atividades Aluno")
        print("0 - Encerra sistema")

        opcao = int(input("Escolha sua opção: "))
        return opcao
