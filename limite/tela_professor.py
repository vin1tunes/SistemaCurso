class TelaProfessor:
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
        print("-------- PROFESSORES --------")
        print("Escolha a opção:")
        print("1 - Incluir Professor")
        print("2 - Alterar Professor")
        print("3 - Listar Professores")
        print("4 - Excluir Professor")
        print("0 - Retornar")

        opcao = self.validacao_opcao("Escolha uma opção: ", [1, 2, 3, 4, 0])
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
