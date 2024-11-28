from Class_Transporte import Transporte

class Auto(Transporte):
    def __init__(self, cantidad: int, velocidad: float, ruedas, marca):
        super().__init__(cantidad, velocidad)
        self._cantidad_ruedas = ruedas
        self.marca = marca

    def frenar(self):
        print(f"El auto: {self.marca}")
        super().frenar()

    def avanzar(self):
        print(f"*el auto: {self.marca}")
        super().avanzar()

    def tocar_bocina(self):
        print(" ****bocinaaaaa")

    def mostra(self):
        super().mostrar()
        print(f" *Cant_Ruedas{self._cantidad_ruedas}, Marca: {self.marca}")
