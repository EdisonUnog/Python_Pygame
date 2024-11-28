import pokemon_sim as poke
import re
ruta_json = "pokedex.json"
output = "lista_pokemon.csv"
def imprimir_menu():
    print("\n{0}\n1) Listar los últimos N pokemones.\n"
            "2) Ordenar y Listar pokemones por poder.\n"
            "3) Ordenar y Listar pokemones por ID.\n"
            "4) Calcular la cantidad promedio de las key tipo lista.\n"
            "5) Buscar pokemones por tipo.\n"
            "6) Exportar a CSV la lista de pokemones ordenada según opción elegida anteriormente [1-4].\n"
            "7) Salir.\n".format("MENÚ".center(50,"-")))

def app_pokedex():
    lista_poke = poke.leer_archivo(ruta_json).copy()
    lista_a_guardar = []

    while True:
        imprimir_menu()
        key = "id"
        respuesta = ""
        while not re.match("^[1-7]{1}$",respuesta):
            respuesta = input("Eliga una opción : ")

        if respuesta=="1":
            a_listar =""
            while not re.match("^[0-9]{1,2}$",a_listar):
                a_listar= input("¿Cuantos pokemones desea listar?")
            lista_ordenada = poke.funct_listar_pokes(lista_poke,a_listar)
            poke.funct_imprimir_pokes(lista_ordenada,"id")
            lista_a_guardar = lista_ordenada.copy()

        elif respuesta=="2":
            asc_o_desc=""
            while not re.match("asc|desc",asc_o_desc):
                asc_o_desc = input("¿Desea ver la lista en forma ascendente o descendente? (asc|desc) ")
            lista_ordenada = poke.funct_ordenar_y_listar(lista_poke,"poder")
            if asc_o_desc == "desc":
                lista_ordenada.reverse()
            poke.funct_imprimir_pokes(lista_ordenada,"poder")
            lista_a_guardar = lista_ordenada.copy()

        elif respuesta=="3":
            asc_o_desc=""
            while not re.match("^(asc|desc)$",asc_o_desc):
                asc_o_desc = input("¿Desea ver la lista en forma ascendente o descendente? (asc|desc) ")
            lista_ordenada = poke.funct_ordenar_y_listar(lista_poke,"id")
            if asc_o_desc == "desc":
                lista_ordenada.reverse()
            poke.funct_imprimir_pokes(lista_ordenada,"id")
            lista_a_guardar = lista_ordenada.copy()

        elif respuesta=="4":
            key = ""
            menor_o_mayor = ""
            while not re.match("^(evoluciones|fortaleza|debilidad|tipo|poder)$",key):
                key = input("¿De que caracteristica desea sacar el promedio? ")
            promedio = poke.funct_sacar_promedio(lista_poke,key)
            while not poke.funct_validar_string("(mayor|menor)",menor_o_mayor):
                menor_o_mayor = input("¿Desea listar los heroes que sean mayor o menor al promedio? ").lower()
            pokes_listados = poke.funct_listar_segun_numero(lista_poke,promedio,key,menor_o_mayor)
            poke.funct_imprimir_pokes(pokes_listados,key)
            lista_a_guardar = pokes_listados.copy()

        elif respuesta=="5":
            tipo = ""
            while not re.match("^(veneno|hielo|fuego|electrico|agua|acero|psiquico|lucha|fantasma|planta|volador|electrico)$",tipo):
                tipo = input("Eliga un tipo (veneno|hielo|fuego|electrico|agua|acero|psiquico|lucha|fantasma|planta|volador|electrico) : ")
            poke.funct_buscar_pokemon_por_tipo(lista_poke,tipo)


        elif respuesta=="6":
            poke.guardar_archivo(output,lista_a_guardar,key)

        elif respuesta=="7":
            break

app_pokedex()