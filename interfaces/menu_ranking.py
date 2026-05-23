
class MenuRanking:
    def __init__(self,sistemaATP):
        self.sistema_atp = sistemaATP

    def exibir_menu(self):
        while True:
            print("\n===== MENU RANKING =====")
            print("1. Exibir ranking geral")
            print("2. Exibir ranking do jogador")
            print("3. Exibir estatísticas gerais")
            print("0. Voltar")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.exibir_ranking_geral()
            elif opcao == "2":
                self.exibir_ranking_jogador()
            elif opcao == "3":
                self.exibir_estatisticas_gerais()
            elif opcao == "0":
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def exibir_ranking_geral(self):
        ranking = self.sistema_atp.get_ranking_geral()
        print(ranking)

    def exibir_ranking_jogador(self):
        nome = input("Digite o nome do jogador: ")
        jogador = self.sistema_atp.buscar_jogador(nome)
        if jogador:
            print(f"\n===== RANKING DE {jogador.nome.upper()} =====")
            print(f"Ranking: {jogador.ranking}")
            print(f"Pontos: {jogador.pontos}")
            print(f"Titulos: {jogador.mostrar_titulos()}")
        else:
            print("Jogador não encontrado.")
        
    def exibir_estatisticas_gerais(self):
        jogadores = self.sistema_atp.jogadores
        if not jogadores:
            print("Nenhum jogador cadastrado.")
            return
        self.sistema_atp.ranking.atualizar_ranking()
        print("\n===== ESTATÍSTICAS GERAIS =====")
        print(f"Total de jogadores: {len(jogadores)}")
        lider = jogadores[0]
        for jogador in jogadores:
            if jogador.pontos > lider.pontos:
                lider = jogador
        print(f"Líder mundial: {lider.nome} ({lider.pontos} pontos)")
        maior_campeao = jogadores[0]
        maior_quantidade = 0
        for quantidade in maior_campeao.titulos.values():
            maior_quantidade += quantidade
        for jogador in jogadores:
            total_titulos = 0
            for quantidade in jogador.titulos.values():
                total_titulos += quantidade
            if total_titulos > maior_quantidade:
                maior_campeao = jogador
                maior_quantidade = total_titulos
        print(f"Maior campeão: {maior_campeao.nome} ({maior_quantidade} títulos)")
        soma_pontos = 0
        for jogador in jogadores:
            soma_pontos += jogador.pontos
        media = soma_pontos / len(jogadores)
        print(f"Média de pontos: {media:.2f}")
        print(self.sistema_atp.ranking.mostrar_top10())
