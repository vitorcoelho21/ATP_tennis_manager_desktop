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
    
    def simular(self):
        if self._finalizada:
            raise Exception("Partida já foi finalizada.")
        forca_jogador1 = self.calcular_forca(self.jogador1)
        forca_jogador2 = self.calcular_forca(self.jogador2)
        diferenca = abs(forca_jogador1 - forca_jogador2)
        
    # Determina o vencedor com base na força calculada
        if forca_jogador1 > forca_jogador2:
            self._vencedor = self.jogador1
            self._perdedor = self.jogador2
        else:
            self._vencedor = self.jogador2
            self._perdedor = self.jogador1
        
        self._placar = self.gerar_placar(diferenca)
        self.atualizar_estatisticas(diferenca)
        self._finalizada = True

    def gerar_placar(self,diferenca):
        placares_equilibrados = [
            "7/6 6/7 7/5",
            "7/5 7/6",
            "6/4 3/6 7/6",
            "6/3 4/6 7/5",
            "7/6 6/4"
        ]
        placares_normais = [
            "6/4 6/3",
            "7/5 6/4",
            "6/3 3/6 6/2",
            "6/2 6/4",
            "6/4 6/3",
            "6/3 6/2"
        ]
        placares_desequilibrados = [
            "6/1 6/0",
            "6/2 6/1",
            "6/2 6/2",
            "6/3 6/1",
            "6/4 6/0",
            "6/0 6/0"
        ]
        if diferenca < 10:
            return random.choice(placares_equilibrados)
        elif diferenca < 20:
            return random.choice(placares_normais)
        else:            
            return random.choice(placares_desequilibrados)
        
    def mostrar_resultado(self):
        if not self._finalizada:
            raise ValueError("Partida ainda não foi finalizada.")
        return (f"===== RESULTADO =====\n"
            f"{self.jogador1.nome} vs {self.jogador2.nome}\n"
            f"Vencedor: {self._vencedor.nome}\n"
            f"Placar: {self._placar}\n"
            f"Superfície: {self.superficie.value}\n"
            f"======================")
    
    def atualizar_estatisticas(self,diferenca):
        self._vencedor.adicionar_vitoria()
        self._vencedor.ganhar_pontos(100)
        self._vencedor.historico.append(self)
        self._perdedor.adicionar_derrota()
        self._perdedor.historico.append(self)
        if diferenca < 10:
            self._vencedor.perder_stamina(random.randint(15, 20))
            self._perdedor.perder_stamina(random.randint(20, 25))
        elif diferenca < 20:
            self._vencedor.perder_stamina(random.randint(10, 15))
            self._perdedor.perder_stamina(random.randint(15, 20))
        else:
            self._vencedor.perder_stamina(random.randint(5, 10))
            self._perdedor.perder_stamina(random.randint(7, 12))
        

        
