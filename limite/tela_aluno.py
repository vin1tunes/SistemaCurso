class TelaAluno:
    def tela_opcoes(self):
        print("-------- ALUNOS --------")
        print("Escolha a opção:")
        print("1 - Incluir Aluno")
        print("2 - Alterar Aluno")
        print("3 - Listar Alunos")
        print("4 - Excluir Aluno")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_aluno(self):
        print("-------- DADOS ALUNO --------")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        matricula = input("Matrícula: ")

        return {"nome": nome, "cpf": cpf, "matricula": matricula}

    def mostra_aluno(self, dados_aluno):
        print("Nome do aluno: ", dados_aluno["nome"])
        print("CPF do aluno: ", dados_aluno["cpf"])
        print("Matrícula do aluno: ", dados_aluno["matricula"])
        print("\n")

    def seleciona_aluno(self):
        matricula = input("Matrícula do aluno que deseja selecionar: ")
        return matricula

    def show_msg(self, msg):
        print(msg)
