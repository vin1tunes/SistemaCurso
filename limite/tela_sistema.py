class TelaSistema:
    def validacao_opcao(self, msg: str = "", numeros_validos: [] = None):
        while True:
            opcao_lida = input(msg)
            try:
                numero = int(opcao_lida)
                if numeros_validos and numero not in numeros_validos:
                    raise ValueError
                return numero
            except ValueError:
                print("Número incorreto.")
                if numeros_validos:
                    print("Números válidos: ", numeros_validos)

    def tela_opcoes(self):
        print("******** BEM-VINDO AO CURSO DE SISTEMAS DE INFORMAÇÃO ********")
        print("Selecione o que deseja acessar: ")
        print("1 - Alunos")
        print("2 - Professores")
        print("3 - Disciplinas")
        print("4 - Atividades")
        print("5 - Atividades Aluno")
        print("0 - Encerra sistema")

        opcao = self.validacao_opcao("Escolha uma opção: ", [1, 2, 3, 4, 5, 0])
        return opcao
