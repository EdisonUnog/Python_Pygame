from data_stark import lista_personajes
from os import system

#crear un menu
'''def menu_integrador_dos()->int: ## views -> vistas
    print("\n 1._")
    print(" 2._")
    print(" 3._")
    print(" 4._")
    print(" 5._")
    print(" 6._")
    print(" 7._")
    print(" 8._salir")

    opcion = int(input("\n >>ELIGE UNA OPCION: "))
    while opcion <1 or opcion > 16:
        print(" Error..")
        opcion = int(input("\n >>ELIGE UNA OPCION: "))
    return opcion'''
#####################################################################################
'''
0. Crear la función 'stark_normalizar_datos' la cual recibirá por parámetro la lista
  de héroes. La función deberá:
● Recorrer la lista y convertir al tipo de dato correcto las keys (solo con
 las keys que representan datos numéricos)
● Validar primero que el tipo de dato no sea del tipo al cual será
  casteado. Por ejemplo si una key debería ser entero (ejemplo edad)
verificar antes que no se encuentre ya en ese tipo de dato.
● Si al menos un dato fue modificado, la función deberá imprimir como
  mensaje ‘Datos normalizados’, caso contrario no imprimirá nada.
● Validar que la lista de héroes no esté vacía para realizar sus acciones,
  caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”
'''

def stark_normalizar_datos(lista:list[dict])->list:
    
    if type(lista) == list and len(lista) > 0:
        flag = False
        for x in lista:
            if x['altura'] != float():
                x['altura'] = float(x['altura'])
                flag = True

            if x['peso'] != float():
                x['peso'] = float(x['peso'])
                flag = True

            if x['fuerza'] != float():
                x['fuerza'] = float(x['fuerza'])
                flag = True

    else:
        print("\n *La lista esta vacia....")
    
    if flag == True:
        print("\n *Datos normalizados")

    lista_casteada = lista

    return lista_casteada

def datos_normalizados_lista(lista:list[dict]):
    if type(lista) == list and len(lista) > 0:
        datos_numericos = stark_normalizar_datos(lista)
        print(datos_numericos)
#####################################################################################
'''
1.1.Crear la función 'obtener_nombre' la cual recibirá por parámetro un
    diccionario el cual representara a un héroe y devolverá un string el cual
    contenga su nombre formateado de la siguiente manera:
    ** Nombre: Howard the Duck
'''

def obtener_nombre(diccionario:dict)->str:

    if diccionario == {}:
        return "Error, el diccionario esta vacio"
    mensaje = " **Nombre: {0}".format(diccionario["nombre"])

    return mensaje


def obtener_nombre_lista(lista:list[dict]):
    if (type(lista) == list and len(lista) > 0):
        nombre = obtener_nombre(lista[0])
        imprimir_dato(nombre)

#####################################################################################
'''
1.2. Crear la función 'imprimir_dato' la cual recibirá por parámetro un string y
deberá imprimirlo en la consola. La función no tendrá retorno.
'''
def imprimir_dato(dato:str):
    print(f"\n{dato}")


#####################################################################################
'''
1.3. Crear la función 'stark_imprimir_nombres_heroes' la cual recibirá por
parámetro la lista de héroes y deberá imprimirla en la consola. Reutilizar las
funciones hechas en los puntos 1.1 y 1.2. Validar que la lista no esté vacía
'''
def stark_imprimir_nombres_heroes(lista:list[dict]):
    if (type(lista) == list and len(lista) > 0):
        for x in lista:
            imprimir_dato(x)

#####################################################################################
'''
2. Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un
diccionario el cual representara a un héroe y una key (string) la cual
representará el dato que se desea obtener.

● La función deberá devolver un string el cual contenga el nombre y dato
(key) del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O
CUALQUIER OTRO DATO.

● El string resultante debe estar formateado de la siguiente manera:
(suponiendo que la key es fuerza)
Nombre: Venom | fuerza: 500
'''
#obtengo nombre y dato
'''def obtener_nombre_y_dato(heroe:dict, clave:str)->str:
    nombre_dato = " **Nombre: {0} | {1}: {2}".format(heroe['nombre'],clave , heroe[clave])
    return nombre_dato'''

