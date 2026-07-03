import customtkinter as ctk
from gui.temporada_page import TemporadaPage
from gui.torneios_page import TorneiosPage
from gui.styles import Cores
from gui.home_page import HomePage
from gui.jogadores_page import JogadoresPage
from gui.ranking_page import RankingPage
import os

class MainWindow(ctk.CTk):

    def __init__(self, sistema):

        super().__init__()
        try:
            icone = os.path.join("assets", "icon.ico")
            self.iconbitmap(icone)
        except Exception:
            pass
        self.sistema = sistema

        self.title("ATP Tennis Manager")

        self.geometry("1250x700")

        self.configure(fg_color=Cores.FUNDO)

        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0,
            fg_color=Cores.PAINEL
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.content = ctk.CTkFrame(
            self,
            fg_color=Cores.FUNDO
        )

        self.content.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.criar_sidebar()

        self.abrir_home()

    def criar_sidebar(self):

        titulo = ctk.CTkLabel(
            self.sidebar,
            text="ATP\nManager",
            font=("Segoe UI",28,"bold")
        )

        titulo.pack(
            pady=30
        )

        botoes = [

            ("🏠 Home", self.abrir_home),

            ("👤 Jogadores", self.abrir_jogadores),

            ("🏆 Torneios", self.abrir_torneios),

            ("📈 Ranking", self.abrir_ranking),

            ("📅 Temporada", self.abrir_temporada)

        ]

        for texto, comando in botoes:

            botao = ctk.CTkButton(

                self.sidebar,

                text=texto,

                height=45,

                command=comando

            )

            botao.pack(
                fill="x",
                padx=15,
                pady=8
            )

    def limpar_tela(self):

        for widget in self.content.winfo_children():

            widget.destroy()

    def abrir_home(self):

        self.limpar_tela()

        HomePage(
            self.content,
            self.sistema
        ).pack(
            fill="both",
            expand=True
        )

    def abrir_jogadores(self):
        self.limpar_tela()

        JogadoresPage(
            self.content,
            self.sistema
        ).pack(
            fill="both",
            expand=True
        )

    def abrir_ranking(self):

        self.limpar_tela()

        RankingPage(
            self.content,
            self.sistema
        ).pack(
            fill="both",
            expand=True
        )

    def abrir_torneios(self):
        self.limpar_tela()

        TorneiosPage(
            self.content,
            self.sistema
        ).pack(
            fill="both",
            expand=True
        )


    def abrir_temporada(self):

        self.limpar_tela()

        TemporadaPage(
            self.content,
            self.sistema
        ).pack(
            fill="both",
            expand=True
        )