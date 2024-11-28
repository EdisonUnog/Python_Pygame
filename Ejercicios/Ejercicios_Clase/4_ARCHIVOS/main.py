
import json
import re


# Sobreescribir - w
# Escribir - a
# Leer - r

'''archivo = open('nombre.TXT','w',encoding="utf-8")
archivo.write("Edison")
archivo.close()'''

'''archivo = open("3_ARCHIVOS.\nombre.txt", "r")
leer = archivo.readlines()
print(leer)
archivo.close()
'''
######################

'''archivo = open("3_ARCHIVOS.\nombre.txt", "r")
leer = archivo.readlines()
for lineas in leer:
    print(lineas)
archivo.close()'''

#print("####################")

#lista = ["Edison", "Silvia", "Alexandra", "Alicia", "Angel"]

#escribe
'''with open("nombre.txt", "w") as archivo:
    for nombres in lista:
        archivo.write(f"{nombres}\n")'''

#lee
'''cont = 0
with open("nombre.txt", "r") as archivo:
    for nombres in archivo:
        cont += 1
        print(f"{cont}._ {nombres}", end="")'''

'''archivo = open("nombre.txt", "r")
leer = archivo.readlines()
for lineas in leer:
    print(lineas, end="")
archivo.close()'''

print("####################")
#################### ARCHIVOS CSV ####################
#____Escribir un archivo csv
'''nombre = ["Edison", "Silvia", "Alexandra"]
apellidos = ["Mendez", "Fernandes", "Coleman"]
edades = [21, 22, 34]

TAM = 3

with open("agenda.csv", "w") as archivo:
    for i in range(TAM):
        registro = "{0},{1},{2}\n".format(nombre[i], apellidos[i], edades[i])
        archivo.write(registro)'''


#___Leer un archivo csv
#with open("EJERCICIOS.\ Ejercicios_Clase.\ 3_ARCHIVOS.\ agenda.csv", "r") as archivo:
'''with open("agenda.csv", "r") as archivo:
    for line in archivo:
        #registro = line.split(",") 
        #print(f"*Nombre: {registro [0]} \n*Apellido: {registro [1]} \n*Edad: {registro [2]}")
        registro = re.split(r",|\n", line)
        print(f"\n*Nombre: {registro [0]} \n*Apellido: {registro [1]} \n*Edad: {registro [2]}")'''


#################### ARCHIVOS JSON ####################
#__Escribir archivo json


'''data = {}
data["alumnos"] = []

data["alumnos"].append({"nombre":"EdisonII","edad":26})
data["alumnos"].append({"nombre":"FranciscoII","edad":27})
data["alumnos"].append({"nombre":"MariaII","edad":20})

with open("alumnos.json","w") as archivo:
    json.dump(data, archivo, indent=4)'''

#__Leer archivo json
'''with open("alumnos.json","r") as archivo:
    data = json.load(archivo)

print(data)'''



####################### BZRAP ######################
#__Funcion para armar un lista de diccionario__Parcear un csv

def parser_csv(path:str)->list:

    lista = []

    archivo = open(path, "r", encoding="utf-8")
    for line in archivo:
        lectura = re.split(",|\n", line)
        tema = {}
        tema['title'] = lectura[0].strip()
        tema['views'] = lectura[1]
        tema['length'] = lectura[2]
        tema['img_url'] = lectura[3]
        tema['url'] = lectura[4]
        tema['date'] = lectura[5]

        lista.append(tema)

    archivo.close()

    return lista

lista = parser_csv("data.csv")
print(f"{lista}")


'''def generar_csv(path:str, lista:list):

    archivo = open(path, "w", encoding="utf-8")

    for tema in lista:
        registro = "{0}, {1}, {2}, {3}, {4}, {5}\n"
        registro = registro.format(tema['title'], tema['views'], tema['length'], tema['img_url'], tema['url'], tema['date'])

        archivo.write(registro)

    archivo.close()

generar_csv("otros.csv", lista)'''



'''def generar_csv_cinco(path:str, lista:list):

    archivo = open(path, "w", encoding="utf-8")

    for i in range(5):
        registro = "{0}, {1}, {2}, {3}, {4}, {5}\n"
        registro = registro.format(lista[i]['title'], lista[i]['views'], lista[i]['length'], 
                                    lista[i]['img_url'], lista[i]['url'], lista[i]['date'])

        archivo.write(registro)

    archivo.close()

generar_csv_cinco("solo_cinco.csv", lista)'''


'''def datos_profesionales():
    persona = {}
    persona["profesionales"] = []
    persona["profesionales"].append({"nombre":"Edison","edad":26, "profesion":"abogado corporativo"})
    persona["profesionales"].append({"nombre":"Francisco","edad":20, "profesion":"ingeniero industrial"})
    persona["profesionales"].append({"nombre":"Angel","edad":50, "profesion":"ingeniero en software"})

    return persona

datos_peronas = datos_profesionales()

def generar_json(path:str, datos:list):
    with open(path,"w") as archivo:
        json.dump(datos, archivo, indent=4)

generar_json("profesionales.json", datos_peronas)'''



#_Funciones_que lee una agenda en csv y la gusrada en json
'''def parser_agenda_csv(path:str):
    lista = []
    f = open(path, "r", encoding="utf-8")
    for i in f:
        indice = re.split(r",|\n", i)
        dato = {}
        dato['nombre'] = indice[0]
        dato['apellido'] = indice[1]
        dato['edad'] = indice[2]

        lista.append(dato)
    return lista

datos = parser_agenda_csv("agenda.csv")
print(datos)

##

def csv_a_json(path:str, lista:list):
    with open(path, "w") as file:
        json.dump(lista, file, indent=4)

csv_a_json("csv_json.json", datos)'''

##_Funcion para leer json
'''def leer_json(path:str):
    #__Leer archivo json
    with open(path,"r") as archivo:
        data = json.load(archivo)
    return data

datos = leer_json("csv_json.json")
print(datos)'''