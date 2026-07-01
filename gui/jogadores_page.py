import customtkinter as ctk
from tkinter import messagebox
from utils.enums import Superficie

class JogadoresPage(ctk.CTkFrame):

    def __init__(self, master, sistema):

        super().__init__(master)

        self.sistema = sistema

        self.configure(fg_color="#202124")

        self.criar_topo()

        self.criar_area_cards()

        self.atualizar_lista()


    def criar_topo(self):

        topo = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        topo.pack(
            fill="x",
            padx=25,
            pady=(20, 10)
        )

        titulo = ctk.CTkLabel(
            topo,
            text="🎾 Gerenciamento de Jogadores",
            font=("Segoe UI", 30, "bold")
        )

        titulo.pack(anchor="w")

        subtitulo = ctk.CTkLabel(
            topo,
            text="Gerencie atletas, estatísticas e desempenho.",
            font=("Segoe UI", 14)
        )

        subtitulo.pack(anchor="w", pady=(0, 15))

        barra = ctk.CTkFrame(
            topo
        )

        barra.pack(fill="x")

        self.entry_pesquisa = ctk.CTkEntry(
            barra,
            placeholder_text="Pesquisar jogador...",
            width=350
        )

        self.entry_pesquisa.pack(
            side="left",
            padx=(0, 10)
        )

        self.entry_pesquisa.bind(
            "<KeyRelease>",
            lambda e: self.atualizar_lista()
        )

        ctk.CTkButton(
            barra,
            text="➕ Novo Jogador",
            width=170,
            command=self.novo_jogador
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            barra,
            text="🔄 Atualizar",
            width=130,
            command=self.atualizar_lista
        ).pack(side="left", padx=5)


    def criar_area_cards(self):

        self.scroll = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )

        self.scroll.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )



    def atualizar_lista(self):

        self.sistema.ranking.atualizar_ranking()

        for widget in self.scroll.winfo_children():

            widget.destroy()

        texto = self.entry_pesquisa.get().lower()

        jogadores = []

        for jogador in self.sistema.ranking.jogadores:

            if texto in jogador.nome.lower():

                jogadores.append(jogador)

        if len(jogadores) == 0:

            ctk.CTkLabel(

                self.scroll,

                text="Nenhum jogador encontrado.",

                font=("Segoe UI",20)

            ).pack(pady=40)

            return

        for jogador in jogadores:

            self.criar_card(jogador)


    def criar_card(self, jogador):

        card = ctk.CTkFrame(

            self.scroll,

            corner_radius=15

        )

        card.pack(

            fill="x",

            padx=10,

            pady=12

        )

        cabecalho = ctk.CTkFrame(

            card,

            fg_color="transparent"

        )

        cabecalho.pack(

            fill="x",

            padx=20,

            pady=(15,10)

        )

        nome = ctk.CTkLabel(

            cabecalho,

            text=f"{jogador.nome}",

            font=("Segoe UI",22,"bold")

        )

        nome.pack(side="left")

        ranking = ctk.CTkLabel(

            cabecalho,

            text=f"🏆 #{jogador.ranking}",

            font=("Segoe UI",20)

        )

        ranking.pack(side="right")

        info = ctk.CTkFrame(

            card,

            fg_color="transparent"

        )

        info.pack(

            fill="x",

            padx=20

        )

        ctk.CTkLabel(

            info,

            text=f"Nacionalidade: {jogador.nacionalidade}"

        ).grid(

            row=0,

            column=0,

            sticky="w",

            padx=5,

            pady=3

        )

        ctk.CTkLabel(

            info,

            text=f"Idade: {jogador.idade} anos"

        ).grid(

            row=0,

            column=1,

            sticky="w",

            padx=15

        )

        ctk.CTkLabel(

            info,

            text=f"Pontos: {jogador.pontos}"

        ).grid(

            row=0,

            column=2,

            sticky="w",

            padx=15

        )

        ctk.CTkLabel(

            info,

            text=f"Vitórias: {jogador.vitorias}"

        ).grid(

            row=1,

            column=0,

            sticky="w",

            padx=5,

            pady=5

        )

        ctk.CTkLabel(

            info,

            text=f"Derrotas: {jogador.derrotas}"

        ).grid(

            row=1,

            column=1,

            sticky="w",

            padx=15

        )

        ctk.CTkLabel(

            info,

            text=f"Desempenho: {jogador.calcular_desempenho():.1f}%"

        ).grid(

            row=1,

            column=2,

            sticky="w",

            padx=15

        )

        self.criar_barras(card, jogador)

        self.criar_botoes(card, jogador)


    def criar_barras(self, card, jogador):

        frame = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.criar_barra(
            frame,
            "Saibro",
            jogador.habilidades[list(jogador.habilidades.keys())[0]],
            0
        )

        self.criar_barra(
            frame,
            "Grama",
            jogador.habilidades[list(jogador.habilidades.keys())[1]],
            1
        )

        self.criar_barra(
            frame,
            "Hard",
            jogador.habilidades[list(jogador.habilidades.keys())[2]],
            2
        )

        self.criar_barra(
            frame,
            "Stamina",
            jogador.stamina,
            3
        )

        self.criar_barra(
            frame,
            "Físico",
            jogador.fisico,
            4
        )


    def criar_barra(self, frame, texto, valor, linha):

        ctk.CTkLabel(
            frame,
            text=texto,
            width=110,
            anchor="w"
        ).grid(
            row=linha,
            column=0,
            sticky="w",
            pady=4
        )

        barra = ctk.CTkProgressBar(
            frame,
            width=320,
            height=12
        )

        barra.grid(
            row=linha,
            column=1,
            padx=10,
            pady=4,
            sticky="ew"
        )

        barra.set(valor / 100)

        ctk.CTkLabel(
            frame,
            text=str(valor),
            width=35
        ).grid(
            row=linha,
            column=2,
            padx=10
        )


    def criar_botoes(self, card, jogador):

        frame = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        frame.pack(
            fill="x",
            padx=20,
            pady=(10,20)
        )

        ctk.CTkButton(
            frame,
            text="📊 Detalhes",
            width=120,
            command=lambda j=jogador: self.mostrar_jogador(j)
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            frame,
            text="✏ Editar",
            width=100,
            command=lambda j=jogador: self.editar_jogador(j)
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            frame,
            text="🗑 Excluir",
            width=100,
            fg_color="#C0392B",
            hover_color="#922B21",
            command=lambda j=jogador: self.excluir_jogador(j)
        ).pack(
            side="right",
            padx=5
        )


    def novo_jogador(self):

        janela = ctk.CTkToplevel(self)
        janela.title("Novo Jogador")
        janela.geometry("420x560")
        janela.grab_set()

        campos = {}

        labels = [
            ("Nome", "nome"),
            ("Idade", "idade"),
            ("Nacionalidade", "nacionalidade"),
            ("Saibro", "saibro"),
            ("Grama", "grama"),
            ("Hard", "hard")
        ]

        for texto, chave in labels:

            ctk.CTkLabel(
                janela,
                text=texto
            ).pack(pady=(12, 2))

            entrada = ctk.CTkEntry(janela)

            entrada.pack(fill="x", padx=30)

            campos[chave] = entrada

        def cadastrar():

            try:

                self.sistema.cadastrar_jogador(

                    campos["nome"].get(),

                    int(campos["idade"].get()),

                    campos["nacionalidade"].get(),

                    int(campos["saibro"].get()),

                    int(campos["grama"].get()),

                    int(campos["hard"].get())

                )

                self.atualizar_lista()

                janela.destroy()

                messagebox.showinfo(
                    "Sucesso",
                    "Jogador cadastrado!"
                )

            except Exception as erro:

                messagebox.showerror(
                    "Erro",
                    str(erro)
                )

        ctk.CTkButton(

            janela,

            text="Cadastrar",

            command=cadastrar

        ).pack(pady=25)


    def mostrar_jogador(self, jogador):

        texto = f"""

🎾 {jogador.nome}

🏆 Ranking: {jogador.ranking}

🌎 Nacionalidade: {jogador.nacionalidade}

🎂 Idade: {jogador.idade}

🏅 Pontos: {jogador.pontos}

✔ Vitórias: {jogador.vitorias}

✖ Derrotas: {jogador.derrotas}

❤️ Stamina: {jogador.stamina}

💪 Físico: {jogador.fisico}

🎾 Saibro: {jogador.habilidades[Superficie.SAIBRO]}

🌱 Grama: {jogador.habilidades[Superficie.GRAMA]}

🏟 Hard: {jogador.habilidades[Superficie.HARD]}

📈 Aproveitamento:

{jogador.calcular_desempenho():.2f} %

"""

        messagebox.showinfo(
            "Jogador",
            texto
        )

    def editar_jogador(self, jogador):

        janela = ctk.CTkToplevel(self)

        janela.title("Editar Jogador")

        janela.geometry("450x620")

        janela.grab_set()

        campos = {}

        dados = [

            ("Nome", jogador.nome),

            ("Idade", jogador.idade),

            ("Nacionalidade", jogador.nacionalidade),

            ("Saibro", jogador.habilidades[Superficie.SAIBRO]),

            ("Grama", jogador.habilidades[Superficie.GRAMA]),

            ("Hard", jogador.habilidades[Superficie.HARD]),

            ("Stamina", jogador.stamina),

            ("Físico", jogador.fisico)

        ]

        for texto, valor in dados:

            ctk.CTkLabel(

                janela,

                text=texto

            ).pack(pady=(12,2))

            entrada = ctk.CTkEntry(janela)

            entrada.insert(0, str(valor))

            entrada.pack(

                fill="x",

                padx=30

            )

            campos[texto] = entrada

        def salvar():

            try:

                self.sistema.editar_jogador(

                    jogador,

                    campos["Nome"].get(),

                    int(campos["Idade"].get()),

                    campos["Nacionalidade"].get(),

                    int(campos["Saibro"].get()),

                    int(campos["Grama"].get()),

                    int(campos["Hard"].get()),

                    int(campos["Stamina"].get()),

                    int(campos["Físico"].get())

                )

                self.atualizar_lista()

                janela.destroy()

                messagebox.showinfo(

                    "Sucesso",

                    "Jogador atualizado."

                )

            except Exception as erro:

                messagebox.showerror(

                    "Erro",

                    str(erro)

                )

        ctk.CTkButton(

            janela,

            text="Salvar Alterações",

            command=salvar

        ).pack(pady=25)

    def excluir_jogador(self, jogador):

        resposta = messagebox.askyesno(
            "Excluir",
            f"Deseja excluir {jogador.nome}?"
        )

        if not resposta:
            return

        try:

            self.sistema.excluir_jogador(jogador)

            self.atualizar_lista()

            messagebox.showinfo(
                "Sucesso",
                "Jogador removido."
            )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )