class Pessoa:
    def __init__(self, nome, idade,nacionalidade):
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade

    @property
    def nome(self):
        return self._nome
    @property
    def idade(self):
        return self._idade
    @property
    def nacionalidade(self):       
        return self._nacionalidade
    
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

    @nacionalidade.setter
    def nacionalidade(self, value):
        if not value:
            raise ValueError("A nacionalidade deve ser preenchida.")
        self._nacionalidade = value
    
    def mostrar_info(self):
        print(f"Nome: {self.nome}\n")
        print(f"Idade: {self.idade}\n")
        print(f"Nacionalidade: {self.nacionalidade}")
    
    def __str__(self):
        return f"Nome: {self.nome} ({self.nacionalidade})"