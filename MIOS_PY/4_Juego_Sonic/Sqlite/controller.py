import sqlite3 as sql

def createDB():
    '''
    La función crea la base de datos con el nombre deseado y la conecta. "sql.connect(nombre)"
    '''
    conexion = sql.connect("Sqlite/ranking.db")
    conexion.commit()# Actualiza los datos realmente en la tabla.
    conexion.close()#cierra la base de datos.

#createDB()
    
def createTable():
    '''
    La funcion abre la base de datos,crea la tabla deseada y al finalizar la cierra automaticamente.
    '''
    with sql.connect("Sqlite/ranking.db") as conexion:
        try:
            sentencia = '''CREATE TABLE puntaje
                        (
                            id integer primary key autoincrement,
                            nombre text,
                            puntos integer
                        )
                    '''#CREATE TABLE son las palabras necesarias para crear la tabla siguiendo del nombre.
                        #Luego dentro de los parentesis el id, que se va a ir incrementando de manera ascendente automaticamente y abajo los campos que quiera.

            conexion.execute(sentencia)#Ejecuta la sentencia para crear la tabla.
            print("Se creo la tabla puntaje")                       
        except sql.OperationalError:
            print("La tabla puntaje ya existe")

# createTable()
            

def insertRow(nombre,puntos):
    '''
    La funcion insertar la información deseada a la base de datos.
    Recibe por parametro la información para cada uno de los campos.
    '''
    with sql.connect("Sqlite/ranking.db") as conexion:
        
        conexion.execute("INSERT INTO puntaje(nombre,puntos) VALUES (?,?)", (nombre,puntos))
        conexion.commit()# Actualiza los datos realmente en la tabla

# insertRow("Sonic",6597)
# insertRow("Player",0)
# insertRow("Player",0)
# insertRow("Player",0) 
        
def readRows():#Selecciona solo una fila
    '''
    Lee todos los datos de la tabla de manera asc y con un limite de 5 valores.
    Retorna una lista con los datos dentro en tipo tupla.
    '''
    conn = sql.connect("Sqlite/ranking.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM puntaje ORDER BY puntos DESC LIMIT 5"
    cursor.execute(instruccion)
    datos = cursor.fetchall()#devolver todos los datos seleccionados
    conn.commit()
    conn.close()    
    return datos


# data = readRows()
# print(data)

def readRows2(lvl):#Selecciona solo una fila
    '''
    Lee todos los datos de la tabla, pero solo los del valor ingresado, de manera asc y con un limite de 3 valores.
    Retorna una lista con los datos dentro en tipo tupla.
    '''
    conn = sql.connect("Sqlite/ranking.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM puntaje WHERE nivel = ? ORDER BY puntos DESC LIMIT 3"
    cursor.execute(instruccion,(lvl,))
    datos = cursor.fetchall()#devolver todos los datos seleccionados
    conn.commit()
    conn.close()
    return datos

# print(readRows2("nivel_uno"))

def deleteRow(id_table):
    '''
    La función borra una fila de la tabla.
    Recibe por parametro el id a borrar. (Nota: es importante colocar el WHERE a la hora de hacer el delete, sino borra la tabla completa.)
    '''
    id = id_table
    with sql.connect("Sqlite/ranking.db") as conexion:
        sentencia = "DELETE FROM puntaje WHERE id=?"
        cursor=conexion.execute(sentencia,(id,))


#deleteRow(0)

def updateRow(id,puntos_player):
    '''
    La funcion reescribe la información ya almacenada en caso de querer hacer un cambio.
    Recibe por parametro el id al cual queremos modificar y el dato que vamos a modificar.
    Retorna una lista con la informacion en forma de tuplas.
    '''
    with sql.connect("Sqlite/ranking.db") as conexion:
        sentencia = "UPDATE puntaje SET puntos = ? WHERE id = ?"
        cursor=conexion.execute(sentencia,(puntos_player,id,))
        filas=cursor.fetchall()
        return filas