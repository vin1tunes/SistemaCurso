class TelaAtividadeAluno:
    def tela_opcoes(self):
        print("-------- ATIVIDADE ALUNO -------")
        print("Escolha a opção:")
        print("1 - Incluir atividade")
        print("2 - Excluir atividade")
        print("3 - Alterar atividade")
        print("4 - Listar todas atividades realizadas")
        print("5 - Calcula média atividades")
        print("6 - Listar todas atividades de um aluno")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_atividade_aluno(self):
        print("------- DADOS ATIVIDADE ALUNO --------")
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

    def seleciona_matricula_aluno(self):
        matricula_aluno = input("Seleciona a matrícula do aluno: ")
        return matricula_aluno

    def seleciona_atividade_titulo(self):
        titulo_atividade = input("Selecione o título da atividade que deseja incluir: ")
        return titulo_atividade

    def mostra_media(self, media):
        print(media)

    def show_msg(self, msg):
        print(msg)
