from interfaces.menu_jogadores import MenuJogadores
from interfaces.menu_ranking import MenuRanking
from interfaces.menu_torneios import MenuTorneios
from utils.enums import Superficie
class MenuPrincipal:
    def __init__(self, sistema_atp):
        self.sistema_atp = sistema_atp
    
    def exibir_menu(self):
        while True:
            print("\nMenu Principal")
            print("1. Jogadores")
            print("2. Ranking")
            print("3. Torneios")
            print("0. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.menu_jogadores()
            elif escolha == "2":
                self.menu_ranking()
            elif escolha == "3":
                self.menu_torneios()
            elif escolha == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def menu_jogadores(self):
        menu = MenuJogadores(self.sistema_atp)
        menu.exibir_menu()
    
    def menu_ranking(self):
        menu = MenuRanking(self.sistema_atp)
        menu.exibir_menu()

    def menu_torneios(self):
        menu = MenuTorneios(self.sistema_atp)
        menu.exibir_menu()