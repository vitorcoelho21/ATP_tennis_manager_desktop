class Ranking:
    def __init__(self):
        self.__jogadores = []

    @property
    def jogadores(self):
        return self.__jogadores

    def adicionar_jogador(self, jogador):
        if jogador not in self.__jogadores:
            self.__jogadores.append(jogador)
    
    def remover_jogador(self, jogador):

        self.__jogadores = [
            j for j in self.__jogadores
            if j.id != jogador.id
        ]
    
    def atualizar_ranking(self):
        self.__jogadores.sort(key=lambda j: j.pontos, reverse=True)

        for i, jogador in enumerate(self.__jogadores, start=1):
            jogador.ranking = i
    def mostrar_ranking(self):
        if not self.__jogadores:
            return "Ranking vazio."
        texto = "\n===== RANKING MUNDIAL =====\n"
        for jogador in self.__jogadores:
            texto += f"{jogador.ranking}. {jogador.nome} - {jogador.pontos} pontos\n"
        return texto
    
    def mostrar_top10(self):
        if not self.__jogadores:
            return "Ranking vazio."
        texto = "\n===== TOP 10 RANKING MUNDIAL =====\n"
        for jogador in self.__jogadores[:10]:
            texto += f"{jogador.ranking}. {jogador.nome} - {jogador.pontos} pontos\n"
        return texto
    