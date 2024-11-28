#from data_animal import lista_animales

lista_animales = [] #lista general

contador = 0

while contador < 1:

    diccionario_animal = {} #diccionario, con cada uno de sus datos

    animal = input("\n Ingresa animal: ")
    tipo = input(" Ingresa tipo: ")

    diccionario_animal["animal"] = animal
    diccionario_animal["tipo"] = tipo

    lista_animales.append(diccionario_animal)

    contador += 1
    print(diccionario_animal)


def imprimi(lista:list[dict]):
    for x in lista:
        print(f"\n **Animal: {x['animal']}, Tipo: {x['tipo']}")

imprimi(lista_animales)


