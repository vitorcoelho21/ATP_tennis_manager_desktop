import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox


class JogadoresPage(ctk.CTkFrame):

    def __init__(self, master, sistema):

        super().__init__(master)

        self.sistema = sistema

        titulo = ctk.CTkLabel(
            self,
            text="Gerenciamento de Jogadores",
            font=("Segoe UI", 24, "bold")
        )

        titulo.pack(pady=20)

        self.criar_barra_superior()

        self.criar_tabela()

        self.atualizar_lista()
    
    def criar_barra_superior(self):

        frame = ctk.CTkFrame(self)

        frame.pack(fill="x", padx=20)

        self.pesquisa = ctk.CTkEntry(
            frame,
            placeholder_text="Pesquisar jogador..."
        )

        self.pesquisa.pack(
            side="left",
            padx=10,
            pady=10,
            fill="x",
            expand=True
        )

        ctk.CTkButton(
            frame,
            text="Pesquisar",
            command=self.pesquisar
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            frame,
            text="Novo Jogador",
            command=self.novo_jogador
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            frame,
            text="Atualizar",
            command=self.atualizar_lista
        ).pack(side="left", padx=5)
    
    def criar_tabela(self):

        frame = ctk.CTkFrame(self)

        frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        colunas = (
            "Ranking",
            "Nome",
            "Pontos",
            "Vitórias",
            "Derrotas",
            "Stamina"
        )

        self.tree = ttk.Treeview(
            frame,
            columns=colunas,
            show="headings",
            height=18
        )

        for coluna in colunas:

            self.tree.heading(coluna, text=coluna)

            self.tree.column(
                coluna,
                anchor="center",
                width=120
            )

        self.tree.pack(
            fill="both",
            expand=True
        )

        self.tree.bind(
            "<Double-1>",
            self.mostrar_jogador
        )    

    def atualizar_lista(self):

        self.sistema.ranking.atualizar_ranking()

        for item in self.tree.get_children():

            self.tree.delete(item)

        for jogador in self.sistema.ranking.jogadores:

            self.tree.insert(
                "",
                "end",
                values=(
                    jogador.ranking,
                    jogador.nome,
                    jogador.pontos,
                    jogador.vitorias,
                    jogador.derrotas,
                    jogador.stamina
                )
            )

    def pesquisar(self):

        nome = self.pesquisa.get()

        jogador = self.sistema.buscar_jogador(nome)

        if jogador is None:

            messagebox.showerror(
                "Erro",
                "Jogador não encontrado."
            )

            return

        for item in self.tree.get_children():

            self.tree.delete(item)

        self.tree.insert(
            "",
            "end",
            values=(
                jogador.ranking,
                jogador.nome,
                jogador.pontos,
                jogador.vitorias,
                jogador.derrotas,
                jogador.stamina
            )
        )

    def novo_jogador(self):

        messagebox.showinfo(
            "Em desenvolvimento",
            "Tela de cadastro será implementada."
        )

    def mostrar_jogador(self, event):

        item = self.tree.focus()

        if not item:

            return

        dados = self.tree.item(item)["values"]

        nome = dados[1]

        jogador = self.sistema.buscar_jogador(nome)

        texto = f"""
Nome: {jogador.nome}

Ranking: {jogador.ranking}

Pontos: {jogador.pontos}

Vitórias: {jogador.vitorias}

Derrotas: {jogador.derrotas}

Stamina: {jogador.stamina}

Físico: {jogador.fisico}

Aproveitamento: {jogador.calcular_desempenho()}%
"""

        messagebox.showinfo(
            "Estatísticas",
            texto
        )
    
