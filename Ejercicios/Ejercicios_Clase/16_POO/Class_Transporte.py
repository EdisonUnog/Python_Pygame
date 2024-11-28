
class Transporte:
    def __init__(self, cantidad, velocidad) -> None:
        self._new_cantidad = cantidad
        self._new_velocidad = velocidad
        self._km_totales = 0
        self._leng_recorrido = 0

    def frenar(self):
        print("esta frenando")

    def avanzar(self, velocidad):
        if velocidad <= self._new_velocidad:
            print("Esta avanzando")
            self._leng_recorrido += velocidad
        else:
            print("limite de velocidad superados")

    def mostrar(self):
        print(f"*********{type(self)}************")
        print(f"""\nCantidad: {self._new_cantidad}, Velocidad: {self._new_velocidad}, 
                destino: {self._km_totales}, Restan: {self.get_distancia()}""")

    
    def set_km_totales(self, valor):
        self._km_totales = valor

    def set_leng_recorrido(self, valor):
        self._leng_recorrido = valor

    def get_distancia(self):
        return self._km_totales - self._leng_recorrido