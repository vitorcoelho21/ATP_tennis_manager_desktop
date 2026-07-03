"""# Main para rodar no terminal
from interfaces.SistemaATP import SistemaAtp
from interfaces.menu_principal import MenuPrincipal

if __name__ == "__main__":
    sistema_atp = SistemaAtp()
    MenuPrincipal(sistema_atp).exibir_menu()""" 

# Main para rodar a interface gráfica
from gui.app import iniciar
if __name__ == "__main__":
    iniciar()   