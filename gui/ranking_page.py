import customtkinter as ctk


class RankingPage(ctk.CTkFrame):

    def __init__(self, master, sistema):
        super().__init__(master)

        self.sistema = sistema

        titulo = ctk.CTkLabel(
            self,
            text="🏆 Ranking Mundial",
            font=("Segoe UI", 28, "bold")
        )
        titulo.pack(pady=20)

        self.lista = ctk.CTkScrollableFrame(
            self,
            width=900,
            height=500
        )
        self.lista.pack(fill="both", expand=True, padx=20, pady=10)

        botao = ctk.CTkButton(
            self,
            text="Atualizar Ranking",
            command=self.atualizar
        )
        botao.pack(pady=20)

        self.atualizar()

    def atualizar(self):

        for widget in self.lista.winfo_children():
            widget.destroy()

        self.sistema.ranking.atualizar_ranking()

        cabecalho = ctk.CTkFrame(self.lista)

        cabecalho.pack(fill="x", padx=5, pady=5)

        titulos = [
            "Pos",
            "Nome",
            "Pts",
            "Vit",
            "Der",
            "%",
            "Sta",
            "Fis"
        ]

        for texto in titulos:
            lbl = ctk.CTkLabel(
                cabecalho,
                text=texto,
                width=90,
                font=("Segoe UI", 14, "bold")
            )
            lbl.pack(side="left", padx=5)

        for jogador in self.sistema.ranking.jogadores:

            linha = ctk.CTkFrame(self.lista)

            linha.pack(fill="x", padx=5, pady=3)

            dados = [
                jogador.ranking,
                jogador.nome,
                jogador.pontos,
                jogador.vitorias,
                jogador.derrotas,
                f"{jogador.calcular_desempenho()}%",
                jogador.stamina,
                jogador.fisico
            ]

            for dado in dados:

                lbl = ctk.CTkLabel(
                    linha,
                    text=str(dado),
                    width=90
                )

                lbl.pack(side="left", padx=5)