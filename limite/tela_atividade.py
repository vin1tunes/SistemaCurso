class TelaAtividade:
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
        print("******** ATIVIDADES ********")
        print("Escolha a opção:")
        print("1 - Incluir Atividade")
        print("2 - Alterar Atividade")
        print("3 - Listar Atividades")
        print("4 - Excluir Atividade")
        print("0 - Retornar")

        opcao = self.validacao_opcao("Escolha uma opção: ", [1, 2, 3, 4, 0])
        return opcao

    def pega_dados_atividade(self):
        print("******** DADOS ATIVIDADE ********")
        titulo = input("Título: ")
        descricao = input("Descrição: ")
        prazo = input("Prazo: ")
        status = input("Status: ")

        return {"titulo": titulo, "descricao": descricao, "prazo": prazo, "status": status}

    def mostra_atividade(self, dados_atividade):
        print("Título da atividade: ", dados_atividade["titulo"])
        print("Descrição da atividade: ", dados_atividade["descricao"])
        print("Prazo da atividade: ", dados_atividade["prazo"])
        print("Status da atividade: ", dados_atividade["status"])
        print("\n")

    def seleciona_atividade(self):
        titulo_atividade = input("Título da atividade que deseja selecionar: ")
        return titulo_atividade

    def show_msg(self, msg):
        print(msg)
