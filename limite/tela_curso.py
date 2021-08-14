class TelaCurso:
    def tela_opcoes(self):
        print("******** CURSO ********")
        print("1 - Incluir Curso")
        print("2 - Excluir Curso")
        print("3 - Alterar Curso")
        print("4 - Listar Curso")
        print("0 - Retornar")

        opcao = int(input("Escolha sua opção: "))
        return opcao

    def pega_dados_curso(self):
        print("******** DADOS CURSO ********")
        nome = input("Nome: ")
        instituicao = input("Instituição: ")

        return {"nome": nome, "instituicao": instituicao}

    def mostra_curso(self, dados_curso):
        print("Nome do curso: ", dados_curso["nome"])
        print("Nome da instituição: ", dados_curso["instituicao"])

    def mostra_disciplina_curso(self, dados_disciplina):
        print("Nome da disciplina: ", dados_disciplina["nome"])

    def seleciona_curso(self):
        nome_curso = input("Nome do curso que deseja selecionar: ")
        return nome_curso

    def seleciona_disciplina_curso(self):
        nome_disciplina = input("Nome da disciplina que deseja incluir no curso: ")
        return nome_disciplina

    def show_msg(self, msg):
        print(msg)
