'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - 3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
import funciones
import re
output = "PP_STARWARS/lista.csv"

def starwars_app():
    lista_personajes = funciones.cargar_json("PP_STARWARS/data.json")
    lista_a_guardar = []
    while(True):
        print("1 - Listar los personajes ordenados por altura\n"
                "2 - Mostrar el personaje mas alto de cada genero\n"
                "3 - Ordenar los personajes por peso\n"
                "4 - Armar un buscador de personajes\n"
                "5 - Exportar lista personajes a CSV\n"
                "6 - Salir\n")

        respuesta = ""
        while not re.search("^[1-6]{1}$",respuesta):
            respuesta = input("Ingrese un número para continuar : ")
            
        if(respuesta=="1"):
            funciones.funct_normalizar_datos(lista_personajes,"height")
            lista_creada = funciones.funct_ordenar_y_listar(lista_personajes,"height")
            funciones.funct_imprimir_datos(lista_creada,"height")
            lista_a_guardar = lista_creada.copy()

        elif(respuesta=="2"):
            funciones.funct_imprimir_mas_alto_por_genero(lista_personajes)

        elif(respuesta=="3"):
            funciones.funct_normalizar_datos(lista_personajes,"mass")
            lista_creada = funciones.funct_ordenar_y_listar(lista_personajes,"mass")
            funciones.funct_imprimir_datos(lista_creada,"mass")
            lista_a_guardar = lista_creada.copy()

        elif(respuesta=="4"):
            personaje = ""
            while not re.search("[a-zA-z ]",personaje):
                personaje = input("Ingrese el personaje que desea buscar : ")
            funciones.funct_buscar_personaje(lista_personajes,personaje)

        elif(respuesta=="5"):
            funciones.guardar_archivo(output,lista_a_guardar)

        elif(respuesta=="6"):
            break


starwars_app()

