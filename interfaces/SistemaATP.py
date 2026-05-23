from models.Jogador import Jogador
from models.Ranking import Ranking

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
        