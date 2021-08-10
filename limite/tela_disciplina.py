class TelaDisciplina:
    def tela_opcpes(self):
        print("-------- DISCIPLINAS --------")
        print("Escolha a opção:")
        print("1 - Incluir Disciplina")
        print("2 - Excluir Disciplina")
        print("3 - Alterar Disciplina")
        print("4 - Listar Disciplians")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_disciplina(self):
        print("-------- DADOS DISCIPLINA --------")
        nome = input("Nome: ")
        qtd_max_alunos = input("Número máximo de alunos: ")

        return {"nome": nome, "qtd_max_alunos": qtd_max_alunos}

    def mostra_disciplina(self, dados_disciplina):
        print("Nome da disciplina: ", dados_disciplina["nome"])
        print("Quantidade máxima de alunos: ", dados_disciplina["qtd_max_alunos"])
        print("Nome do professor: ", dados_disciplina["nome_professor"])
        print("CPF professor: ", dados_disciplina["cpf_professor"])
        print("Departamento: ", dados_disciplina["departamento_professor"])

    def mostra_aluno_disciplina(self, dados_aluno):
        print("Nome do aluno: ", dados_aluno["nome"])
        print("CPF do aluno: ", dados_aluno["cpf"])
        print("Matrícula do aluno ", dados_aluno["matricula"])

    def mostra_atividade_disciplina(self, dados_atividade):
        print("Título da atividade: ", dados_atividade["titulo"])
        print("Descrição da atividade: ", dados_atividade["descricao"])
        print("Prazo da atividade: ", dados_atividade["prazo"])
        print("Status da atividade: ", dados_atividade["status"])

    def seleciona_disciplina(self):
        nome_disciplina = input("Nome da disciplina que deseja selecionar: ")
        return nome_disciplina

    def seleciona_cpf_professor(self):
        cpf_professor = input("Selecione o CPF do professor que deseja incluir na disciplina: ")
        return cpf_professor

    def seleciona_matricula_aluno(self):
        matricula_aluno = input("Selecione a matrícula do aluno que deseja incluir na disciplina: ")
        return matricula_aluno

    def seleciona_titulo_atividade(self):
        titulo_atividade = input("Selecione o título da atividade que deseja incluir na disciplina: ")
        return titulo_atividade

    def show_msg(self, msg):
        print(msg)
