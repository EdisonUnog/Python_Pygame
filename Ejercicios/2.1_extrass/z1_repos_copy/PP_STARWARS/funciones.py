import json
import re

def cargar_json(ruta:str)->list[dict]:
    '''
    Extrae la información de un .json y lo devuelve como lista de diccionarios.
    '''
    data = []
    with open(ruta,"r") as archivo:
        data = json.load(archivo)
        data = list[dict](data["results"])
        return data


def funct_imprimir_datos(lista:list,key:str):
    '''
    Imprime el nombre y un dato de una lista, según la key indicada.
    '''
    for contenido in lista:
        print("Nombre: {0}. {1} : {2}.".format(contenido["name"],key.capitalize(),contenido[key]))


def funct_normalizar_datos(lista:list,key:str)->list:
    '''
    Convierte strings de una lista a entero.
    '''
    for elemento in lista:
        if not type[elemento[key]] == type[int]:
            elemento[key] = int(elemento[key])
    return lista


def funct_imprimir_mas_alto_por_genero(lista:list):
    '''
    Organiza listas por generos y luego busca el mayor en cada una. 
    Imprime el nombre de cada uno de estos.
    '''
    funct_normalizar_datos(lista,"height")
    
    male_lista = []
    female_lista = []
    n_a_lista = []
    for elemento in lista:
        if elemento["gender"] == "male":
            male_lista.append(elemento)
        elif elemento["gender"] == "female":
            female_lista.append(elemento)
        else:
            n_a_lista.append(elemento)
    mas_alto_male = male_lista[funct_buscar_minimo_y_maximo(male_lista,"height","max")]
    mas_alto_female = female_lista[funct_buscar_minimo_y_maximo(female_lista,"height","max")]
    mas_alto_n_a = n_a_lista[funct_buscar_minimo_y_maximo(male_lista,"height","max")]
    print("El personaje de género másculino más alto es : {0}, más alto femenino : {1} y el más alto n/a : {2}-\n"
                                                .format(mas_alto_male["name"],mas_alto_female["name"],mas_alto_n_a["name"]))


def funct_buscar_minimo_y_maximo(lista:list,key:str,max_o_min:str)->int:
    '''
    Recorre una lista pasada por el usuario y compara según la key indicada.
    Devuelve un entero correspondiente a la posicion en la lista siendo este el mayor o menor.
    '''
    max_o_min_final = 0
    for i in range(len(lista)):
        if(lista[i][key] < lista[max_o_min_final][key]) and max_o_min == "min":
            max_o_min_final = i
        elif(lista[i][key] > lista[max_o_min_final][key]) and max_o_min == "max": 
            max_o_min_final = i
    return max_o_min_final


def funct_ordenar_y_listar(lista:list,key)->list:
    '''
    A partir de la funcion de buscar mínimo, crea una nueva lista ordenada de menor a mayor.
    Devuelve una lista.
    '''
    lista_llena = lista.copy()
    lista_ordenada = []
    while len(lista_llena) > 0:
       minimo = funct_buscar_minimo_y_maximo(lista_llena,key,"min")
       element_min = lista_llena.pop(minimo)
       lista_ordenada.append(element_min)
    return lista_ordenada


def funct_buscar_personaje(lista:list,personaje:str)->dict:
    '''
    Recorre una lista y compara el string ingresado con los nombres de la lista, si lo encuentra lo imprime.
    '''
    for elemento in lista:
        if re.match(personaje,elemento["name"],re.IGNORECASE):
            print("Nombre : {0} | Altura : {1} | Peso : {2} | Género : {3} ".format(elemento["name"],elemento["height"],
                                                                            elemento["mass"],elemento["gender"]))
        else:
            print("El personaje no se encuentra en esta lista.")


def guardar_archivo(output:str,contenido:list)->bool:
    '''
    Recibe una lista, la recorre creando strings y finalmente la guarda en un csv.
    Si no es posible muestra una alerta. Devuelve un booleano.
    '''
    if len(contenido) > 0 :
        with open(output,"w") as file:
            for elemento in contenido:
                file.write("Nombre : {0} | Altura : {1} | Peso : {2} | Genero : {3}.\n".format(elemento["name"],
                                                                                            elemento["height"],
                                                                                            elemento["mass"],
                                                                                            elemento["gender"]))
            print("Se creó el archivo {0}.csv".format(output))
            return True
    else :
        print("No se ejecutó la función.")
        return False