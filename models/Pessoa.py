class Pessoa:
    def __init__(self, nome, idade,nacionaldade):
        self.nome = nome
        self.idade = idade
        self.nacionaldade = nacionaldade

    @property
    def nome(self):
        return self._nome
    @property
    def idade(self):
        return self._idade
    @property
    def nacionaldade(self):       
        return self._nacionaldade
    
    @nome.setter
    def nome(self, value):
        if not value:
            raise ValueError("O nome deve ser preenchido.")
        self._nome = value

    @idade.setter
    def idade(self, value):
        if not value:
            raise ValueError("A idade deve ser preenchida.")
        self._idade = value

    @nacionaldade.setter
    def nacionaldade(self, value):
        if not value:
            raise ValueError("A nacionalidade deve ser preenchida.")
        self._nacionaldade = value
    
    def mostrar_info(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Nacionalidade: {self.nacionaldade}")
    
    def __str__(self):
        return f"Nome: {self.nome} ({self.nacionaldade})"