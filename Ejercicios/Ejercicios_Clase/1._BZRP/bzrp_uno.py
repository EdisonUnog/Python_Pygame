from data import lista_bzrp
from funciones_bzrp import *

seguir = True

while True:
    
    opcion = menu_bzrp()

    match opcion:
        case 1:
            mostrar_lista_temas(lista_bzrp)
        
        case 2:
            mostrar_lista_temas_views()
        
        case 3:
            mostar_max_views()

        case 4:
            mostrar_min_views()

        case 5:
            #mostar_cantidad_promedio_views()       
            buscar_temas_mas_largo(lista_bzrp)

        case 6:
            seguir = input("\n deseas salir si/no: ")
            if seguir != "no":
                print("\n **GRACIAS**\n")
                break
    

