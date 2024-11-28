'''
Edison Francisco Uñog Valencia...

La división de higiene está trabajando en un control de stock para productos
sanitarios. Debemos realizar la carga de
una compra de productos de prevención de contagio, de cada una debe obtener los
siguientes datos:
· El tipo (&quot;barbijo&quot;, &quot;jabón&quot; o &quot;alcohol&quot;)
· El precio
· La cantidad de unidades
· La marca
· El fabricante
Se debe informar los datos de la compra procesados para poder iniciar el control de
stock.
'''

from os import system

system("cls")


print(" Productoa a ingresar: barbijo, jabon, alcohol")


tipo = str(input(" Ingresa primer producto: "))
while tipo != "barbijo":
    tipo = str(input(" Ingresa primer producto: "))

precio = float(input(" Ingresa Precio: "))
while precio != float(precio):
    precio = float(input(" Ingresa Precio: "))

cantidad_producto = int(input(" Ingresa cantidad: "))
while cantidad_producto != int(cantidad_producto):
    cantidad_producto = int(input(" Ingresa cantidad: "))

marca = str(input(" Ingresa marca: "))
while marca != str(marca):
    marca = str(input(" Ingresa marca: "))

fabricante = str(input(" Ingresa fabricante: "))   
while fabricante != str(fabricante):
    fabricante = str(input(" Ingresa fabricante: "))

################################################################

print(f" \n Producto: {tipo}")
print(f" Precio de {tipo} es: {precio}")
print(f" Cantidad de {tipo} son: {cantidad_producto}")
print(f" Marca de {tipo} es: {marca}")
print(f" Fabricante de {tipo} es: {fabricante}\n")