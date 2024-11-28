from data_stark import lista_personajes 

def funct_stark_normalizar_datos(lista_personajes:dict)->dict:
    '''
    Convierte los datos al tipo necesario para cada función (strings a flotantes y enteros).
    '''
    if len(lista_personajes) > 0:
        flag = False
        for datos in lista_personajes:
            if not (datos["altura"] == type(float)) :
                datos["altura"] = float(datos["altura"])
                flag = True

            if not (datos["peso"] == type(float)) :
                datos["peso"] = float(datos["peso"])
                flag = True

            if not (datos["fuerza"] == type(int)) :
                datos["fuerza"] = int(datos["fuerza"])
                flag = True

        if flag == True:
            print("Datos normalizados.")
        return lista_personajes
    else :
        print("No tiene datos dentro.")

def funct_obtener_nombre(dict_nombres:dict)->str:
    '''
    Obtiene nombres de un diccionario y los devuelve en string.
    '''
    nombre = "Nombre : {0}.".format(dict_nombres["nombre"])
    return nombre

def funct_imprimir_dato(mensaje:str):
    '''
    Imprime un string con lo que se le ingrese.
    '''
    
    print(mensaje)

def funct_stark_imprimir_nombres(lista:dict):
    '''
    Recorre un diccionario e imprime los nombres (si no es posible, devuelve -1).
    '''

    if len(lista) > 0 :
        for nombre in lista:
            funct_imprimir_dato(funct_obtener_nombre(nombre))
    else :
        return -1

def funct_obtener_nombre_y_dato(lista:dict,dato:str)->str:
    '''
    Obtiene el nombre y un dato indicado de un diccionario y lo devuelve formateado en un string.
    '''
    nombre_y_dato = "{0} | {1} : {2}".format(funct_obtener_nombre(lista),dato,lista[dato])
    return nombre_y_dato

def funct_imprimir_nombres_alturas(lista:dict):
    '''
    Obtiene los nombres y la altura de un diccionario e imprime estos datos (si no es posible, devuelve -1).
    '''
    if len(lista)>0:
        for personaje in lista:
            funct_imprimir_dato(funct_obtener_nombre_y_dato(personaje,"altura"))
    else :
        return -1

def funct_calcular_max(lista:dict,dato_a_calcular:str)->str:
    '''
    Calcula el máximo de un dato en un diccionario y devuelve el diccionario que lo contenga.
    '''
    maximo_de_dato = lista[0]
    for dato in lista:
        if maximo_de_dato[dato_a_calcular] < dato[dato_a_calcular]:
            maximo_de_dato = dato
    return maximo_de_dato
def funct_calcular_min(lista:dict,dato_a_calcular:str)->str:
    '''
    Calcula el minimo de un dato en un diccionario y devuelve el diccionario que lo contenga.
    '''
    minimo_de_dato = lista[0]
    for dato in lista:
        dato_a_calcular = dato_a_calcular.lower()
        if minimo_de_dato[dato_a_calcular] > dato[dato_a_calcular]:
            minimo_de_dato = dato
    return minimo_de_dato

def funct_calcular_max_min_dato(lista:dict,minomax:str,dato_a_calcular:str)->str:
    '''
    Convierte los datos al tipo necesario para cada luego calcular el maximo o minimo de un dato asignado,
    devuelve el diccionario que lo contenga.
    '''
    funct_stark_normalizar_datos(lista)
    minomax = minomax.lower()
    if minomax == "maximo":
       maxmin_heroe = funct_calcular_max(lista,dato_a_calcular)
    elif minomax == "minimo":
       maxmin_heroe = funct_calcular_min(lista,dato_a_calcular)
    return maxmin_heroe

def funct_stark_calcular_imprimir_heroe(lista:list,tipo_de_calculo:str,dato_a_calcular:str):
    '''
    Imprime el nombre y dato calculado (mayor o menor de un dato) de una lista (si la lista esta vacía, devuelve -1).
    '''

    if len(lista) > 0:
        funct_imprimir_dato("{0} {1} :\n{2}".format(tipo_de_calculo.capitalize(),
                                                    dato_a_calcular,funct_obtener_nombre_y_dato((funct_calcular_max_min_dato
                                                                                                    (lista,tipo_de_calculo,dato_a_calcular))
                                                                                                    ,dato_a_calcular)))
    else :
        return -1
        
