from Class_Transporte import Transporte

class Bicicleta(Transporte):
    def __init__(self, cantidad: int, velocidad: float, cambios, rodado):
        super().__init__(cantidad, velocidad)
        self.cambios = cambios
        self.rodado = rodado

    def frenar(self):
        print(f"*La bicicleta rodado: {self.rodado}")
        super().frenar()

    def avanzar(self):
        print(f"*La bicicleta rodado: {self.rodado}")
        super().avanzar()

    def mostra(self):
        super().mostrar()
        print(f" *Cambios: {self.cambios}, Rodado: {self.rodado}")