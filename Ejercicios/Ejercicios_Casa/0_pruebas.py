###################_SEGUIR?_#################
'''
acum = 0

while True:
    numero = int(input("Ingresa numero: "))
    acum += numero

    seguir = input("\n Desea seguir si / no: ")
    if seguir != "si":
        break
    
print(f" acumuñudar: {acum}")
'''
##############_NUMERO_MIN_MAX#################
'''
edad_minima = 0
flag_edad = True

if voto == "nacho":
    if(edad < edad_minima or flag_edad == True):
        edad_minima = edad
        nombre_minimo = nombre_votante
        flag_edad = False
'''
###########_WHILE_EN_VEZ_DE_FOR###############
'''
acum_numero = 0 
num = 2

while True:

    numero = int(input(" Ingresa numero: "))
    acum_numero += numero

    num -= 1
    if num == 0:
        break
'''

'''
lista_numeros=[1,2,4,5,77,-1]

for x in lista_numeros:
    print(x, end = " ")

'''

'''
lista = [1, 3, 6, 3, 2, 1]
s = set(lista)
print(s)       # {1, 2, 3, 6}
print(type(s)) # <class 'set'>
'''
######################_Validar_Cadena_##############################
'''
import re

def validar_cadena(palabra):
    ascii = '^[a-zA-Z0-9_]+$'

    return bool(re.search(ascii, palabra))

texto = 'delta'
print(validar_cadena(texto))

#########
def validar_cadena(palabra):
    ascii = '^[a-zA-Z0-9_]+$'

    if bool(re.search(ascii, palabra)) == True:
        print(palabra)
    else: 
        print("Error")
texto = 'delta_'
validar_cadena(texto)

print("")
'''

########################################################################
'''
def validar_string(texto:str)->str:
    cadena = input(texto)
    ascii = '^[a-zA-Z]+$'

    if bool(re.search(ascii, cadena)) == True:
        return cadena
    else:
        print("\n Error. solo cadena de texto")
    

def pedir_dato_string():
    cadena = validar_string("ingresa nombre")
    if cadena != True:
        print(cadena)

pedir_dato_string()
'''

########################################################################
'''
def agregar_personas_lista(lista, nombre):
    lista.append(nombre)

lista_nombres = ['edison', 'franc'] 
print(lista_nombres)

agregar_personas_lista(lista_nombres, 'jose')
print(lista_nombres)
'''

###########################_Uso_De_split()_###############################
''' 
cadena = "Edison unog"

def contar_cadena(cadena:str):
    contador = cadena.split()
    
    #return len(contador) ->cuenta las palabras
    return len(contador)  #->#['Edison', 'unog'] --> result

mostrar = contar_cadena(cadena)
print(mostrar)
'''
#############################_Contar_Letras_###############################
''' 
nombre = "edison uñog"

def contar_letras(cadena:str)->int:
    if type(cadena) == str:
        largo_cadena = len(cadena)
        return int(largo_cadena)
    

contador = contar_letras(nombre)
print(f"\n *    Cantidad de letras: {contador} \n")
'''

# upper -> minisculas
# lower -> MAYUSCULAS
# capitalize() -> primera letra en mayusculas y las demas en minusculas

# replace() -> reemplaza una palabra con otra  
  #ejem:
#txt = "I like bananas"

#x = txt.replace("bananas", "apples")

#print(x)

#############################_Contar_split_RegEx_###############################
'''import re

texto = 'uno 1 dos 2 tres 3 cuatro'

print(re.split(' ', texto))
#['uno', '1', 'dos', '2', 'tres', '3', 'cuatro']

print(re.split('[0-9]+', texto))
#['uno ', ' dos ', ' tres ', ' cuatro']

print(re.split('[a-z ]+', texto))
#['', '1', '2', '3', '']'''


#############################_Contar_Search_RegEx_###############################
'''import re

texto = ' uno 1 dos 2 tres 3 cuatro'

print(re.search(' ', texto))
#<re.Match object; span=(0, 1), match=' '>

print(re.search('[0-9]+', texto))
#<re.Match object; span=(5, 6), match='1'>

print(re.search('[a-z ]+', texto))
#<re.Match object; span=(0, 5), match=' uno '>'''