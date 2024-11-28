import re
import json
import random
import datetime

######################################################################################################
def imprimir_dato(dato:str):
    print(f"{dato}")

######################################################################################################
##_Funcion_Para_Leer_Archivo_CSV_######

def parsear_csv(path:str)->list:
    
    lista_dbz= []
    
    archivo_dbz = open(path, "r", encoding= "utf-8") 
    
    for line in archivo_dbz:
        lectura = re.split(',|\n',line)
        personajes = {}
        personajes['id'] = lectura[0].strip()
        personajes['nombre'] = lectura[1]
        personajes['raza'] = lectura[2]
        personajes['poder_de_pelea'] = lectura[3]
        personajes['poder_de_ataque'] = lectura[4]
        personajes['habilidad'] = lectura[5].split("|$%")

        lista_dbz.append(personajes)
    
    archivo_dbz.close()

    return lista_dbz

######################################################################################################
##_Funcion_Listar Cantidad Por Raza_####
def listar_cantidad_por_raza(lista:list, clave:str):
    if type(lista) == list and len(lista) > 0:
        contador = {}
        for x in lista:
            if x[clave] not in contador:
                contador[x[clave]] = 1
            else:
                contador[x[clave]] += 1

        contadores(contador) # funcion para imprimir la lista filtrada

def contadores(contador:dict):
    for raza, cantidad in contador.items():
        print(f"\n {cantidad} de la raza: {raza}")

######################################################################################################
##_Funcion_Listar_Nombres_Por_Raza_####
def listar_personaje_por_raza(lista:list, clave:str):
    if type(lista) == list and len(lista) > 0:
        lista_nombre = []
        for x in lista:
            personaje = x[clave]
            lista_nombre.append(personaje)
        lista_filtrada = set(lista_nombre)

        for personaje in lista_filtrada:
            print(f"{personaje} :")

            for x in lista:
                if x[clave] == personaje:
                    print(f"\t {x['nombre']} - {x['poder_de_ataque']}")

######################################################################################################
def listar_habilidad(lista:list)->None:
    if type(lista) == list and len(lista) > 0:
        mensaje = []
        for x in lista:
            habilidad = x['habilidad']
            mensaje = "habilidades: {0}".format( habilidad)
            imprimir_dato(mensaje)

##_Funcion_Mostrar_Personaje_Por_Habilidaes_##
def listar_personaje_por_habilidaes(lista:list, valor:str)->str:
    if type(lista) == list and len(lista) > 0:

        listar_habilidad(lista)

        ingresa_habilidad = input("\n Ingresa habilidad: ").capitalize()
        mensajes = []
        for x in lista:
            if ingresa_habilidad in x[valor]:
                promedio = (int(x["poder_de_pelea"]) + int(x["poder_de_pelea"])) / 2
                mensaje = " {0} es: {1}, poder de pelea: {2}".format(x["nombre"], x["raza"],promedio)
                mensajes.append(mensaje)

        return mensajes
######################################################################################################
##_Funcion_De_Jugar_Batalla_###
def jugar_batalla(lista:list)->str:
    if type(lista) == list and len(lista) > 0:       

        mostra_nombres(lista) # nombres en la lista a seleccionar
        #---------------------------------------------#
        result = comenzar_batalla(lista)
        #---------------------------------------------#
        #guardo en archivo json
        guardar_batalla(result)
        #---------------------------------------------#
    return result

############################################
# funcion que compara poderdes y peleas
def comenzar_batalla(lista:list):
    #---------------------------------------------#
    personaje_user = None

    while personaje_user is None:
        personaje = input("\n Selecciona un personaje: ").capitalize()
        for x in lista:
            if x['nombre'] == personaje:
                personaje_user = x
                break
                    
        if personaje_user is None:
            print("\n no existe")

    personaje_maquina = random.choice(lista)

    if int(personaje_user['poder_de_pelea']) > int(personaje_maquina['poder_de_pelea']):
        ganador = personaje_user
        perdedor = personaje_maquina

    elif int(personaje_user['poder_de_pelea']) < int(personaje_maquina['poder_de_pelea']):
        ganador = personaje_maquina
        perdedor = personaje_user
        
    else:
        return 'empate'
        #---------------------------------------------#
    fecha_combate = datetime.datetime.now()
    fecha_batalla = "{0}-{1}-{2}".format(fecha_combate.year, fecha_combate.month, fecha_combate.day)
    #---------------------------------------------#
    result = "Ganador: {0}, Poder: {1}._ Le gano a {2}, Poder: {3} / fecha: {4}\n"
    result = result.format(ganador['nombre'], ganador['poder_de_pelea'],
                                perdedor['nombre'], perdedor['poder_de_pelea'], fecha_batalla)
    
    return result


# guarad en el alchivo json
def guardar_batalla(resultado):
    with open("resultado_batalla.txt","a") as file:
            file.write(resultado)

# imprime los nombres a seleccionar para la batalla
def mostra_nombres(lista:list):
    nombres = []
    for x in lista:
        nombre = x['nombre'].strip()
        nombres.append(nombre)

    imprimir_dato(nombres)
