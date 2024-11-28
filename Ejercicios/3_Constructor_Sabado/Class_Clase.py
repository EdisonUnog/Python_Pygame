

class Clase:
    def __init__(self, cambios, rodado) -> None:
        self.cambios = cambios
        self.rodado = rodado

    def mostra(self):
        print(f" *Cambios: {self.cambios}, Rodado: {self.rodado}")