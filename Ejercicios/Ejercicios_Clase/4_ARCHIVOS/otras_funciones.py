
def formato_fecha(tema:dict):
    fecha_string = tema['date']
    fecha_split = fecha_string.split(" ")
    fecha = fecha_split[0].spit("-")
    dia = fecha[2]
    mes = fecha[1]
    anio = fecha[0]
    print(f"{dia}/{mes}/{anio}")

def test(lista:list):
    for x in lista:
        #regex(x['tiel'])
        pass