######################################################################################################
def raza_habilidad(lista:list)->None:
    if type(lista) == list and len(lista) > 0:
        mensaje = []
        for x in lista:
            raza= x['raza']
            habilidad = x['habilidad']
            mensaje = "Raza: {0} -- habilidades: {1}".format(raza, habilidad)
            print(mensaje)
#---------------------------------------------#
##_Funcion_Que_Guarda_Un_Archivo_.json
def guardar_json(lista):
    
    if type(lista) == list and len(lista) > 0:

        imprimir_dato(raza_habilidad(lista))
        
        personajes_coincidentes = []
        
        raza_ingresada = input("Ingrese una raza: ").capitalize()
        habilidad_ingresada = input("Ingrese una habilidad: ").capitalize()
        
        for personaje_dbz in lista:
            if personaje_dbz["raza"] == raza_ingresada and habilidad_ingresada in personaje_dbz["habilidad"]:
                habilidades_no_buscadas = []
                
                for habilidad_dbz in personaje_dbz["habilidad"]:
                    if habilidad_dbz != habilidad_ingresada:
                        
                        habilidades_no_buscadas.append(habilidad_dbz)
                        
                personaje_coincidente = {
                    "nombre": personaje_dbz["nombre"],
                    "poder_de_ataque": personaje_dbz["poder_de_ataque"],
                    "habilidades_no_buscadas": habilidades_no_buscadas
                }
                
                personajes_coincidentes.append(personaje_coincidente)
        
        mi_archivo = f"{raza_ingresada}_{habilidad_ingresada}.json"
        
        with open(mi_archivo, "w") as x:
            json.dump(personajes_coincidentes, x , indent=4)
    
    return mi_archivo

######################################################################################################
##_EJERCICIO_ADICIONAL_LABORATORIO________
'''
Requerimiento extra._
agregar una opcion que permita otorgarle un 50% mas de poder de pelea y un 70% mas de ataque a los saiyan, 
y agregaran a sus habilidades la "transforacion nivel Dios", guardar en un archivo csv los personajes que 
hayan recibido esta actualizacion.
'''
def actualizar_lista_csv(lista:list, path:str):
    
    if type(lista) == list and len(lista) > 0:

        lista_actualizada = []

        for x in lista:

            if x['raza'] == "Saiyan" in "Saiyan-Humano":              
                
                if x['poder_de_pelea'].isnumeric():
                    x['poder_de_pelea'] = float(x['poder_de_pelea']) * 1.5
                
                if x['poder_de_ataque'].isnumeric():
                    x['poder_de_ataque'] = float(x['poder_de_ataque']) * 1.7
                
                x['habilidad'].append("Transformacion Nivel Dios")
                lista_actualizada.append(x)

        with open(path, "w", encoding = "utf-8") as file:
            for x in lista_actualizada:
                datos = f"{x['nombre']},{x['raza']},{int(x['poder_de_pelea'])},{int(x['poder_de_ataque'])},{'-'.join(x['habilidad'])}\n"
                
                file.write(datos)

######################################################################################################
##_Funcion_Lee_Json_##
def leer_archivo(nom_archivo:str):

    archivo = input(nom_archivo)

    with open(archivo,"r") as file:
        datos_Json = json.load(file)

    for x in datos_Json:
        print(f" Nombre: {x['nombre']}")
        print(f" poder de ataque: {x['poder_de_ataque']}")
        print(f" Habilidades: {'-'.join(x['habilidades_no_buscadas'])}")

######################################################################################################
def codigos(lista):
    for x in lista:
        codigo = generar_codigo_personaje(x)   
        imprimir_dato(codigo)

def generar_codigo_personaje(personaje):
    nombre = str(personaje['nombre'])
    raza = str(personaje['raza'])
    poder_de_ataque = int(personaje['poder_de_pelea'])
    poder_de_pelea = int(personaje['poder_de_pelea'])
    id_personaje = int(personaje['id'])

    if poder_de_ataque > poder_de_pelea:
        ganador = 'A'
        valor_mas_alto = poder_de_ataque
    elif poder_de_pelea > poder_de_ataque:
        ganador = 'P'
        valor_mas_alto = poder_de_pelea
    else:
        ganador = 'AP'
        valor_mas_alto = poder_de_ataque

    codigo = f"{nombre[0]}-{ganador}-{valor_mas_alto}-{str(id_personaje).zfill(9)}"
    return codigo
######################################################################################################
#__MENU

def menu_integrador_dos():
    mensaje = "\n 1._Mostrar datos"
    mensaje += "\n 2._Cantidad por raza"
    mensaje += "\n 3._Nombres por raza"
    mensaje += "\n 4._personaje por habilidades"
    mensaje += "\n 5._Jugar batalla"
    mensaje += "\n 6._Guardar en archivo json"
    mensaje += "\n 7._Leer archivo json"
    mensaje += "\n 8._Agregar poder_pelea, poder_ataque y transformacion"
    mensaje += "\n 9._Generar Codigos"
    return mensaje

def validar_entero(numero:str)->bool:
    
    flag = False
    if numero.isdigit:
        flag = True

    return flag

def menu_principal():
    opcion = input(f"{menu_integrador_dos()} \n\n Ingresa una opcion >> ")
    while validar_entero(opcion) == False:
        print("Error")
        opcion = input(f"{menu_integrador_dos()} \n\n Ingresa una opcion >> ")

    return opcion


