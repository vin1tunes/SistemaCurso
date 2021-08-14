class TelaAtividadeAluno:
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
        print("******** ATIVIDADE ALUNO ********")
        print("Escolha a opção:")
        print("1 - Incluir Atividade")
        print("2 - Excluir Atividade")
        print("3 - Alterar Atividade")
        print("4 - Listar todas atividades realizadas")
        print("5 - Listar todas atividades de um aluno")
        print("6 - Listar todas atividades de um aluno em uma disciplina")
        print("7 - Calcula a média de um aluno em uma disciplina")
        print("8 - Buscar Atividade de um aluno")
        print("0 - Retornar")

        opcao = self.validacao_opcao("Escolha uma opção: ", [1, 2, 3, 4, 5, 6, 7, 8, 0])
        return opcao

    def pega_dados_atividade_aluno(self):
        print("******** DADOS ATIVIDADE ALUNO ********")
        nota = input("Nota: ")
        data_entrega = input("Data de entrega: ")

        return {"nota": nota, "data_entrega": data_entrega}

    def mostra_atividade_aluno(self, dados_atividade_aluno):
        print("Nota do aluno: ", dados_atividade_aluno["nota"])
        print("Data da entrega: ", dados_atividade_aluno["data_entrega"])
        print("Título da atividade: ", dados_atividade_aluno["titulo_atividade"])
        print("Descrição da atividade: ", dados_atividade_aluno["descricao_atividade"])
        print("Prazo da atividade: ", dados_atividade_aluno["prazo"])
        print("Status da atividade: ", dados_atividade_aluno["status"])
        print("Nome do aluno: ", dados_atividade_aluno["nome_aluno"])
        print("CPF do aluno: ", dados_atividade_aluno["cpf_aluno"])
        print("Matrícula do aluno: ", dados_atividade_aluno["matricula_aluno"])
        print("Nome da disciplina: ", dados_atividade_aluno["nome_disciplina"])
        print("Nome do professor: ", dados_atividade_aluno["nome_professor"])

    def seleciona_matricula_aluno(self):
        matricula_aluno = input("Seleciona a matrícula do aluno: ")
        return matricula_aluno

    def seleciona_atividade_titulo(self):
        titulo_atividade = input("Selecione o título da atividade que deseja incluir: ")
        return titulo_atividade

    def seleciona_nome_disciplina(self):
        nome_disciplina = input("Selecione o nome da disciplina: ")
        return nome_disciplina

    def mostra_media(self, media):
        print(media)

    def show_msg(self, msg):
        print(msg)
