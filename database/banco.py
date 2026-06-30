import os
import sqlite3
from utils.enums import Superficie

class Banco:
    def __init__(self):
        caminho = os.path.join(
        os.path.dirname(__file__),
        "tennis.db"
        )
        self.conexao = sqlite3.connect(caminho)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

    def criar_tabelas(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS jogadores(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT UNIQUE,
                idade INTEGER,
                nacionalidade TEXT,
                saibro INTEGER,
                grama INTEGER,
                hard INTEGER,
                pontos INTEGER,
                ranking INTEGER,
                vitorias INTEGER,
                derrotas INTEGER,
                stamina INTEGER,
                fisico INTEGER
            )
        """)

        self.conexao.commit()
    
    def salvar_jogador(self, jogador):
        try:
            self.cursor.execute("""
                INSERT INTO jogadores(
                    nome,
                    idade,
                    nacionalidade,
                    saibro,
                    grama,
                    hard,
                    pontos,
                    ranking,
                    vitorias,
                    derrotas,
                    stamina,
                    fisico
                )
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
            """, (
                jogador.nome,
                jogador.idade,
                jogador.nacionalidade,
                jogador.habilidades[Superficie.SAIBRO],
                jogador.habilidades[Superficie.GRAMA],
                jogador.habilidades[Superficie.HARD],
                jogador.pontos,
                jogador.ranking,
                jogador.vitorias,
                jogador.derrotas,
                jogador.stamina,
                jogador.fisico
            ))

            jogador.id = self.cursor.lastrowid
            self.conexao.commit()

        except sqlite3.IntegrityError:
            print("Jogador já existe no banco.")

    def carregar_jogadores(self):
        self.cursor.execute("SELECT * FROM jogadores")
        return self.cursor.fetchall()

    def atualizar_jogador(self, jogador):
        self.cursor.execute("""
            UPDATE jogadores
            SET idade = ?,
                nacionalidade = ?,
                saibro = ?,
                grama = ?,
                hard = ?,
                pontos = ?,
                ranking = ?,
                vitorias = ?,
                derrotas = ?,
                stamina = ?,
                fisico = ?
            WHERE id = ?
        """, (
            jogador.idade,
            jogador.nacionalidade,
            jogador.habilidades[Superficie.SAIBRO],
            jogador.habilidades[Superficie.GRAMA],
            jogador.habilidades[Superficie.HARD],
            jogador.pontos,
            jogador.ranking,
            jogador.vitorias,
            jogador.derrotas,
            jogador.stamina,
            jogador.fisico,
            jogador.id
        ))

        self.conexao.commit()
    
    def remover_jogador(self, jogador):
        self.cursor.execute(
            "DELETE FROM jogadores WHERE id = ?",
            (jogador.id,)
        )
        self.conexao.commit()