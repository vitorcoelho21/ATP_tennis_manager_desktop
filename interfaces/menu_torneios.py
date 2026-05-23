from models.Torneio import Torneio
from utils.enums import CategoriaTorneio, CategoriaTorneio, Superficie

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

    def criar_torneio(self):
        nome = input("Digite o nome do torneio: ")
        superficie = input("Digite a superfície do torneio (saibro, grama, hard): ").lower()
        categoria = input("Digite a categoria do torneio (atp250, atp500, masters1000): ").lower()
        if superficie == "saibro":
            superficie = Superficie.SAIBRO
        elif superficie == "grama":
            superficie = Superficie.GRAMA
        elif superficie == "hard":
            superficie = Superficie.HARD
        else:
            print("Superfície inválida.")
            return
        if categoria == "atp250":
            categoria = CategoriaTorneio.ATP250
        elif categoria == "atp500":
            categoria = CategoriaTorneio.ATP500
        elif categoria == "masters1000":
            categoria = CategoriaTorneio.MASTERS1000
        else:
            print("Categoria inválida.")
            return
        torneio = Torneio(nome, categoria, superficie)
        self.sistema_atp.torneios.append(torneio)
        print(f"Torneio {nome} criado com sucesso!")

    def listar_torneios(self):
        if not self.sistema_atp.torneios:
            print("Nenhum torneio cadastrado.")
            return
        print("\n===== TORNEIOS =====")
        for torneio in self.sistema_atp.torneios:
            if torneio.campeao is None:
                print(f"Nome: {torneio.nome}, Categoria: {torneio.categoria.nome}, Superfície: {torneio.superficie.value}, Jogadores: {len(torneio.jogadores)}")
            else:
                print(f"Nome: {torneio.nome}, Categoria: {torneio.categoria.nome}, Superfície: {torneio.superficie.value}, Campeão: {torneio.campeao.nome}")

    def adicionar_jogador_torneio(self):
        if not self.sistema_atp.torneios:
            print("Nenhum torneio cadastrado.")
            return
        i = 1
        for torneio in self.sistema_atp.torneios:
            print(f"{i}. {torneio.nome}")
            i += 1
        try:
            indice = int(input("Escolha o torneio para adicionar um jogador: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            return
        if indice < 1 or indice > len(self.sistema_atp.torneios):
            print("Índice inválido.")
            return
        torneio = self.sistema_atp.torneios[indice - 1]
        j = 1
        self.sistema_atp.ranking.atualizar_ranking()
        for jogador in self.sistema_atp.ranking.jogadores:
            print(f"{j}. {jogador.nome}")
            j += 1
        try:
            indice_jogador = int(input("Escolha o jogador para adicionar ao torneio: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            return
        if indice_jogador < 1 or indice_jogador > len(self.sistema_atp.ranking.jogadores):
            print("Índice inválido.")
            return
        jogador = self.sistema_atp.ranking.jogadores[indice_jogador - 1]
        try:
            torneio.adicionar_jogador(jogador)
        except ValueError as e:
            print(e)
            return
        print(f"Jogador {jogador.nome} adicionado ao torneio {torneio.nome} com sucesso!")
    
    def iniciar_torneio(self):
        if not self.sistema_atp.torneios:
            print("Nenhum torneio cadastrado.")
            return
        i = 1
        for torneio in self.sistema_atp.torneios:
            print(f"{i}. {torneio.nome}")
            i += 1
        try:
            indice = int(input("Escolha o torneio para iniciar: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            return
        if indice < 1 or indice > len(self.sistema_atp.torneios):
            print("Índice inválido.")
            return
        torneio = self.sistema_atp.torneios[indice - 1]
        if len(torneio.jogadores) % 2 != 0:
            print("O torneio precisa ter um número par de jogadores para iniciar.")
            return
        elif len(torneio.jogadores) < 2:
            print("O torneio precisa ter pelo menos 2 jogadores para iniciar.")
            return
        if torneio.campeao is not None:
            print("Torneio já foi iniciado e tem um campeão.")
            return
        try:
            torneio.iniciar_torneio()
        except ValueError as e:
            print(e)
            return
        print(f"Torneio {torneio.nome} iniciado com sucesso!")