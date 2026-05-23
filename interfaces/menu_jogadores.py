from models.Jogador import Jogador

class MenuJogadores:
    def __init__(self, sistema_atp):
        self.sistema_atp = sistema_atp

    def exibir_menu(self):
        while True:
            print("\n===== MENU JOGADORES =====")
            print("1. Cadastrar jogador")
            print("2. Buscar jogador")
            print("3. Listar jogadores")
            print("0. Voltar")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.cadastrar_jogador()
            elif escolha == "2":
                self.buscar_jogador()
            elif escolha == "3":
                self.listar_jogadores()
            elif escolha == "0":
                break
            else:
                print("Opção inválida!")

    def cadastrar_jogador(self):
        print("\n--- Cadastro de Jogador ---")

        nome = input("Nome: ")
        if nome.strip() == "":
            print("Nome não pode ser vazio.")
            return
        try:
            idade = int(input("Idade: "))
            if idade < 0:
                print("Idade deve ser um número positivo.")
                return
        except ValueError:
            print("Idade deve ser um número inteiro.")
            return
        
        nacionalidade = input("Nacionalidade: ")
        try:
            habilidade_saibro = int(input("Habilidade no saibro (0-100): "))
            habilidade_grama = int(input("Habilidade na grama (0-100): "))
            habilidade_hard = int(input("Habilidade no hard (0-100): "))
            if not (0 <= habilidade_saibro <= 100 and 0 <= habilidade_grama <= 100 and 0 <= habilidade_hard <= 100):
                print("Habilidades devem ser entre 0 e 100.")
                return
        except ValueError:            
            print("Habilidades devem ser números inteiros.")
            return

        self.sistema_atp.cadastrar_jogador(
            nome,
            idade,
            nacionalidade,
            habilidade_saibro,
            habilidade_grama,
            habilidade_hard
        )

        print("Jogador cadastrado com sucesso!")

    def buscar_jogador(self):
        print("\n--- Buscar Jogador ---")

        nome = input("Nome do jogador: ")

        jogador = self.sistema_atp.buscar_jogador(nome)

        if jogador:
            print("\nJogador encontrado:")
            print(jogador.mostrar_info())
            print(jogador.mostrar_estatisticas())
        else:
            print("Jogador não encontrado.")

    def listar_jogadores(self):
        print("\n--- Lista de Jogadores ---")

        if not self.sistema_atp.jogadores:
            print("Nenhum jogador cadastrado.")
            return

        for jogador in self.sistema_atp.jogadores:
            print(jogador)