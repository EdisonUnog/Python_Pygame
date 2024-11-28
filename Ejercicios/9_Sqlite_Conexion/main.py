import sqlite3

with sqlite3.connect("mi_base_de_datos.db") as conexion:
    try:
        #_crear una tablas
        sentencia = '''
                    create tabla empleados
                    (
                        id integer primary key autoincrement
                        nombre text
                        pellido text
                        sueldo real
                    )
                    '''

        #sentencia = '''
        #            insert into empleados(nombre, apellido, sueldo, direccion) values("Pepe","Argento", 5000, "Mitre 750")
        #            '''
        

        conexion.execute(sentencia)
        print("tabla creada con exito")

    except:
        print("error")


