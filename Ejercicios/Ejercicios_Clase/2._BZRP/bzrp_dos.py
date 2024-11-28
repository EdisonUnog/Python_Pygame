from data import lista_bzrp
from funciones_bzrp import *

seguir = True

while True:
    
    opcion = menu_bzrp()

    match opcion:
        case 1:
            #mostrar_lista_temas()
            mostrar_lista_temas_sintaxis(lista_bzrp)
        
        case 2:
            #mostrar_lista_temas_views()
            mostrar_lista_temas_views_sintaxis(lista_bzrp)
        
        case 3:
            mostar_max_views()
            mostrar_max_views_sintaxis(lista_bzrp)

        case 4:
            mostrar_min_views()
            mostrar_min_views_sintaxis(lista_bzrp)

        case 5:
            mostar_cantidad_promedio_views()
            pass

        case 6:
            seguir = input("\n deseas salir si/no: ")
            if seguir != "no":
                print("\n **GRACIAS**\n")
                break
    

