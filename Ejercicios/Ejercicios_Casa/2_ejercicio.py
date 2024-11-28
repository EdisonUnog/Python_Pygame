'''
Edison Francisco Uñog Valencia...

Debemos hacer un programa para que el usuario recuerde las reglas de estilo de
python, entonces debemos pedirle al usuario un número entre el 1 y el 8,
al ingresar el número debemos mostrarle que regla de estilo representa y su
descripción (Sacar la información de las diapositivas de las reglas de estilo).
En caso de que ingrese un numero fuera del rango deberá mostrarle al usuario
“Error, regla de estilo inexistente”
'''

numero = int(input(" Ingresa numero del 1 al 8: "))

while numero >=1 or numero <=2:
    match numero:
        case 1:
            print("mensaje 1")
            break

        case 2:
            print("mensaje 2")
            break

        case 3:
            print("mensaje 2")
            break

        case 4:
            print("mensaje 2")
            break

        case 5:
            print("mensaje 2")
            break

        case 6:
            print("mensaje 2")
            break

        case 7:
            print("mensaje 2")
            break

        case 8:
            print("mensaje 2")
            break

    print("error")
    break