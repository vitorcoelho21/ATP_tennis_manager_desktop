from interfaces.SistemaATP import SistemaAtp
from interfaces.menu_principal import MenuPrincipal

if __name__ == "__main__":
    sistema_atp = SistemaAtp()
    MenuPrincipal(sistema_atp).exibir_menu()