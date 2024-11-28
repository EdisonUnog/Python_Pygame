import library as funct
import re

ruta = "data_stark_modif.json"
output = "data_stark.csv"

def imprimir_menu():
    print(
        "\n{0}\n"
        "1) Listar los primeros N héroes. El valor de N será ingresado por el usuario .\n"
        "2) Ordenar y Listar héroes por altura.\n"
        "3) Ordenar y Listar héroes por fuerza.\n"
        "4) Calcular promedio de cualquier key numérica.\n"
        "5) Buscar héroes por inteligencia [good, average, high] y listar en consola los que cumplan dicha búsqueda.\n"
        "6) Exportar a CSV la lista de héroes ordenada.\n"
        "7) Salir.\n".format("MENÚ".center(50,"-"))
    )

def app_parcial()->None:
    lista_heroes = funct.leer_archivo(ruta).copy()
    lista_a_guardar = []

    while True: 
        imprimir_menu()
        while True:
            opcion = input("Ingrese un número para continuar : ")
            if funct.funct_validar_string("^[1-7]{1}$",opcion):
                opcion = int(opcion)
                break
            else:
                print("Número invalido, vuelva a ingresar : ") 

        if opcion == 1:
            heroes_a_listar = ""
            key = ""
            heroes_listados = [ ]
            while not funct.funct_validar_string("^[0-9]{1,2}$",heroes_a_listar):
                heroes_a_listar = input("¿Cuantos héroes desea listar? ")
            key = input("¿Que dato desea agregar? identidad / fuerza / altura / inteligencia. \n")
            while not funct.funct_validar_string("(identidad|fuerza|altura|inteligencia)",key):
                heroes_a_listar = int(heroes_a_listar)
            heroes_listados = funct.funct_listar_heroes(lista_heroes,int(heroes_a_listar))
            lista_a_guardar = heroes_listados.copy()
            funct.funct_imprimir_heroes(heroes_listados,key)

        elif opcion == 2:
            ordenador = ""
            while not funct.funct_validar_string("(asc|desc)",ordenador):
                ordenador = input("¿Desea ver los heroes de manera ascendente (asc) o descendente (desc)? ").lower()
            heroes_listados = funct.funct_ordenar_y_listar(lista_heroes,"altura")
            if ordenador == "desc":
                heroes_listados.reverse()
            funct.funct_imprimir_heroes(heroes_listados,"altura")
            lista_a_guardar = heroes_listados.copy()

        elif opcion == 3:
            ordenador = ""
            while not funct.funct_validar_string("(asc|desc)",ordenador):
                ordenador = input("¿Desea ver los heroes de manera ascendente (asc) o descendente (desc)? ").lower()
            heroes_listados = funct.funct_ordenar_y_listar(lista_heroes,"fuerza")
            if ordenador == "desc":
                    heroes_listados.reverse()
            funct.funct_imprimir_heroes(heroes_listados,"fuerza")
            lista_a_guardar = heroes_listados.copy()
        
        elif opcion == 4:
            key = ""
            while not funct.funct_validar_string("(fuerza|peso|altura)",key):
                key = input("Desea sacar promedio de :  altura , fuerza o peso ? ")
            promedio = funct.funct_sacar_promedio(lista_heroes,key)
            menor_o_mayor = ""
            heroes_listados = []
            while not funct.funct_validar_string("(mayor|menor)",menor_o_mayor):
                menor_o_mayor = input("¿Desea listar los heroes que sean mayor o menor al promedio? ").lower()
            heroes_listados = funct.funct_listar_segun_numero(lista_heroes,promedio,key,menor_o_mayor)
            funct.funct_imprimir_heroes(heroes_listados,key)
            lista_a_guardar = heroes_listados.copy()
            
        elif opcion == 5:
            tipo_de_inteligencia = ""
            while not funct.funct_validar_string("(good|average|high)",tipo_de_inteligencia.lower()):
                tipo_de_inteligencia = input("Ingrese que tipo de inteligencia quiere listar : good , average , high. ")
            heroes_listados = funct.funct_buscar_por_inteligencia(tipo_de_inteligencia)
            funct.funct_imprimir_heroes(heroes_listados,key)
            lista_a_guardar = heroes_listados.copy()
            
        elif opcion == 6:
            nombre_archivo = "default"
            while not funct.funct_validar_string("[0-9a-z_-]",nombre_archivo):
                nombre_archivo = input("Ingrese el nombre que desea poner al archivo.")
            funct.guardar_archivo(output+nombre_archivo+".csv",lista_a_guardar,key)

        elif opcion == 7:
            print("Programa finalizado.")
            break

app_parcial()