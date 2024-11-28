
from Class_Auto import Auto
from Class_Bicicleta import Bicicleta
from Class_Clase import Clase

mi_auto1 = Auto(4, 34, 4, "mustang")
mi_bici1 = Bicicleta(2, 20, 16, 24)
mi_auto2 = Auto(5, 30, 4, "Ferrari")
mi_bici2 = Bicicleta(3, 30, 8, 10)

mi_clase = Clase(65, 97)
mi_clase.mostra()

mi_lista = [mi_auto1, mi_bici1, mi_auto2, mi_bici2]

for x in mi_lista:
    x.mostra()
    if (type(x) == Auto):
        x.tocar_bocina()


