class MenuTorneios:
    def __init__(self, sistemaATP):
        self.sistema_atp = sistemaATP

    def exibir_menu(self):
        while True:
            print("\n===== MENU TORNEIOS =====")
            print("1. Criar torneio")
            print("2. Listar torneios")
            print("3. Adicionar jogador a torneio")
            print("4. Iniciar torneio")
            print("0. Voltar")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.criar_torneio()
            elif opcao == "2":
                self.listar_torneios()
            elif opcao == "3":
                self.adicionar_jogador_torneio()
            elif opcao == "4":
                self.iniciar_torneio()
            elif opcao == "0":
                break
            else:
                print("Opção inválida. Tente novamente.")