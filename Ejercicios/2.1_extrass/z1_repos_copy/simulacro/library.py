import json
import re

def leer_archivo(ruta:str)->list[dict]:
    '''
    Extrae la información de un .json y lo devuelve como lista de diccionarios.
    '''
    data = []
    with open(ruta,"r") as archivo:
        data = json.load(archivo)
        data = list[dict](data["heroes"])
        return data

def funct_listar_heroes(lista:list,cantidad:int)->list:

    lista_salida = []
    if len(lista)>0 and cantidad <= len(lista):
        lista_salida = lista[:cantidad]
        return lista_salida
    else:
        print("El número ingresado no coincide con la lista.")
        return -1 

def funct_imprimir_heroes(lista:list,key:str):

    for elemento in lista:
        print("Nombre : {0}. {1} : {2}.".format(elemento["nombre"],key.capitalize(),elemento[key]))


def funct_validar_string(patron:str,data:str)->bool:
    '''
    Valida que el string ingresado contenga un número que cumpla con el patrón asignado.
    Si se cumple retorna True, sino False.
    '''
    if re.match(patron,data):
        return True
    else:
        return False
    
def funct_buscar_minimo(lista:list,key:str)->int:

    minimo = 0
    for i in range(len(lista)):
        if(lista[i][key] < lista[minimo][key]):
            minimo = i
    return minimo

def funct_ordenar_y_listar(lista:list,key)->list:
    lista_llena = lista.copy()
    lista_ordenada = []
    while len(lista_llena) > 0:
       minimo = funct_buscar_minimo(lista_llena,key)
       element_min = lista_llena.pop(minimo)
       lista_ordenada.append(element_min)
    return lista_ordenada

def funct_sacar_promedio(lista:list,key:str)->float:
    '''
    Itera una lista y obtiene el promedio según el key indicado. Imprime el promedio y devuelve un flotante.
    '''
    acumulador = 0
    for element in lista:
        acumulador += element[key]
    result = acumulador/len(lista)
    print("El promedio de {0} es : {1:.2F} .".format(key,result))

    return result

def funct_listar_segun_numero(lista:list,promedio:float,key:str,menor_o_mayor:str)->list:
    '''
    Toma un número y crea una lista con los elementos que superen, o no, a este.
    Devuelve una lista 
    '''
    lista_segun_numero = [ ]
    for elemento in lista:
        if elemento[key]>promedio and menor_o_mayor == "mayor":
            lista_segun_numero.append(elemento)
        elif elemento[key]<promedio and menor_o_mayor == "menor":
            lista_segun_numero.append(elemento)
    return lista_segun_numero


def funct_buscar_por_inteligencia(lista:list,tipo_de_inteligencia:str)->list:
    '''
    Recorre una lista y crea una lista nueva 
    con los elementos que coincidan con el tipo de inteligencia(luego de validarlo).
    Devuelve la lista creada, si da error devuelve -1.
    '''
    lista_segun_inteligencia = []
    
    if len(lista)>0:
        for elemento in lista:
            if elemento["inteligencia"] == tipo_de_inteligencia:
                lista_segun_inteligencia.append[elemento]
        return lista_segun_inteligencia
    else:
        print("La lista está vacía.")
        return -1

def guardar_archivo(output:str,contenido:list,key:str):

    if len(contenido) > 0 :
        with open(output,"w") as file:
            for elemento in contenido:
                file.write("Nombre : {0}. {1} : {2}.\n".format(elemento["nombre"],key.capitalize(), elemento[key]))
            print("Se creó el archivo {0}.csv".format(output))
            return True
    else :
        print("No se ejecutó la función.")
        return False

ruta = "C:/Users/bilix/OneDrive/Escritorio/backup/ArchivosUTN/primercuatri/simulacro/data_stark_modif.json"
output = "C:/Users/bilix/OneDrive/Escritorio/backup/ArchivosUTN/primercuatri/simulacro/"
