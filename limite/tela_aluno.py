class TelaAluno:
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
        print("******** ALUNOS ********")
        print("Escolha a opção:")
        print("1 - Incluir Aluno")
        print("2 - Alterar Aluno")
        print("3 - Listar Alunos")
        print("4 - Excluir Aluno")
        print("5 - Buscar Aluno")
        print("0 - Retornar")

        opcao = self.validacao_opcao("Escolha uma opção: ", [1, 2, 3, 4, 5, 0])
        return opcao

    def pega_dados_aluno(self):
        print("******** DADOS ALUNO ********")
        nome = input("Nome: ")
        cpf = int(input("CPF: "))
        matricula = int(input("Matrícula: "))

        return {"nome": nome, "cpf": cpf, "matricula": matricula}

    def mostra_aluno(self, dados_aluno):
        print("Nome do aluno: ", dados_aluno["nome"])
        print("CPF do aluno: ", dados_aluno["cpf"])
        print("Matrícula do aluno: ", dados_aluno["matricula"])
        print("\n")

    def seleciona_aluno(self):
        matricula = int(input("Matrícula do aluno que deseja selecionar: "))
        return matricula

    def show_msg(self, msg):
        print(msg)
