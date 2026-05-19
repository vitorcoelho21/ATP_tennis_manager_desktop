from enum import Enum

class Superficie(Enum):
    SAIBRO = "saibro"
    GRAMA = "grama"
    HARD = "hard"

class EstadoPartida(Enum):
    NAO_INICIADA = 1
    EM_ANDAMENTO = 2
    FINALIZADA = 3

class CategoriaTorneio(Enum):
    GRAND_SLAM = ("GRAND SLAM", 2000)
    MASTERS_1000 = ("MASTERS 1000", 1000)
    ATP_500 = ("ATP 500", 500)
    ATP_250 = ("ATP 250", 250)

    @property
    def nome(self):
        return self.value[0]
    @property
    def pontos(self):
        return self.value[1]