def obtener_nombre_y_dato(heroe:dict, clave:str)->str:
        
    nombre_dato = " **Nombre: {0} | {1}: {2}".format(heroe['nombre'], clave , heroe[clave])

    return nombre_dato


def nombres_datos(lista:list[dict]):
    if type(lista) == list and len(lista) > 0:
        datos = obtener_nombre_y_dato(lista_personajes[0],"altura")
        imprimir_dato(datos)


#####################################################################################
'''
3. Crear la función 'stark_imprimir_nombres_alturas' la cual recibirá por
parámetro la lista de héroes, la cual deberá iterar e imprimir sus nombres y
alturas USANDO la función creada en el punto 2. Validar que la lista de héroes
no esté vacía para realizar sus acciones, caso contrario no hará nada y
retornara -1.
Con este se resuelve el Ej 2 del desafío #00
'''

def stark_imprimir_nombres_alturas(lista:list[dict]):
    if type(lista) == list and len(lista) > 0:
        for x in lista:
            imprimir_dato(obtener_nombre_y_dato(x,"altura"))
    else:
        print("/no")


#####################################################################################
'''
4.1. Crear la función 'calcular_max' la cual recibirá por parámetro la lista de
héroes y una key (string) la cual representará el dato que deberá ser evaluado
a efectos de determinar cuál es el máximo de la lista. Por ejemplo la función
deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe
que tenga el dato más alto.
Ejemplo de llamada:
calcular_max(lista, 'edad')
'''

def calcular_max(lista:list[dict], clave:str)->dict:

    flag = True
    if type(lista) == list and len(lista) > 0:

        lista[0][clave] = float(lista[0][clave])
        diccionario_heroe_clave = {"nombre":lista[0]['nombre'], clave:lista[0][clave]}

        for x in lista:

            x[clave] = float(x[clave])

            if flag == True or x[clave] > diccionario_heroe_clave[clave]:
                diccionario_heroe_clave = {"nombre":x['nombre'],clave:x[clave]}
                flag = False

    return diccionario_heroe_clave


def stark_maximo_valor(lista:list[dict]):
    if type(lista) == list and len(lista) > 0:
        diccionario = calcular_max(lista,'altura')
        imprimir_dato(diccionario)


'''
4.2. Crear la función 'calcular_min' la cual recibirá por parámetro la lista de
héroes y una key (string) la cual representará el dato que deberá ser evaluado
a efectos de determinar cuál es el mínimo de la lista. Por ejemplo la función
deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe
que tenga el dato más bajo.
Ejemplo de llamada:
calcular_min(lista, 'edad')
'''
def calcular_min(lista:list[dict], clave:str)->dict:

    flag = True
    if type(lista) == list and len(lista) > 0:

        lista[0][clave] = float(lista[0][clave])
        diccionario_heroe_clave = {"nombre":lista[0]['nombre'], clave:lista[0][clave]}

        for x in lista:

            x[clave] = float(x[clave])

            if flag == True or x[clave] < diccionario_heroe_clave[clave]:
                diccionario_heroe_clave = {"nombre":x['nombre'],clave:x[clave]}
                flag = False

    return diccionario_heroe_clave


def stark_minimo_valor(lista:list[dict]):
    if type(lista) == list and len(lista) > 0:
        diccionario = calcular_min(lista,'altura')
        imprimir_dato(diccionario)

#####################################################################################
'''
4.3 Crear la funcion 'calcular_max_min_dato' la cual recibira tres parámetros:
La lista de héroes
El tipo de cálculo a realizar: es un valor string que puede tomar los valores ‘maximo’ o ‘minimo’
Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘edad’, etc.
La función deberá retornar el héroe que cumpla con la condición pedida. Reutilizar las funciones hechas en los puntos 4.1 y 4.2
Ejemplo de llamada:
calcular_max_min_dato(lista, "maximo", "edad")
'''

def calcular_max_min_dato(lista:list[dict], calcular, clave:str)->dict:
    
    if type(lista) == list and len(lista) > 0:

        if calcular == 1: #maximo
            calcular_valores = calcular_max(lista, clave)

        elif calcular == 2: #minimo
            calcular_valores = calcular_min(lista, clave)

    return calcular_valores


