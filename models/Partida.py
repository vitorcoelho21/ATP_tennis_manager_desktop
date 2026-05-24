import random
from utils.enums import Superficie
class Partida:
    def __init__(self, jogador1, jogador2, superficie):
        if jogador1 == jogador2:
            raise ValueError("Jogadores devem ser diferentes.")
        if not isinstance(superficie, Superficie):
            raise ValueError("Superfície deve ser: 'saibro', 'grama' ou 'hard'.")
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self._vencedor = None
        self.superficie = superficie
        self._placar = ""
        self._finalizada = False
        self._perdedor = None

    @property
    def placar(self):
        return self._placar
    @property
    def vencedor(self):
        return self._vencedor
    @property
    def perdedor(self):
        return self._perdedor
    @property
    def finalizada(self):
        return self._finalizada
    
    def calcular_forca(self, jogador):
        habilidade = jogador.habilidades[self.superficie]
        fisico = jogador.fisico
        stamina = jogador.stamina
        aleatorio = random.uniform(-5, 5)  # Introduz uma variação aleatória
        return habilidade * 0.5 + fisico * 0.3 + stamina * 0.2 + aleatorio
    
    def simular_game(self):
        forca_jogador1 = self.calcular_forca(self.jogador1)
        forca_jogador2 = self.calcular_forca(self.jogador2)
        total = forca_jogador1 + forca_jogador2
        probabilidade_jogador1 = forca_jogador1 / total
        if random.random() < probabilidade_jogador1:
            return self.jogador1
        else:            
            return self.jogador2

    def simular_set(self):
        games_jogador1 = 0
        games_jogador2 = 0
        while True:
            if games_jogador1 == 6 and games_jogador2 == 6:
                pontos_jogador1, pontos_jogador2 = self.simular_tiebreak()
                if pontos_jogador1 > pontos_jogador2:
                    games_jogador1 += 1
                else:
                    games_jogador2 += 1
                break
            vencedor_game = self.simular_game()
            if vencedor_game == self.jogador1:
                games_jogador1 += 1
            else:
                games_jogador2 += 1
            if (games_jogador1 >= 6 and games_jogador1 >= games_jogador2 + 2) or (games_jogador2 >= 6 and games_jogador2 >= games_jogador1 + 2):
                break
        return games_jogador1, games_jogador2

    def simular_tiebreak(self):
        pontos_jogador1 = 0
        pontos_jogador2 = 0
        while True:
            vencedor_ponto = self.simular_game()
            if vencedor_ponto == self.jogador1:
                pontos_jogador1 += 1
            else:
                pontos_jogador2 += 1
            if (pontos_jogador1 >= 7 and pontos_jogador1 >= pontos_jogador2 + 2) or (pontos_jogador2 >= 7 and pontos_jogador2 >= pontos_jogador1 + 2):
                break
        return pontos_jogador1, pontos_jogador2
    
    def simular(self):
        if self._finalizada:
            raise Exception("Partida já foi finalizada.")
        jogador1_sets = 0
        jogador2_sets = 0
        placar_sets = []
        total_games = 0
        total_sets = 0
        while True:
            games1, games2 = self.simular_set()
            total_games += games1 + games2
            total_sets += 1
            if games1 > games2:
                jogador1_sets += 1
            else:
                jogador2_sets += 1
            placar_sets.append(f"{games1}/{games2}")
            if jogador1_sets == 2 or jogador2_sets == 2:
                if jogador1_sets > jogador2_sets:
                    self._vencedor = self.jogador1
                    self._perdedor = self.jogador2
                else:                    
                    self._vencedor = self.jogador2
                    self._perdedor = self.jogador1
                break
        self._placar = " ".join(placar_sets)
        self.atualizar_estatisticas(total_games, total_sets)
        self._finalizada = True

    
    def mostrar_resultado(self):
        if not self._finalizada:
            raise ValueError("Partida ainda não foi finalizada.")
        return (f"===== RESULTADO =====\n"
            f"{self.jogador1.nome} vs {self.jogador2.nome}\n"
            f"Vencedor: {self._vencedor.nome}\n"
            f"Placar: {self._placar}\n"
            f"Superfície: {self.superficie.value}\n"
            f"======================")
    
    def atualizar_estatisticas(self, qtd_games, qtd_sets):
        self._vencedor.adicionar_vitoria()
        self._vencedor.ganhar_pontos(100)
        self._vencedor.historico.append(self)
        self._perdedor.adicionar_derrota()
        self._perdedor.historico.append(self)
        desgaste = qtd_games // 2
        if qtd_sets == 3:
            desgaste += 5
        elif qtd_sets == 2:
            desgaste += 3
        self._vencedor.perder_stamina(desgaste)
        self._perdedor.perder_stamina(desgaste + 4)