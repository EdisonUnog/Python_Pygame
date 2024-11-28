import re
import json

'''
			"id": 9,
			"nombre": "blastoise",
			"tipo": ["agua"],
            "evoluciones": [],
			"poder": 18,
			"fortaleza":["fuego", "piedra"],
			"debilidad":["planta", "electrico"]
'''

def leer_archivo(ruta:str)->list[dict]:
    '''
    Extrae la información de un .json y lo devuelve como lista de diccionarios.
    '''
    data = []
    with open(ruta,"r") as archivo:
        data = json.load(archivo)
        data = list[dict](data["pokemones"])
        return data

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

def funct_sacar_promedio(lista:list,key:str)->float:
    '''
    Itera una lista y obtiene el promedio según el key indicado. Imprime el promedio y devuelve un flotante.
    '''
    acumulador = 0
    for element in lista:
        if key == "poder":
            acumulador += element[key]
        else:
            acumulador += len(element[key])
    result = acumulador/len(lista)
    print("El promedio de {0} es : {1:.2F} .".format(key,result))

    return result


def funct_listar_pokes(lista:list,cantidad:int)->list:

    lista_salida = []
    if len(lista)>0 and cantidad <= len(lista):
        lista_salida = lista[-cantidad:]
        return lista_salida
    else:
        print("El número ingresado no coincide con la lista.")
        return -1 


def funct_imprimir_pokes(lista:list,key:str):
    '''
    Imprime el nombre y la key indicada.
    '''
    for elemento in lista:
        if re.match("^(poder|id)$",key) :
            key_format = elemento[key]
        else: 
            key_format = " | ".join(elemento[key])
        print("Nombre : {0}. {1} : {2}.".format(elemento["nombre"],key.capitalize(),key_format))

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

def funct_listar_segun_numero(lista:list,promedio:float,key:str,menor_o_mayor:str)->list:
    '''
    Toma un número y crea una lista con los elementos que superen, o no, a este.
    Devuelve una lista 
    '''
    lista_segun_numero = [ ]
    
    if key == "poder":
        for elemento in lista:
            if elemento[key]>promedio and menor_o_mayor == "mayor":
                lista_segun_numero.append(elemento)
            elif elemento[key]<promedio and menor_o_mayor == "menor":
                lista_segun_numero.append(elemento)
    else:
        for elemento in lista:
            if len(elemento[key])>promedio and menor_o_mayor == "mayor":
                lista_segun_numero.append(elemento)
            elif len(elemento[key])<promedio and menor_o_mayor == "menor":
                lista_segun_numero.append(elemento)
    return lista_segun_numero


def funct_buscar_pokemon_por_tipo(lista:list,tipo_a_buscar:str):
    pokemon_con_un_tipo = []
    pokemon_con_dos_tipos = []
    tipo_a_buscar = tipo_a_buscar.lower()
    for pokemon in lista:
        for tipo in pokemon["tipo"]:
            if re.match(tipo_a_buscar,tipo):
                if len(pokemon["tipo"]) == 1:
                    pokemon_con_un_tipo.append(pokemon["nombre"])
                else:
                    pokemon_con_dos_tipos.append(pokemon["nombre"])
    print("\n")
    if (len(pokemon_con_un_tipo)) > 0:
        pokemon_listados_un_tipo = ", ".join(pokemon_con_un_tipo)
        print("Los pokemon de tipo {0} son : {1}.".format(tipo_a_buscar,pokemon_listados_un_tipo))
    if  (len(pokemon_con_dos_tipos)) > 0:
        pokemon_listados_dos_tipos = ", ".join(pokemon_con_dos_tipos)
        print("Los pokemon {0} poseen más de un tipo; pero uno de ellos es {1}.".format(pokemon_listados_dos_tipos,tipo_a_buscar))
    print("\n")


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
