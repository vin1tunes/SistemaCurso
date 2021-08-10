class TelaProfessor:
    def tela_opcoes(self):
        print("-------- PROFESSORES --------")
        print("Escolha a opção:")
        print("1 - Incluir Professor")
        print("2 - Alterar Professor")
        print("3 - Listar Professores")
        print("4 - Excluir Professor")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_professor(self):
        print("-------- DADOS PROFESSOR --------")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        departamento = input("Departamento: ")

        return {"nome": nome, "cpf": cpf, "departamento": departamento}

    def mostra_professor(self, dados_professor):
        print("Nome do professor: ", dados_professor["nome"])
        print("CPF do professor: ", dados_professor["cpf"])
        print("Departamento do professor: ", dados_professor["departamento"])
        print("\n")

    def seleciona_professor(self):
        cpf = input("CPF do professor que deseja selecionar: ")
        return cpf

    def show_msg(self, msg):
        print(msg)
