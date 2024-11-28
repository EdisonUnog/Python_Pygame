from data_stark import lista_personajes
import re
def funct_extraer_iniciales(nombre_heroe:str)->str:   
        
    if len(nombre_heroe) == 0:
        iniciales = "N/A"
        return iniciales
    
    else:              
        if nombre_heroe.count("-") > 0:
               nombre_heroe = nombre_heroe.replace("-"," ")
        if nombre_heroe.count("The ") > 0:
            nombre_heroe = nombre_heroe.replace("The ","")
        if nombre_heroe.count("the ") > 0:
            nombre_heroe = nombre_heroe.replace("the ","")
        lista_nombres_heroe = nombre_heroe.split(" ")
        if len(lista_nombres_heroe) > 1:
            inicial_list = ""
            for nombre_dividido in lista_nombres_heroe:
                inicial_list += nombre_dividido[0] + "."
            iniciales = inicial_list
            return iniciales
        else :
            iniciales = "{0}.".format(nombre_heroe[:1])
            return iniciales

def funct_definir_iniciales_nombre(heroe:dict)->bool:
    if type(heroe) == type(dict()):
        if "nombre" in heroe.keys():
            iniciales = funct_extraer_iniciales(heroe["nombre"])
            heroe["iniciales"] = iniciales
            return True
    else :
        return False

def funct_agregar_iniciales_nombre(lista_heroes:list)->bool:
    
    if type(lista_heroes) == type(list()):
        if len(lista_heroes) > 0:
            for heroe in lista_heroes:
                funct_definir_iniciales_nombre(heroe)
        return True
    else :
        print("El origen de datos no tiene el formato correcto.")
        return False

def funct_stark_imprimir_nombres_con_iniciales(lista_heroes:list):
    funct_agregar_iniciales_nombre(lista_heroes)
    if type(lista_heroes) == type(list()):
        if len(lista_heroes) > 0:
            for heroe in lista_heroes:
                print("* {0} ({1})".format(heroe["nombre"],heroe["iniciales"]))

def funct_generar_codigo_heroe(id_heroe:int,genero_heroe:str)->str:
    genero_heroe = genero_heroe.upper()
    if type(id_heroe) == int and genero_heroe == "F" or genero_heroe == "M" or genero_heroe == "NB":
        fill = 9 - len(genero_heroe)
        id_heroe = str(id_heroe)
        codigo_heroe = "{0}-{1}".format(genero_heroe,(id_heroe.zfill(fill)))
        return codigo_heroe
    else :
        return "N/A"

def funct_agregar_codigo_heroe(heroe:dict,id_heroe:str)->bool:
    if len(id_heroe) == 10 and len(heroe) > 0:
        heroe["codigo heroe"] = id_heroe
        return True
    else :
        return False

def funct_stark_generar_codigos_heroes(lista_heroes:list):
    if len(lista_heroes) > 0:
        contador = 0
        for heroe in lista_heroes:
            if "genero" in heroe and type(heroe) == type(dict()):
                id_heroe = lista_heroes.index(heroe) + 1
                funct_agregar_codigo_heroe(heroe,funct_generar_codigo_heroe(id_heroe,heroe["genero"]))
                contador += 1
                flag = True
            else :
                flag = False

        if flag == True:
            print("\nSe asignaron {0} códigos.\n"
                    "* El código del primer héroe es : {1}.\n"
                    "* El código del último héroe es : {2}.\n"
                                                            .format(contador,lista_heroes[0]["codigo heroe"]
                                                                    ,lista_heroes[-1]["codigo heroe"]))
        else :
            print("El origen de datos no tiene el formato correcto.") 

def funct_sanitizar_entero(numero_str:str)->int:

        numero_str = numero_str.strip()
        if numero_str.isnumeric() and int(numero_str) > 0:
            numero_str = int(numero_str)
            return numero_str
        else:
            if numero_str.isalnum():
                 return -1
            elif int(numero_str) < 0:
                return -2
            else :
                return -3

def funct_sanitizar_flotante(numero_str:float)->int:
  
    numero_str = numero_str.strip()
    if float(numero_str) > 0:
        numero_str = float(numero_str)
        return numero_str
    elif not numero_str.isnumeric():
        return -1
    elif float(numero_str) < 0:
        return  -2
    else :
        return -3

def funct_sanitizar_string(valor_str:str,valor_por_defecto:str="-"):
       
    if valor_str.count("[0-9]")<=0:
        if valor_str.count("/")>0:
            valor_str = valor_str.replace("/"," ")
        valor_str = valor_str.lower()
        return valor_str
    if len(valor_str) == 0 and not valor_por_defecto == "-":
        valor_por_defecto=valor_por_defecto.lower()
        return valor_por_defecto
    else:
        return "N/A"

print(funct_sanitizar_string("A8Tr"))