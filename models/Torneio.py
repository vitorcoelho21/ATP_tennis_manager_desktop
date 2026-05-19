import random
from models.Partida import Partida
from utils.enums import Superficie
from utils.enums import CategoriaTorneio
class Torneio:
    def __init__(self, nome, categoria, superficie):
        self.nome = nome
        self.categoria = categoria
        self.superficie = superficie
        self.__jogadores = []
        self.__partidas = []
        self.campeao = None

    @property
    def jogadores(self):
        return self.__jogadores.copy()
    
    @property
    def partidas(self):
        return self.__partidas.copy()
    
    def adicionar_jogador(self, jogador):
        if jogador in self.__jogadores:
            raise ValueError("Jogador já está inscrito no torneio.")
        self.__jogadores.append(jogador)

    def gerar_chave(self):
        if len(self.__jogadores) < 2:
            raise ValueError("É necessário pelo menos 2 jogadores para gerar a chave.")
        elif len(self.__jogadores) % 2 != 0:
            raise ValueError("Número de jogadores deve ser par para gerar a chave.")
        jogadores_embaralhados = self.__jogadores.copy()
        random.shuffle(jogadores_embaralhados)
        for i in range(0, len(jogadores_embaralhados), 2):
            jogador1 = jogadores_embaralhados[i]
            jogador2 = jogadores_embaralhados[i + 1]
            partida = Partida(jogador1, jogador2, self.superficie)
            self.__partidas.append(partida)

    
