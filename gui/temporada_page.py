import customtkinter as ctk

from gui.styles import Cores


class TemporadaPage(ctk.CTkFrame):

    def __init__(self, master, sistema):

        super().__init__(master)

        self.sistema = sistema

        self.configure(fg_color=Cores.FUNDO)

        self.criar_titulo()

        self.criar_resumo()

        self.criar_proximo_torneio()

        self.criar_historico()

        self.criar_lider()


    def criar_titulo(self):

        ctk.CTkLabel(

            self,

            text="Temporada ATP",

            font=("Segoe UI",30,"bold")

        ).pack(pady=(20,15))


    def criar_resumo(self):

        frame = ctk.CTkFrame(self)

        frame.pack(fill="x", padx=20)

        total = len(self.sistema.torneios)

        finalizados = len(

            [t for t in self.sistema.torneios if t.finalizado]

        )

        pendentes = total-finalizados

        ctk.CTkLabel(

            frame,

            text="Resumo da Temporada",

            font=("Segoe UI",20,"bold")

        ).pack(pady=(15,10))

        ctk.CTkLabel(

            frame,

            text=f"Torneios: {total}"

        ).pack()

        ctk.CTkLabel(

            frame,

            text=f"Finalizados: {finalizados}"

        ).pack()

        ctk.CTkLabel(

            frame,

            text=f"Pendentes: {pendentes}"

        ).pack(pady=(0,15))


    def criar_proximo_torneio(self):

        frame = ctk.CTkFrame(self)

        frame.pack(fill="x", padx=20, pady=20)

        ctk.CTkLabel(

            frame,

            text="Próximo Torneio",

            font=("Segoe UI",20,"bold")

        ).pack(pady=(15,10))

        proximo = None

        for torneio in self.sistema.torneios:

            if not torneio.finalizado:

                proximo = torneio

                break

        if proximo is None:

            ctk.CTkLabel(

                frame,

                text="Todos os torneios foram concluídos."

            ).pack(pady=20)

            return

        ctk.CTkLabel(

            frame,

            text=proximo.nome,

            font=("Segoe UI",18,"bold")

        ).pack()

        ctk.CTkLabel(

            frame,

            text=f"Categoria: {proximo.categoria.nome}"

        ).pack()

        ctk.CTkLabel(

            frame,

            text=f"Superfície: {proximo.superficie.value.title()}"

        ).pack()

        ctk.CTkLabel(

            frame,

            text=f"Jogadores inscritos: {len(proximo.jogadores)}"

        ).pack(pady=(0,10))

        ctk.CTkButton(

            frame,

            text="▶ Iniciar Torneio",

            command=lambda:self.iniciar_torneio(proximo)

        ).pack(pady=(0,15))


    def criar_historico(self):

        frame = ctk.CTkFrame(self)

        frame.pack(fill="x", padx=20)

        ctk.CTkLabel(

            frame,

            text="Torneios Concluídos",

            font=("Segoe UI",20,"bold")

        ).pack(pady=(15,10))

        encontrou = False

        for torneio in self.sistema.torneios:

            if torneio.finalizado:

                encontrou = True

                texto = f"🏆 {torneio.nome}  •  {torneio.campeao.nome}"

                ctk.CTkLabel(

                    frame,

                    text=texto

                ).pack(anchor="w", padx=20, pady=3)

        if not encontrou:

            ctk.CTkLabel(

                frame,

                text="Nenhum torneio finalizado."

            ).pack(pady=(0,15))


    def criar_lider(self):

        frame = ctk.CTkFrame(self)

        frame.pack(fill="x", padx=20, pady=20)

        ctk.CTkLabel(

            frame,

            text="Líder do Ranking",

            font=("Segoe UI",20,"bold")

        ).pack(pady=(15,10))

        self.sistema.ranking.atualizar_ranking()

        if len(self.sistema.ranking.jogadores)==0:

            ctk.CTkLabel(

                frame,

                text="Nenhum jogador."

            ).pack(pady=15)

            return

        lider = self.sistema.ranking.jogadores[0]

        ctk.CTkLabel(

            frame,

            text=f"🥇 {lider.nome}",

            font=("Segoe UI",18,"bold")

        ).pack()

        ctk.CTkLabel(

            frame,

            text=f"{lider.pontos} pontos"

        ).pack()

        ctk.CTkLabel(

            frame,

            text=f"{lider.vitorias}V / {lider.derrotas}D"

        ).pack(pady=(0,15))


    def iniciar_torneio(self, torneio):

        self.sistema.iniciar_torneio(torneio)

        for widget in self.winfo_children():

            widget.destroy()

        self.criar_titulo()

        self.criar_resumo()

        self.criar_proximo_torneio()

        self.criar_historico()

        self.criar_lider()