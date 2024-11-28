
from funciones import *

bandera_ingreso = False

numero = 12
print(f" Tabla de multiplicar del numero: {numero}")
for x in range(0, 13):
    print(f" {numero} * {x} = {numero * x}")




while True:
    opciones = menu_opciones()

    match opciones:
        case 1:
            bandera_ingreso = True
            x = int(input("\n Ingresa primer numero: "))
            y = int(input(" Ingresa segundo numero: "))

        case 2:
            if bandera_ingreso == True:
                resulado_suma = sumar_numero(x, y)
                print(f"\n *La suma es: {resulado_suma}")

        case 3:
            if bandera_ingreso == True:
                resulado_resta = resta_numero(x, y)
                print(f"\n *La resta es: {resulado_resta}")

        case 4:
            if bandera_ingreso == True:
                resultado_multiplicar = multiplicar_numero(x, y)
                print(f"\n *La multiplicacion es: {resultado_multiplicar}")
        
        case 5:
            if bandera_ingreso == True:
                resultado_dividir = dividir_numero(x, y)
                print(f"\n *La divicion es: {resultado_dividir}")

        case 6:
            seguir = input("\n Deseas salir: ")
            if seguir != "no":
                break