from Class_Transporte import Transporte
from Class_Caballo import Caballo
from Class_Auto import Auto

'''a_transporte = Transporte(5, 20)

a_transporte.avanzar()
a_transporte.mostrar()
a_transporte.frenar()'''

caballo_1 = Caballo(5, 20, "pura sangre", "negro")
caballo_1.set_km_totales(100)

auto_1 = Auto(12, 130, 4, "mustang")
auto_1.set_km_totales(500)

auto_2 = Auto(10, 200, 3, "ferrari")
auto_2.set_km_totales(1000)

caballo_2 = Caballo(4, 50, "fino", "marron")
caballo_2.set_km_totales(300)


caballo_1.avanzar(120)
auto_1.avanzar(120)
auto_2.avanzar(210)
caballo_2.avanzar(25)


lista_trasnporte = [caballo_1, auto_1, caballo_2, auto_2]

for x in lista_trasnporte:
    x.mostrar() #polimorfismo

