
from data_stark import lista_personajes
from funciones_integrador_uno import *

numero = '123'
print(type(numero))

seguir = True
while True:

    opcion = menu_integrador_uno()
    match opcion:
        case 1:
            print_por_genero_masculino(lista_personajes)
        
        case 2:
            print_por_genero_femenino(lista_personajes)
        
        case 3:
            print_max_alto_masculino(lista_personajes)
        
        case 4:
            print_max_alto_femenino(lista_personajes)
        
        case 5:
            print_bajo_masculino(lista_personajes)

        case 6:
            print_bajo_femenino(lista_personajes)

        case 7:
            print_promedio_m(lista_personajes)
        
        case 8:
            print_promedio_f(lista_personajes)

        case 9:
            print_heroes_tipos_ojos(lista_personajes)

        case 10:
            print_heroes_tipos_cabello(lista_personajes)

        case 11:
            print_heroes_tipos_inteligencia(lista_personajes)

        case 12: ###
            print_heroes_mismos_ojos(lista_personajes)

        case 13:
            print_heroes_mismo_pelo(lista_personajes)

        case 14:
            print_heroes_misma_inteligencia(lista_personajes)
            
        case 15:
            seguir = input("\n deseas salir si/no: ")
            if seguir != "n":
                print("\n **GRACIAS**\n")
                break