heroe = " "
habilidades_mensaje = " "
heroe_nombre = " "
heroe_data = []
heroes_para_reclutar = [
    "Batman", "BatWoman", "BatGirl",
    "Wonder Woman", "Aquaman", "Shazam",
    "Superman", "Super Girl", "Power Girl"
]
heroes_info = {
    "Super Girl": {
        "ID": 1,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Volar", "Fuerza", "Velocidad"],
        "Identidad": "Kara Zor-El"
    },
    "Shazam": {
        "ID": 25,
        "Origen": "Tierra",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Magia", "Fuerza", "Velocidad"],
        "Identidad": "Billy Batson"
    },
    "Power Girl": {
        "ID": 14,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Congelar", "Congelar", "Congelar"],
        "Identidad": "Karen Starr"
    },
    "Wonder Woman": {
        "ID": 29,
        "Origen": "Amazonia",
        "Habilidades": ["Agilidad", "Fuerza", "Lazo de la verdad", "Escudo"],
        "Identidad": "Diana Prince"
    }
}
for heroe in heroes_para_reclutar:
    if heroe in heroes_info.keys(): #<--devuelve Booleano
        heroe_nombre = heroe
        info_heroes = heroes_info[heroe]
        id_heroe = info_heroes["ID"]
        origen_heroe = info_heroes["Origen"]
        identidad_heroe = info_heroes["Identidad"]
        habilidades_list = info_heroes["Habilidades"]

        habilidades_unicas = set(habilidades_list)
        habilidades_list = list(habilidades_unicas) #<--para qe no se repitan
        
        habilidades_mensaje = " | ".join(habilidades_list)
        #print(heroe,":\n ID : ", id_heroe, " Origen : " , origen_heroe,  " Identidad secreta : ", identidad_heroe ,"\n HABILIDADES : ",  habilidades_mensaje,"\n")  
        print("Heroe : {0} \nID : {1} \nOrigen : {2} \nIdentidad Secreta : {3}\nHabilidades : {4}\n".format(heroe_nombre,id_heroe,origen_heroe,identidad_heroe,habilidades_mensaje))
'''
Preparando todo para reclutar héroes y heroínas para la liga de la justicia, el departamento de HR dispone de una larga 
lista de justicieros pero solo tiene información detallada de algunos de ellos.
Es por eso que te piden que desarrolles un pequeño programa el cual basado en la lista 'heroes_para_reclutar' 
busque en el diccionario 'heroes_info' los que coincidan y los guarde en un nuevo diccionario para 
luego imprimir por consola todos sus datos. (id, origen, etc)
TIP: Las habilidades están repetidas, busca la manera de que en el resultado final no existan duplicados, que usarías para eso?
'''