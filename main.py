from models.Jogador import Jogador
from models.Partida import Partida
from utils.enums import Superficie


jogador1 = Jogador(
    "Novak Djokovic",
    38,
    "Sérvia",
    88,
    97,
    95
)

jogador2 = Jogador(
    "Rafael Nadal",
    39,
    "Espanha",
    99,
    85,
    89
)


print(jogador1.mostrar_estatisticas())
print(jogador2.mostrar_estatisticas())


partida = Partida(
    jogador1,
    jogador2,
    Superficie.SAIBRO
)

partida.simular()


print(partida.mostrar_resultado())


print(jogador1.mostrar_estatisticas())
print(jogador2.mostrar_estatisticas())