from abc import ABC, abstractmethod
class Competidor(ABC):
    
    @abstractmethod
    def treinar(self):
        pass

    @abstractmethod
    def calcular_desempenho(self):
        pass

    @abstractmethod
    def mostrar_estatisticas(self):
        pass