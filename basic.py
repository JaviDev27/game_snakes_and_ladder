class Mascota:

    def __init__(self, color, tamano, nombre):
        self.color = color
        self.tamano = tamano
        self.nombre = nombre

    def caminar(self):
        print(self.nombre + " esta caminando")


if __name__ == "__main__":
    Gato = Mascota(color="cafe", tamano="40cm", nombre="mimi")
    Perro = Mascota(color="cafe", tamano="60cm", nombre="MAX")

    print(Gato.nombre)
    print(Perro.nombre)

    Gato.caminar()
    Perro.caminar()
