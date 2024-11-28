tipo_producto = " "
precio_producto = -1
cantidad = -1
marca = " "
fabricante = " "
barbijo_mas_caro = 0
cantidad_barbijo_caro = 0
fabricante_barbijo_caro = " "
item_mas_unidades = 0
fabricante_mas_unidades = " "
unidades_jabon_total  = 0


for iteracion in range(5):
    
    while(True):
        tipo_producto = input("Ingrese el tipo de producto : ")
        if tipo_producto == "barbijo" or tipo_producto == "jabon" or tipo_producto == "alcohol":
            break
    while(True):
        precio_producto = int(input("Ingrese el precio : "))
        if precio_producto > 99 and precio_producto < 301:
            break
    while (True):
        cantidad = int(input("Ingrese la cantidad de productos : "))
        if cantidad > 0 and cantidad < 1001:
            break
    marca = input("Ingrese la marca : ")
    fabricante = input("Ingrese el fabricante : ")

    if tipo_producto == "barbijo":
        if precio_producto > barbijo_mas_caro :
            barbijo_mas_caro = precio_producto
            cantidad_barbijo_caro = cantidad
            fabricante_barbijo_caro = fabricante
    elif tipo_producto == "jabon":
        unidades_jabon_total += cantidad
    
    if cantidad > item_mas_unidades :
        item_mas_unidades = cantidad
        fabricante_mas_unidades = fabricante

print("La cantidad de unidades del más caro de los barbijos es ", cantidad_barbijo_caro, "y su fabricante es ", fabricante_barbijo_caro,".")
print("El fabricante del item con más unidades es : ", fabricante_mas_unidades,".")
print("La cantidad total de jabones es de ", unidades_jabon_total,".")

#La división de higiene está trabajando en un control de stock para productos sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
#El tipo (validar "barbijo", "jabón" o "alcohol")
#El precio: (validar entre 100 y 300)
#La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
#La marca y el Fabricante.
# 
# Se debe informar lo siguiente:
#Del más caro de los barbijos, la cantidad de unidades y el fabricante.
#Del ítem con más unidades, el fabricante.
#Cuántas unidades de jabones hay en total.