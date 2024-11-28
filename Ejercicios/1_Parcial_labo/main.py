from funciones_dbz import *
#from funcion import*

lista_DBZ = parsear_csv("DBZ.csv")

validar = False
seguir = True

while True:

    opcion = menu_principal()
    match opcion:
        case "1":
            archivo = parsear_csv("DBZ.csv")
            imprimir_dato(archivo)
        
        case "2":
            listar_cantidad_por_raza(lista_DBZ, 'raza')
        
        case "3":
            listar_personaje_por_raza(lista_DBZ,'raza')
        
        case "4":
            dato = listar_personaje_por_habilidaes(lista_DBZ, 'habilidad')
            imprimir_dato(dato)
        
        case "5":
            dato = jugar_batalla(lista_DBZ)
            imprimir_dato(dato)

        case "6":
            validar = True
            dato = guardar_json(lista_DBZ)
            imprimir_dato(dato)

        case "7":
            validar == False 
            if validar != False:
                leer_archivo("\n Ingresa nombre de archivo: ")
            else:
                print("\n ingresa a la opcion 6")

        case "8":
            print("opcion 8\n")
            actualizar_lista_csv(lista_DBZ,"lista_actualizada.csv")

        case "9":
            codigos(lista_DBZ)

        
        case "10":
            seguir = input("\n deseas salir si/no: ")
            if seguir != "no":
                print("\n **GRACIAS**\n")
                break