def stark_max_min_dato(lista:list[dict]):

    valor = int(input("\n calcular._ 1: maximo / 2: minimo >> "))
    while valor != 1 and valor != 2:
        print("\n ERROR....")
        valor = int(input("\n calcular._ 1: maximo / 2: minimo >> "))

    obtengo_calculo = calcular_max_min_dato(lista, valor, 'altura')
    imprimir_dato(obtengo_calculo)

#####################################################################################
'''
4.4. Crear la función 'stark_calcular_imprimir_heroe' la cual recibirá tres
parámetros:
● La lista de héroes
● El tipo de cálculo a realizar: es un valor string que puede tomar los
valores ‘maximo’ o ‘minimo’
● Un string que representa la key del dato a calcular, por ejemplo: ‘altura’,
‘peso’, ‘edad’, etc.
Con este se resuelve el Ej 3, Ej 4, Ej 6 y Ej 7 del desafío #00
La función deberá obtener el héroe que cumpla dichas condiciones, imprimir
su nombre y el valor calculado. Reutilizar las funciones de los puntos:
punto 1.2, punto: 2 y punto 4.3
Validar que la lista de héroes no esté vacía para realizar sus acciones, caso
contrario no hará nada y retornara -1.
Ejemplo de llamada:
stark_calcular_imprimir_heroe (lista, "maximo", "edad")
Ejemplo de salida:
Mayor altura: Nombre: Howard the Duck | altura: 79.34
'''
def stark_calcular_imprimir_heroe(lista:list[dict], max_min, clave:str)->dict:
    
    if type(lista) == list and len(lista) > 0:

        if max_min == 1: #maximo
            mensaje = " {2} Mayor ___ Nombre: {0} - {2}: {1}".format(calcular_max_min_dato(lista, max_min, clave)['nombre'],
            calcular_max_min_dato(lista, max_min, clave)[clave],clave.capitalize())

        elif max_min == 2: #minimo
            mensaje = " {2} Menor ___ Nombre: {0} - {2}: {1}".format(calcular_max_min_dato(lista, max_min, clave)['nombre'],
            calcular_max_min_dato(lista, max_min, clave)[clave],clave.capitalize())

    return mensaje


def stark_max_min_de_lista(lista:list[dict]):

    valor = int(input("\n calcular._ 1: maximo / 2: minimo >> "))
    while valor != 1 and valor != 2:
        print("\n ERROR....")
        valor = int(input("\n calcular._ 1: maximo / 2: minimo >> "))

    obtengo_calculo = stark_calcular_imprimir_heroe(lista, valor, 'altura')
    imprimir_dato(obtengo_calculo)


#####################################################################################
'''
5.1. Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una
lista de héroes y un string que representara el dato/key de los héroes que se
requiere sumar. Validar que cada héroe sea tipo diccionario y que no sea un

correspondientes
diccionario vacío antes de hacer la suma. La función deberá retorna la suma
de todos los datos según la key pasada por parámetro
'''
def sumar_dato_heroe(lista:list[dict], clave:str)->float:

    if type(lista) == list and len(lista) > 0:
        suma_acumulada = float(lista[0][clave])
        for x in lista:
            if(type(x) == type({}) and len(x) > 0):
                suma_acumulada += float(x[clave])

    #mensaje = "Suma acumulada {0} de._ {1} ".format(suma_acumulada, clave.capitalize())
    mensaje = suma_acumulada

    return mensaje


def stark_suma_acum(lista:list[dict]):
    if type(lista) == list and len(lista) > 0:

        suma = sumar_dato_heroe(lista, 'peso')
        imprimir_dato(suma) 


#####################################################################################
'''
5.2. Crear la función ‘dividir’ la cual recibirá como parámetro dos números
(dividendo y divisor). Se debe verificar si el divisor es 0, en caso de serlo,
retornar 0, caso contrario realizar la división entre los parámetros y retornar el
resultado
'''

def dividir(dividendo:float, divisor:float)->float:

    if divisor != 0:
        result = dividendo / divisor
    else:
        result = 0

    return result


#####################################################################################
'''
5.3. Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una
lista de héroes y un string que representa el dato del héroe que se requiere
calcular el promedio. La función debe retornar el promedio del dato pasado
por parámetro
'''

def calcular_promedio(lista:list, clave:str)->str:

    contador = 0
    if type(lista) == list and len(lista) > 0:
        for x in lista:
            contador += 1

    promedio = dividir(sumar_dato_heroe(lista, clave), contador)
    mensaje = " *Promedio de {0} es: {1}".format(clave.capitalize(),promedio)

    return mensaje

#####################################################################################
'''
5.4. Crear la función 'stark_calcular_imprimir_promedio_altura' la cual recibirá
una lista de héroes y utilizando la función del punto 5.3 calcula y mostrará la
altura promedio. Validar que la lista de héroes no esté vacía para realizar sus
acciones, caso contrario no hará nada y retornara -1.
IMPORTANTE: hacer uso de las las funciones creadas en los puntos 1.2, 5.1 y
5.3
'''

def stark_calcular_imprimir_promedio_altura(lista:list[dict]):
    if type(lista) == list and len(lista) > 0:

        operacion = calcular_promedio(lista,'altura')
        imprimir_dato(operacion)

#####################################################################################
'''
6.1. Crear la función "imprimir_menu" que imprima el menú de opciones por
pantalla, el cual permite utilizar toda la funcionalidad ya programada. Se
deberá reutilizar la función antes creada encargada de imprimir un string (1.2)
'''
def menu_integrador_dos():
    mensaje = "\n 1._Normalizar datos"
    mensaje += "\n 2._Obtener nombre"
    mensaje += "\n 3._Imprimir nombre heroes"
    mensaje += "\n 4._Nombres dato"
    mensaje += "\n 5._Imprimir nombre altura"
    mensaje += "\n 6._Maximo y minimo valor"
    mensaje += "\n 7._Stark_Max_min_dato"
    mensaje += "\n 8._Stark_Max_Min_Lista"
    mensaje += "\n 9._Suma acumulada"
    mensaje += "\n 10._Promediomensaje"
    mensaje += "\n 11._ Salir..."
    return mensaje

#####################################################################################
'''
6.2. Crear la función “validar_entero” la cual recibirá por parámetro un string de
número el cual deberá verificar que sea sea un string conformado únicamente
por dígitos. Retornara True en caso de serlo, False caso contrario
'''
def validar_entero(numero:str)->bool:
    
    flag = False
    if numero.isdigit:
        flag = True

    return flag

#####################################################################################
'''
6.3. Crear la función 'stark_menu_principal' la cual se encargará de imprimir el
menú de opciones y le pedirá al usuario que ingrese el número de una de las
opciones elegidas y deberá validarlo. En caso de ser correcto dicho número,
lo retornara casteado a entero, caso contrario retorna -1. Reutilizar las
funciones del ejercicio 6.1 y 6.2
'''
def stark_menu_principal():
    opcion = input(f"{menu_integrador_dos()} \n\n Ingresa una opcion >> ")
    while validar_entero(opcion) == False:
        print("Error")
        opcion = input(f"{menu_integrador_dos()} \n\n Ingresa una opcion >> ")

    return opcion

#####################################################################################
'''
7. Crear la función 'stark_marvel_app' la cual recibirá por parámetro la lista de
héroes y se encargará de la ejecución principal de nuestro programa.
Utilizar if/elif o match según prefiera (match solo para los que cuentan con
python 3.10+). Debe informar por consola en caso de seleccionar una opción
'''

def stark_marvel_app(lista:list):

    if type(lista) == list and len(lista) > 0:
        seguir = True
        while True:

            opcion = stark_menu_principal()

            match opcion:
                case "1":
                    datos_normalizados_lista(lista)       
                case "2":
                    obtener_nombre_lista(lista)        
                case "3":
                    stark_imprimir_nombres_heroes(lista)        
                case "4":
                    nombres_datos(lista)        
                case "5":
                    stark_imprimir_nombres_alturas(lista)
                case "6":
                    stark_maximo_valor(lista)
                    stark_minimo_valor(lista)
                case "7":
                    stark_max_min_dato(lista)
                case "8":
                    stark_max_min_de_lista(lista)       
                case "9":
                    stark_suma_acum(lista)       
                case "10":
                    stark_calcular_imprimir_promedio_altura(lista)        
                
                case "11":
                    seguir = input("\n deseas salir si/no: ")
                    if seguir != "no":
                        print("\n **GRACIAS**\n")
                        break