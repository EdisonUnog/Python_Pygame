'''
Edison Francisco Uñog Valencia...

La división de alimentos está trabajando en un pequeño software para cargar las
compras de ingredientes para la cocina de Industrias Wayne.
Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
para preparar comida al por mayor. En total, sabemos que se realizarán 15 compras
de ingredientes.
Se registra por cada compra:
 1. PESO: (entre 10 y 100 kilos)
 2. PRECIO POR KILO: (mayor a 0 [cero]).
 3. TIPO VARIEDAD: (vegetal, animal, mezcla).
Además tener en cuenta que si compro más de 100 kilos en total tengo un 15% de
descuento sobre el precio bruto, o si compro más de 300 kilos en total, tengo un 25%
de descuento sobre el precio bruto.
Se desea saber:
 A. El importe total a pagar, BRUTO sin descuento.
 B. El importe total a pagar con descuento (Solo si corresponde).
 C. Informar el tipo de alimento más caro
'''

from os import system

system("cls")

num_productos = 2

for i in range(num_productos):

    peso = int(input("\n Ingresa peso entre 10 y 100kg: "))
    while peso < 10:
        print("\n Error")
        peso = int(input(" Ingresa peso entre 10 y 100kg: "))

    precio_kilo = float(input(" Ingresa precio por kilo: "))
    while precio_kilo < 0:
        print("\n Error")
        precio_kilo = float(input(" Ingresa precio por kilo: "))

    tipo = input(" Tipo de producto._ vegetal, animal, mezcla: ")
    while tipo != "vegetal" and tipo != "animal" and tipo != "mezcla":
        print("\n Error")
        tipo = input(" Tipo de producto._ vegetal, animal, mezcla: ")

    if peso > 100:
        descuento = (15 / 100) * precio_kilo
        total_con_aumento = precio_kilo + descuento
        print(f"\n precio con el 15%: {total_con_aumento}")
    
    elif peso > 300:
        descuento = (25 / 100) * precio_kilo
        total_con_aumento = precio_kilo + descuento
        print(f"\n precio con el 25%: {total_con_aumento}")


print(f"\n peso ingresados: {peso}")

#print(f"\n sume de los numero  es {acum_numeroDos}\n")