def funct_sumar_dato_heroe(lista:list,dato_a_calcular:str)->float:
    '''
    Convierte los datos necesarios de una lista a numericos, recorre esta lista para acumular
    y devolver estos datos de un tipo asignado.
    '''
    funct_stark_normalizar_datos(lista)
    acumulador_dato = 0
    for heroe in lista:
        if len(heroe) > 0 and type(heroe) == dict:
            acumulador_dato += heroe[dato_a_calcular]
    acumulador_dato = round(acumulador_dato,2)
    return acumulador_dato

def funct_dividir(dividendo:float,divisor:float)->float:
    '''
    Ejecuta una división y devuelve el resultado.
    '''
    if not divisor == 0:
        resultado_division = dividendo / divisor
        return resultado_division
    else:
        return 0 

def funct_calcular_promedio(lista:list,dato_a_calcular:str)->float:
    '''
    Calcula y devuelve el promedio a través de la longitud de un a lista y la sumatoria de un dato acumulado.
    '''
    promedio = funct_dividir(funct_sumar_dato_heroe(lista,dato_a_calcular),len(lista))
    promedio = round(promedio,2)
    return promedio

def funct_stark_calcular_imprimir_promedio_altura(lista:list):
    '''
    Calcula e imprime el promedio de altura de una lista (si no es posible devuelve -1).
    '''
    if len(lista) > 0 :
        funct_imprimir_dato("El promedio de altura es {0}".format(funct_calcular_promedio(lista,"altura")))
    else :
        return -1

def funct_imprimir_menu():
    '''
    Imprime un string con el menú de opciones.
    '''
    funct_imprimir_dato("\n{0}\n \n(1) Nombres.\n(2) Nombres y altura.\n"
                           "(3) Heroe más alto.\n(4) Heroe más bajo.\n(5) Promedio altura.\n"
                           "(6) Heroe más y menos pesado.\n(7) Salir.\n".format("MENÚ".center(50,"-")))

def funct_validar_entero(numero:str)->bool:
    '''
    Valida que el string ingresado sea solamente númerico y devuelve un booleano.
    '''
    if numero.isnumeric():
        return True
    else :
        return False

def funct_stark_menu_principal():
    '''
    Imprime el menú, reclama un número que pueda ser validado y convertido a entero (si no es posible devuelve -1).
    '''
    funct_imprimir_menu()
    numero_ingresado = input("Ingrese un número para ejecutar una acción:\n")
    if funct_validar_entero(numero_ingresado):
        numero_ingresado = int(numero_ingresado)
        return numero_ingresado
    else :
        return -1

def funct_stark_marvel_app(lista:list):
    '''
    Muestra el menú y pide una respuesta que ejecutará una acción según el número ingresado.
    '''
    while True:
        respuesta = funct_stark_menu_principal()

        if respuesta == 1:
            funct_stark_imprimir_nombres(lista)
        elif respuesta == 2:
            funct_imprimir_nombres_alturas(lista)
        elif respuesta == 3:
            funct_stark_calcular_imprimir_heroe(lista,"maximo","altura")
        elif respuesta == 4:
            funct_stark_calcular_imprimir_heroe(lista,"minimo","altura")
        elif respuesta == 5:
            funct_stark_calcular_imprimir_promedio_altura(lista)
        elif respuesta == 6:
            funct_stark_calcular_imprimir_heroe(lista,"maximo","peso")
            funct_stark_calcular_imprimir_heroe(lista,"minimo","peso")
        elif respuesta == 7:
            funct_imprimir_dato("Programa terminado.")
            break
        else :
            funct_imprimir_dato("\nLo ingresado no es válido.")
        


#funct_stark_marvel_app(lista_personajes)