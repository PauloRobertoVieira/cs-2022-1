
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        return "som"


class Cachorro(Animal):
    def emitir_som(self):
        return "Som de cachorro latindo..."

    def correr(self):
        return "Cachorro correndo"


class Cavalo(Animal):
    def emitir_som(self):
        return "Som de cavalo relinxando...iiiirrirri"

    def correr(self):
        return "Cavalo correndo... pocoto, pocoto"


class Preguica(Animal):
    def emitir_som(self):
        return "Som Preguica"

    def subir_arvore(self):
        return "Preguica subindo na arvore..."


class Veterinario():
    def examinar(self, animal):
        print(animal.emitir_som())


class Zoologico:
