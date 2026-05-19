from utils.enums import Superficie
from .Pessoa import Pessoa
from .Competidor import Competidor


class Jogador(Pessoa, Competidor):

    def __init__(
        self,
        nome,
        idade,
        nacionalidade,
        habilidade_saibro,
        habilidade_grama,
        habilidade_hard
    ):

        super().__init__(nome, idade, nacionalidade)

        # ESTATÍSTICAS

        self.__pontos = 0
        self.__ranking = 999
        self.__vitorias = 0
        self.__derrotas = 0
        self.__titulos = 0

        # ATRIBUTOS DE JOGO

        self.__stamina = 100
        self.__fisico = 70

        self.habilidades = {
            Superficie.SAIBRO: habilidade_saibro,
            Superficie.GRAMA: habilidade_grama,
            Superficie.HARD: habilidade_hard
        }

        # HISTÓRICO

        self.__historico = []

    # GETTERS

    @property
    def pontos(self):
        return self.__pontos

    @property
    def ranking(self):
        return self.__ranking

    @property
    def vitorias(self):
        return self.__vitorias

    @property
    def derrotas(self):
        return self.__derrotas

    @property
    def stamina(self):
        return self.__stamina

    @property
    def fisico(self):
        return self.__fisico
    
    @property
    def historico(self):
        return self.__historico
    
    @property
    def titulos(self):
        return self.__titulos

    # SETTERS

    @ranking.setter
    def ranking(self, novo_ranking):

        if novo_ranking <= 0:
            raise ValueError("Ranking inválido.")

        self.__ranking = novo_ranking

    # MÉTODOS

    def adicionar_vitoria(self):

        self.__vitorias += 1

        self.__fisico += 2

        if self.__fisico > 100:
            self.__fisico = 100

    def adicionar_derrota(self):

        self.__derrotas += 1

        self.__fisico -= 3

        if self.__fisico < 0:
            self.__fisico = 0

    def ganhar_pontos(self, pontos):

        self.__pontos += pontos

    def perder_stamina(self, valor):

        self.__stamina -= valor

        if self.__stamina < 0:
            self.__stamina = 0

    def recuperar_stamina(self):

        self.__stamina += 10

        if self.__stamina > 100:
            self.__stamina = 100

    def treinar(self):

        self.__fisico += 5

        self.__stamina -= 3

        if self.__fisico > 100:
            self.__fisico = 100

        print(f"{self.nome} treinou intensamente.")

    def calcular_desempenho(self):

        total = self.__vitorias + self.__derrotas

        if total == 0:
            return 0

        return round((self.__vitorias / total) * 100, 2)

    def registrar_partida(self, resultado):

        self.__historico.append(resultado)

    def mostrar_estatisticas(self):

        return (
            f"\n===== ESTATÍSTICAS =====\n"
            f"Jogador: {self.nome}\n"
            f"Ranking: {self.__ranking}\n"
            f"Pontos: {self.__pontos}\n"
            f"Vitórias: {self.__vitorias}\n"
            f"Derrotas: {self.__derrotas}\n"
            f"Aproveitamento: {self.calcular_desempenho()}%\n"
            f"Stamina atual: {self.__stamina}\n"
            f"Fisico atual: {self.__fisico}\n"
        )

    def mostrar_info(self):

        info_base = super().mostrar_info()

        return (
            f"{info_base}\n"
            f"Ranking: {self.__ranking}\n"
            f"Pontos: {self.__pontos}"
        )

    def __str__(self):

        return (
            f"{self.ranking}° - "
            f"{self.nome} "
            f"({self.pontos} pts)"
        )
    
