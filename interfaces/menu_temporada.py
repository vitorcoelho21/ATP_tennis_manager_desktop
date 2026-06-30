
class MenuTemporada:
    def __init__(self, sistema_atp):
        self.sistema_atp = sistema_atp

    def exibir_menu(self):
        while True:
            print("\n===== MENU TEMPORADA =====")
            print("1. Simular temporada")
            print("2. Recuperar stamina dos jogadores")
            print("3. Exibir campeões da temporada")
            print("0. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.simular_temporada()
            elif opcao == "2":
                self.recuperar_stamina()
            elif opcao == "3":
                self.exibir_campeoes()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

    def simular_temporada(self):
        if not self.sistema_atp.torneios:
            print("Nenhum torneio cadastrado.")
            return

        print("\n===== INICIANDO TEMPORADA =====")

        for torneio in self.sistema_atp.torneios:
            if torneio.campeao is None:
                self.sistema_atp.iniciar_torneio(torneio)

        self.sistema_atp.ranking.atualizar_ranking()

        print("\nTemporada encerrada!")
        print(self.sistema_atp.get_ranking_geral())

    def recuperar_stamina(self):
        for jogador in self.sistema_atp.jogadores:
            while jogador.stamina < 100:
                jogador.recuperar_stamina()

        self.sistema_atp.atualizar_banco()

        print("Todos os jogadores recuperaram a stamina.")

    def exibir_campeoes(self):
        print("\n===== CAMPEÕES DA TEMPORADA =====")

        existe = False

        for torneio in self.sistema_atp.torneios:
            if torneio.campeao is not None:
                print(f"{torneio.nome}: {torneio.campeao.nome}")
                existe = True

        if not existe:
            print("Nenhum torneio foi disputado.")