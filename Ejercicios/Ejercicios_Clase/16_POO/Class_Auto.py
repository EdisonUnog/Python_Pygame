from Class_Transporte import Transporte

class Auto(Transporte):
    def __init__(self, cantidad, velocidad, ruedas, marca) -> None:
        super().__init__(cantidad, velocidad)

        self._cant_ruedas = ruedas
        self._marca = marca

    def frenar(self):
        print("el Auto ")
        super().frenar()

    def avanzar(self, velocidad):
        print("El Auto ")
        super().avanzar(velocidad)

    def mostrar(self):
        super().mostrar()
        print(f"cantidad de ruedas: {self._cant_ruedas}, marca: {self._marca}")
        print("**************************************************")