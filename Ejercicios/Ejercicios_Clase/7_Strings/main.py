from data import lista_bzrp

def prueba():
    titulo = "QUEVEDO || BZRP Music Sessions #52"
    cadena = titulo.split("||")
    artista = cadena[0].strip()
    cadena2 = cadena[1].split("#")
    tipo = cadena2[0].strip()
    numero = cadena2[1].strip()
    print(f"{artista} - {tipo} - {numero}")


def prueba2(titulo:str):
    #titulo = "QUEVEDO || BZRP Music Sessions #52"
    cadena = titulo.split("||")
    artista = cadena[0].strip()
    cadena2 = cadena[1].split("#")
    tipo = cadena2[0].strip
    numero = cadena2[1].strip()
    print(f"{artista} - {tipo} - {numero}")

def prueba3(titulo:str):
    #titulo = "QUEVEDO || BZRP Music Sessions #52"
    cadena = titulo.split("||")
    if( len(cadena) > 1 ):
        artista = cadena[0].strip()
        cadena2 = cadena[1].split("#")
        if( len(cadena2) > 1 ):
            tipo = cadena2[0].strip()
            numero = cadena2[1].strip()
            print(f"{artista} - {tipo} - {numero}")


# 'QUEVEDO || BZRP Music Sessions #52'
def prueba4(titulo:str):
    tipo = "BZRP Music Sessions"
    parte1= titulo.split("BZRP Music Sessions")
    if( len(parte1) == 2 ):
        artista = parte1[0].replace("||","").strip()
        numero = parte1[1].replace("#","").strip()
        print(f"{artista} - {numero} - {tipo}")


def test_nom(lista:list):
    for x in lista:
        prueba4(x['title'])

test_nom(lista_bzrp)

#'https://youtube.com/watch?v=A_g3lMcWVy0'
def url(tema:dict):
    '''cadena = tema["url"].split("=")
    print(cadena[1])'''
    
    '''codigo = tema["url"].replace("https://youtube.com/watch?v=","")
    print(codigo)'''

    '''url= tema["url"]
    codigo = url[28:]
    print(codigo)'''

    '''l = len("https://youtube.com/watch?v=")
    url= tema["url"]
    codigo = url[l:]
    print(codigo)'''

    url= tema["url"]
    indice = url.index("=")
    codigo = url[indice + 1:]
    #print(codigo)


'''def test_url(lista:list):
    for x in lista:
        #url(x['title'])
        url(x)

test_url(lista_bzrp)'''

'''def formato_fecha(fecha_cadena:str):
    #fecha_string = tema['date']
    fecha_split = fecha_cadena.split(" ")
    fecha = fecha_split[0].split("-")
    anio = fecha[0]
    mes = fecha[1]
    dia = fecha[2]
    print(f"{dia}/{mes}/{anio}")

def test_date(lista:list):
    for x in lista:
        formato_fecha(x['date'])

test_date(lista_bzrp)'''

lista = [4,3,2,5,1]
print(lista)
for i in range(len(lista)-1):#VERDES
    for j in range(i+1, len(lista)):#NARANJAS
        if lista[i] < lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

print(lista)


nombres = ["zoila", "Maria", "Ana"]
print(nombres)
nombres.sort()
print(nombres)
