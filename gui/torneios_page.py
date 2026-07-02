import customtkinter as ctk
from tkinter import messagebox

from utils.enums import CategoriaTorneio, Superficie
from gui.styles import Cores


class TorneiosPage(ctk.CTkFrame):

    def __init__(self, master, sistema):

        super().__init__(master, fg_color=Cores.FUNDO)

        self.sistema = sistema

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.criar_topo()
        self.criar_barra_ferramentas()
        self.criar_lista()

        self.atualizar_lista()

    def criar_topo(self):

        frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=25,
            pady=(20,10)
        )

        titulo = ctk.CTkLabel(

            frame,

            text="🏆 Torneios",

            font=("Segoe UI",30,"bold")

        )

        titulo.pack(side="left")

    def criar_barra_ferramentas(self):

        barra = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        barra.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=25,
            pady=10
        )

        self.busca = ctk.CTkEntry(

            barra,

            width=300,

            placeholder_text="Pesquisar torneio..."

        )

        self.busca.pack(
            side="left",
            padx=(0,10)
        )

        ctk.CTkButton(

            barra,

            text="Pesquisar",

            width=120,

            command=self.pesquisar

        ).pack(side="left")

        ctk.CTkButton(

            barra,

            text="Novo Torneio",

            width=140,

            command=self.criar_torneio

        ).pack(
            side="right"
        )


    def criar_lista(self):

        self.scroll = ctk.CTkScrollableFrame(

            self,

            fg_color="transparent"

        )

        self.scroll.grid(

            row=2,

            column=0,

            sticky="nsew",

            padx=20,

            pady=10

        )

    def atualizar_lista(self):

        for widget in self.scroll.winfo_children():

            widget.destroy()

        torneios = self.sistema.torneios

        texto = self.busca.get().lower()

        if texto:

            torneios = [

                t for t in torneios

                if texto in t.nome.lower()

            ]

        if not torneios:

            vazio = ctk.CTkLabel(

                self.scroll,

                text="Nenhum torneio encontrado.",

                font=("Segoe UI",18)

            )

            vazio.pack(pady=50)

            return

        for torneio in torneios:

            self.criar_card(torneio)

    def criar_card(self, torneio):

        card = ctk.CTkFrame(

            self.scroll,

            corner_radius=15

        )

        card.pack(

            fill="x",

            padx=10,

            pady=10

        )

        titulo = ctk.CTkLabel(

            card,

            text=f"🏆 {torneio.nome}",

            font=("Segoe UI",22,"bold")

        )

        titulo.pack(

            anchor="w",

            padx=20,

            pady=(15,5)

        )

        categoria = ctk.CTkLabel(

            card,

            text=f"Categoria: {torneio.categoria.nome}"

        )

        categoria.pack(

            anchor="w",

            padx=20

        )

        superficie = ctk.CTkLabel(

            card,

            text=f"Superfície: {torneio.superficie.value}"

        )

        superficie.pack(

            anchor="w",

            padx=20

        )

        inscritos = ctk.CTkLabel(

            card,

            text=f"Jogadores inscritos: {len(torneio.jogadores)}"

        )

        inscritos.pack(

            anchor="w",

            padx=20,

            pady=(0,10)

        )

        if torneio.campeao:

            campeao = torneio.campeao.nome

        else:

            campeao = "Ainda não definido"

        ctk.CTkLabel(

            card,

            text=f"Campeão: {campeao}"

        ).pack(

            anchor="w",

            padx=20,

            pady=(0,10)

        )

        botoes = ctk.CTkFrame(

            card,

            fg_color="transparent"

        )

        botoes.pack(

            fill="x",

            padx=15,

            pady=15

        )

        ctk.CTkButton(

            botoes,

            text="➕ Jogador",

            width=120,

            command=lambda t=torneio: self.adicionar_jogador(t)

        ).pack(side="left", padx=5)

        ctk.CTkButton(

            botoes,

            text="▶ Iniciar",

            width=120,

            command=lambda t=torneio: self.iniciar_torneio(t)

        ).pack(side="left", padx=5)

        ctk.CTkButton(

            botoes,

            text="ℹ Detalhes",

            width=120,

            command=lambda t=torneio: self.detalhes_torneio(t)

        ).pack(side="left", padx=5)

        ctk.CTkButton(

            botoes,

            text="🗑 Excluir",

            width=120,

            fg_color="#b91c1c",

            hover_color="#991b1b",

            command=lambda t=torneio: self.excluir_torneio(t)

        ).pack(side="right")

    def pesquisar(self):

        self.atualizar_lista()


    def excluir_torneio(self, torneio):

        confirmar = messagebox.askyesno(

            "Excluir",

            f"Excluir o torneio\n\n{torneio.nome}?"

        )

        if not confirmar:

            return

        self.sistema.excluir_torneio(torneio)

        self.atualizar_lista()


    def detalhes_torneio(self, torneio):

        texto = ""

        texto += f"Nome: {torneio.nome}\n"

        texto += f"Categoria: {torneio.categoria.nome}\n"

        texto += f"Superfície: {torneio.superficie.value}\n\n"

        texto += "Jogadores inscritos:\n\n"

        if torneio.jogadores:

            for jogador in torneio.jogadores:

                texto += f"• {jogador.nome}\n"

        else:

            texto += "Nenhum jogador."

        if torneio.campeao:

            texto += f"\n\nCampeão:\n{torneio.campeao.nome}"

        messagebox.showinfo(

            "Detalhes",

            texto

        )


    def iniciar_torneio(self, torneio):

        try:

            self.sistema.iniciar_torneio(torneio)

            messagebox.showinfo(

                "Sucesso",

                f"{torneio.campeao.nome} venceu o {torneio.nome}!"

            )

        except Exception as erro:

            messagebox.showerror(

                "Erro",

                str(erro)

            )

        self.atualizar_lista()


    def adicionar_jogador(self, torneio):

        janela = ctk.CTkToplevel(self)

        janela.title("Adicionar Jogador")

        janela.geometry("420x500")

        janela.grab_set()

        ctk.CTkLabel(

            janela,

            text="Escolha um jogador",

            font=("Segoe UI",22,"bold")

        ).pack(pady=20)

        frame = ctk.CTkScrollableFrame(

            janela,

            width=350,

            height=320

        )

        frame.pack(

            padx=20,

            pady=10,

            fill="both",

            expand=True

        )

        for jogador in self.sistema.ranking.jogadores:

            ctk.CTkButton(

                frame,

                text=jogador.nome,

                command=lambda j=jogador: self.inscrever_jogador(

                    torneio,

                    j,

                    janela

                )

            ).pack(

                fill="x",

                pady=5

            )

    def inscrever_jogador(

        self,

        torneio,

        jogador,

        janela

    ):

        try:

            self.sistema.inscrever_jogador(torneio, jogador)

            messagebox.showinfo(

                "Sucesso",

                f"{jogador.nome} inscrito."

            )

            janela.destroy()

            self.atualizar_lista()

        except Exception as erro:

            messagebox.showerror(

                "Erro",

                str(erro)

            )

    def criar_torneio(self):

        janela = ctk.CTkToplevel(self)

        janela.title("Novo Torneio")

        janela.geometry("420x420")

        janela.grab_set()

        ctk.CTkLabel(

            janela,

            text="Criar Torneio",

            font=("Segoe UI",24,"bold")

        ).pack(pady=20)

        nome = ctk.CTkEntry(

            janela,

            width=300,

            placeholder_text="Nome do torneio"

        )

        nome.pack(pady=10)

        categoria = ctk.CTkComboBox(

            janela,

            width=300,

            values=[

                "GRAND SLAM",

                "MASTERS 1000",

                "ATP 500",

                "ATP 250"

            ]

        )

        categoria.pack(pady=10)

        categoria.set("ATP 250")

        superficie = ctk.CTkComboBox(

            janela,

            width=300,

            values=[

                "SAIBRO",

                "GRAMA",

                "HARD"

            ]

        )

        superficie.pack(pady=10)

        superficie.set("HARD")

        ctk.CTkButton(

            janela,

            text="Criar",

            width=180,

            command=lambda: self.salvar_torneio(

                janela,

                nome.get(),

                categoria.get(),

                superficie.get()

            )

        ).pack(pady=25)

    def salvar_torneio(

        self,

        janela,

        nome,

        categoria,

        superficie

    ):

        if nome.strip() == "":

            messagebox.showwarning(

                "Aviso",

                "Digite um nome."

            )

            return

        categorias = {

            "GRAND SLAM": CategoriaTorneio.GRAND_SLAM,

            "MASTERS 1000": CategoriaTorneio.MASTERS_1000,

            "ATP 500": CategoriaTorneio.ATP_500,

            "ATP 250": CategoriaTorneio.ATP_250

        }

        superficies = {

            "SAIBRO": Superficie.SAIBRO,

            "GRAMA": Superficie.GRAMA,

            "HARD": Superficie.HARD

        }

        try:

            self.sistema.criar_torneio(

                nome,

                categorias[categoria],

                superficies[superficie]

            )

        except Exception as erro:

            messagebox.showerror(

                "Erro",

                str(erro)

            )

            return

        janela.destroy()

        self.atualizar_lista()

        messagebox.showinfo(

            "Sucesso",

            "Torneio criado com sucesso!"

        )