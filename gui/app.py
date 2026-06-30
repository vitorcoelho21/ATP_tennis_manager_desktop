from gui.main_window import MainWindow
from interfaces.SistemaATP import SistemaAtp


def iniciar():
    sistema = SistemaAtp()

    app = MainWindow(sistema)
    app.mainloop()