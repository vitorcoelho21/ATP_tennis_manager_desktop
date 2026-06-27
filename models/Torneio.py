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

    def gerar_chave(self, competidores):
        if len(competidores) < 2:
            raise ValueError("É necessário pelo menos 2 jogadores para gerar a chave.")
        elif len(competidores) % 2 != 0:
            raise ValueError("Número de jogadores deve ser par para gerar a chave.")
        jogadores_embaralhados = competidores.copy()
        partidas_rodada = []
        random.shuffle(jogadores_embaralhados)
        for i in range(0, len(jogadores_embaralhados), 2):
            jogador1 = jogadores_embaralhados[i]
            jogador2 = jogadores_embaralhados[i + 1]
            partida = Partida(jogador1, jogador2, self.superficie)
            self.__partidas.append(partida)
            partidas_rodada.append(partida)
        return partidas_rodada
    
    def iniciar_torneio(self):
        self.__partidas.clear()
        partida_rodada = self.gerar_chave(self.__jogadores)
        vencedores = []
        for partida in partida_rodada:
            partida.simular()
            vencedores.append(partida.vencedor)
        
        while len(vencedores) > 1:
            partida_rodada = self.gerar_chave(vencedores)
            vencedores = []
            for partida in partida_rodada:
                partida.simular()
                vencedores.append(partida.vencedor)
        self.campeao = vencedores[0]
        self.campeao.adicionar_titulo(self.nome)
        self.campeao.ganhar_pontos(self.categoria.pontos)
        for jogador in self.__jogadores:
            jogador.recuperar_stamina()
        print(f"\nO campeão do {self.nome} é {self.campeao.nome}!")

    def __str__(self):
        return f"{self.nome} - {self.categoria.nome}"
