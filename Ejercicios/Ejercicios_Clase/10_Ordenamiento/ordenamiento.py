
import re

#__ORDENAMIENTO DE NUMEROS EN UNA LISTA

numeros = [4,3,2,5,1]
print(f"\n*Numeros desordenados: ")
print(f"{numeros}")

for i in range(len(numeros)-1):#VERDES
    for j in range(i+1, len(numeros)):#NARANJAS
        if numeros[i] > numeros[j]:
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux

print(f"\n*Numeros ordenados: ")
print(f"{numeros}")


#__ORDENAMIENTO DE NOMBRES DE UNA LISTA


nombres = ["Edison", "Ana", "Zoila", "Bertha"]
print(f"\n*Nombres desordenados:")
print(f"{nombres}")

for i in range(len(nombres)-1):
    for j in range(i+1, len(nombres)):
        if nombres[i] > nombres[j]:
            aux = nombres[i]
            nombres[i] = nombres[j]
            nombres[j] = aux

print(f"\n*Nombres ordenados: ")
print(f"{nombres}")

#__FUNCION DE ORDENAMIENTO

def sort_nombres(lista:list)->list:
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

    return lista

orden = sort_nombres(nombres)
print("\n*lista_Funcion nombres ordenados: ")
print(f"{orden}")

#--------------------------------------------------------------------

lista_nombres = [{"nombre":"Edison","edad":26},
                {"nombre":"Zoila","edad":30},
                {"nombre":"Ana","edad":33}]

print("\nSin ordenamiento")
for i in lista_nombres:
    print(i)

def sort_lista_nombres(lista:list)->list:
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):

            if lista[i]["edad"] < lista[j]["edad"]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
            
            elif lista[i]["edad"] == lista[j]["edad"]:
                if lista[i]["nombre"] > lista[j]["nombre"]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

    return lista

result = sort_lista_nombres(lista_nombres)
print(f"\n*Nombres de diccionario ordenados: ")
print(f"{result}")


# numero negativos a positivos:
# crear una funcion

def valor_adsoluto(valor):
    if valor < 0:
        valor = -valor
    
    return valor

numero = valor_adsoluto(222)
print(numero)

