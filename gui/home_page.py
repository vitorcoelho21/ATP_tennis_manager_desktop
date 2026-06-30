import customtkinter as ctk

from gui.styles import Cores


class HomePage(ctk.CTkFrame):

    def __init__(self, master, sistema):
        super().__init__(master, fg_color=Cores.FUNDO)

        self.sistema = sistema

        self.criar_titulo()
        self.criar_cards()

    def criar_titulo(self):

        titulo = ctk.CTkLabel(
            self,
            text="ATP Tennis Manager",
            font=("Segoe UI", 32, "bold")
        )

        titulo.pack(pady=(30, 5))

        subtitulo = ctk.CTkLabel(
            self,
            text="Painel de Controle",
            font=("Segoe UI", 16)
        )

        subtitulo.pack(pady=(0, 30))

    def criar_cards(self):

        container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        container.pack(padx=20, pady=10)

        total_jogadores = len(self.sistema.jogadores)
        total_torneios = len(self.sistema.torneios)

        self.sistema.ranking.atualizar_ranking()

        if self.sistema.ranking.jogadores:
            lider = self.sistema.ranking.jogadores[0]
            lider_texto = f"{lider.nome}\n{lider.pontos} pts"
        else:
            lider_texto = "Nenhum"

        campeao = "Nenhum"

        for torneio in self.sistema.torneios:
            if torneio.campeao:
                campeao = torneio.campeao.nome

        cards = [

            ("👤", "Jogadores", str(total_jogadores)),

            ("🏆", "Torneios", str(total_torneios)),

            ("🥇", "Líder Ranking", lider_texto),

            ("🎾", "Último Campeão", campeao)

        ]

        linha = ctk.CTkFrame(
            container,
            fg_color="transparent"
        )

        linha.pack()

        for icone, titulo, valor in cards:

            card = ctk.CTkFrame(
                linha,
                width=220,
                height=180,
                corner_radius=15
            )

            card.pack(side="left", padx=15)

            card.pack_propagate(False)

            ctk.CTkLabel(
                card,
                text=icone,
                font=("Segoe UI Emoji", 40)
            ).pack(pady=(20, 5))

            ctk.CTkLabel(
                card,
                text=titulo,
                font=("Segoe UI", 18, "bold")
            ).pack()

            ctk.CTkLabel(
                card,
                text=valor,
                font=("Segoe UI", 18)
            ).pack(pady=15)

        dica = ctk.CTkLabel(
            self,
            text="Utilize o menu lateral para gerenciar jogadores, torneios, ranking e temporadas.",
            font=("Segoe UI", 14)
        )

        dica.pack(pady=40)