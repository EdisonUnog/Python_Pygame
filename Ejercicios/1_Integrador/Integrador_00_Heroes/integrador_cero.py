
from funciones_integrador_cero import *

seguir = True
while True:

    opcion = menu_integrador_cero()

    match opcion:
        case 1:
            mostrar_nombre_heroes()
        
        case 2:
            mostrar_nombre_altura()
        
        case 3:
            mortrar_heroe_max_alto()
        
        case 4:
            mostrar_heroe_min_altura()
        
        case 5:
            mostrar_promedio_altura()

        case 6:
            mostrar_heroe_mas_pesado()

        case 7:
            mostrar_heroe_menos_pesado()
        
        case 8:
            seguir = input("\n deseas salir si/no: ")
            if seguir != "no":
                print("\n **GRACIAS**\n")
                break