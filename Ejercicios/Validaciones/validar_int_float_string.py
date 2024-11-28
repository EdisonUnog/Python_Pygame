import re

'''
    la funcion analiza si el dato es numerico entero, positico o negativo
    Recibe un str que representa un numero
    Devuelve el numero en formato int sin espacios,si es no numerico = -1 , negativo = -2, otro error = -3
'''

def validar_entero(cadena_num:str)->int:
    
    numero_str = input(cadena_num)
    
    entero = re.findall("[0-9]+",numero_str) #"[0-9]+.[0-9]+" num float
    letras = re.findall("([a-zA-Z]+)",numero_str)
    negativos = re.findall("-([0-9]+)",numero_str)
    
    if(len(entero) > 0 and len(negativos) == 0 and len(letras) == 0):
        numero = int (entero[0]) 
    
    else:      
        if(len(letras) > 0):
            print("\n Error..")
            numero = -1      
        elif(len(negativos) > 0):
            numero = -2  
        else:
            numero = -3
    return numero

numero = validar_entero("ingresa numero entero: ")
print(numero)

#############################################################################################

'''
    la funcion analiza si el dato es numerico flotante, positico o negativo
    Recibe un str que representa un numero
    Devuelve el numero en formato int sin espacios,si es no numerico = -1 , negativo = -2, otro error = -3
'''
def validar_flotante(cadena_num:str)->float:
    numero_str = input(cadena_num)
    flotante = re.findall("[0-9]+.[0-9]+",numero_str) #"[0-9]+.[0-9]+" numero flotante
    letras = re.findall("([a-zA-Z]+)",numero_str)
    negativos = re.findall("-([0-9]+.[0-9]+)",numero_str)
    
    if(len(flotante) > 0 and len(negativos) == 0 and len(letras) == 0):
        numero = float (flotante[0]) 
        
    else:
        if(len(letras) > 0):
            numero = -1         
        elif(len(negativos) > 0):
            numero = -2 
        else:
            numero = -3  
    return numero


#############################################################################################
'''
    La funcion verifica el valor si es un string sin numeros,en caso de tener barras las reemplaza por espacios
    Recibe un valor en str
    Devuelve el valor sanitizado 
'''
def validar_string(cadena_str:str)->str:

    obtengo_str = input(cadena_str)

    valido_numero = re.findall("[0-9]+",obtengo_str)
    str_sin_numeros = bool(re.search('^[a-zA-ZñÑ ]+$',obtengo_str))

    if (str_sin_numeros == True and len(valido_numero) == 0):
        cadena = obtengo_str
        cadena = cadena.replace("/"," ")
        cadena = cadena.lower()               
    else:
        cadena = "Error"
    
    return cadena.capitalize()


'''letra = validar_string("ingresa letras: ")
print(letra)'''

