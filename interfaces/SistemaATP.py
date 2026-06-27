import random

from models.Torneio import Torneio
from models.Jogador import Jogador
from models.Ranking import Ranking
from utils.enums import CategoriaTorneio, Superficie

class SistemaAtp:
    def __init__(self):
        self.jogadores = []
        self.ranking = Ranking()
        self.torneios = []

    def cadastrar_jogador(self, nome, idade, nacionalidade, habilidade_saibro, habilidade_grama, habilidade_hard):
        jogador = Jogador(nome, idade, nacionalidade, habilidade_saibro, habilidade_grama, habilidade_hard)
        self.jogadores.append(jogador)
        self.ranking.adicionar_jogador(jogador)

    def buscar_jogador(self, nome):
        for jogador in self.jogadores:
            if jogador.nome == nome:
                return jogador
        return None
    
    def get_ranking_geral(self):
        self.ranking.atualizar_ranking()
        return self.ranking.mostrar_ranking()
    
    def gerar_jogadores_teste(self):
        nomes = [
            "Djokovic", "Alcaraz", "Sinner", "Medvedev",
            "Zverev", "Rune", "Rublev", "Tsitsipas"
        ]

        for nome in nomes:
            self.cadastrar_jogador(
                nome,
                random.randint(18, 38),
                "Teste",
                random.randint(70, 100),
                random.randint(70, 100),
                random.randint(70, 100)
            )
    
    def gerar_torneios_teste(self):
        torneios = [
            ("Australian Open", CategoriaTorneio.GRAND_SLAM, Superficie.HARD),
            ("Roland Garros", CategoriaTorneio.GRAND_SLAM, Superficie.SAIBRO),
            ("Wimbledon", CategoriaTorneio.GRAND_SLAM, Superficie.GRAMA),
            ("US Open", CategoriaTorneio.GRAND_SLAM, Superficie.HARD),
            ("Indian Wells", CategoriaTorneio.MASTERS_1000, Superficie.HARD),
            ("Monte Carlo", CategoriaTorneio.MASTERS_1000, Superficie.SAIBRO),
            ("Queen's", CategoriaTorneio.ATP_500, Superficie.GRAMA),
            ("Doha", CategoriaTorneio.ATP_250, Superficie.HARD)
        ]

        for nome, categoria, superficie in torneios:
            self.torneios.append(
                Torneio(nome, categoria, superficie)
            )

    def gerar_temporada_teste(self):
        self.gerar_jogadores_teste()
        self.gerar_torneios_teste()

        for torneio in self.torneios:
            for jogador in self.jogadores:
                torneio.adicionar_jogador(jogador)

    def iniciar_torneio(self, torneio):
        torneio.iniciar_torneio()
        self.ranking.atualizar_ranking()

    def criar_torneio(self, nome, categoria, superficie):
        torneio = Torneio(nome, categoria, superficie)
        self.torneios.append(torneio)
        return torneio
        