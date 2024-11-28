import re
lista_precios = {
    
    "banana" : {
        "precio" : 120.10,
        "unidad_medida": "kg",
        "stock": 50
    },
    
    "pera": {
        "precio": 240.50,
        "unidad_medida": "kg",
        "stock": 40        
    },
    
    "frutilla": {
        "precio": 300,
        "unidad_medida": "kg",
        "stock": 100        
    }, 
    
    "mango" : {
        "precio": 300,
        "unidad_medida": "unidad",
        "stock": 100  
    }

}

# Punto 1: solicitar al usuario un producto y verificiar si existe en 'lista_precios' en caso de existir mostrar precio y el stock. En caso de no existir el 
# producto mostrar el mensaje 'el articulo no se encuentra en la lista'

# Punto 2: agregar al punto anterior que el usuario ingrese la cantidad y retornar el precio total (precio * cantidad)

# Punto 3: solicitar al usuario que ingrese una nueva fruta junto con su precio, unidad de medida y stock. Agregar la nueva fruta a la lista de precios.

# Punto 4: imprimir el listado de frutas (solo su nombre)

# Punto 5: solicitarle al usuario el nombre de fruta y en caso de exisitir eliminarla. En caso de que el producto no exista mostrar 
# el mensaje 'el articulo no se encuentra en la lista'

def funct_punto_uno_y_dos(lista:list):
    product_in = input("Ingrese un producto : ")
    if product_in in lista.keys():
        print("Precio : $ {0}. Stock : {1} {2}.".format(lista_precios[product_in]["precio"],lista_precios[product_in]["stock"],lista_precios[product_in]["unidad_medida"]))
        if "precio" in lista_precios[product_in].keys():
            cant = ""
            while not re.match("^[0-9]{1,2}$",cant):
                cant = input("Ingrese la cantidad : ")
            cant = int(cant)
            precio = lista_precios[product_in]["precio"]
            precio_total = precio * cant
            print("El precio total es : {0}".format(precio_total))
    else: 
        print("El artículo no se encuentra en la lista.")

def funct_ingresar_fruta()->dict:
    nueva_fruta = {}
    nombre = ""
    precio = ""
    unid_de_medida = ""
    stock = ""
    nueva_fruta = ""
    while not re.match("^[a-zA-Z]$",nombre):
        nombre = input("Ingrese el nombre de la fruta : ")
    while not re.match("^[0-9.]$",precio):
        precio = input("Ingrese el precio de la fruta : ")
    while not re.match("^(kg|unidad)$",unid_de_medida):
        unid_de_medida = input("Ingrese una unidad de medida : (kg|unidad) ")
    while not re.match("^[0-9]$",stock):
        stock = input("Ingrese la cantidad de stock : ")
    nueva_fruta = {nombre:{"precio":float(precio),"unidad_medida":unid_de_medida,"stock":int(stock)}}
    return nueva_fruta

def funct_agregar_fruta(lista:list):
    nueva_entrada = funct_ingresar_fruta()
    lista.update(nueva_entrada)
    print(lista)

def funct_imprimir_nombres(lista:list):
    for x in lista:
        print("{0}".format(x.capitalize()))

def funct_eliminar_de_lista(lista:list):
    a_borrar = input("Ingrese una fruta a eliminar : ")
    

#funct_punto_uno_y_dos(lista_precios)
#funct_imprimir_nombres(lista_precios)