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
        