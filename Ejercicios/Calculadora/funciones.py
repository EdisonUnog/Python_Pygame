
def menu_opciones()->int:
    print("\n 1._Ingresar valores")
    print(" 2._sumar")
    print(" 3._restar")
    print(" 4._multiplicar")
    print(" 5._dividir")
    print(" 6._salir...")
    opcion = int(input("\n Ingresa un opcion: "))
    while opcion < 1 or opcion > 6:
        opcion = int(input("\n Ingresa un opcion: "))
    return opcion


def sumar_numero(primer_num:int, segundo_num:int)->int:
    
    suma = primer_num + segundo_num
    return suma

def resta_numero(primer_num:int, segundo_num:int)->int:

    resta = primer_num - segundo_num
    return resta

def multiplicar_numero(primer_num:int, segundo_num:int)->int:
    multiplicar = primer_num * segundo_num
    return multiplicar

def dividir_numero(primer_num:int, segundo_num:int):
    dividir = None
    if segundo_num != 0:
        dividir = primer_num / segundo_num

    return dividir
