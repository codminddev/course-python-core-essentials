from sqlalchemy import create_engine

engine = create_engine("mysql://root:root@localhost:3306/palabras_db")

def insertar_dato(palabra , traduccion):
    conexion = engine.connect()
    sql = f"INSERT INTO diccionario (palabra, traduccion) VALUES ('{palabra}' , '{traduccion}')"
    conexion.execute(sql)

def buscar_palabra(palabra):
    conexion  = engine.connect()
    sql = f"SELECT traduccion FROM diccionario WHERE palabra = '{palabra}'"
    result_set = conexion.execute(sql)
    for row in result_set:
        return row["traduccion"]

def obtener_aleatorios():
    conexion = engine.connect()
    sql = "SELECT * FROM diccionario order by RAND() limit 5"
    result_set = conexion.execute(sql)
    #diccionario = [ {"palabra": row["palabra"] , "traduccion": row["traduccion"]} for row in result_set]
    diccionario = []
    for row in result_set:
        palabra = {"palabra": row["palabra"] , "traduccion": row["traduccion"]}
        diccionario.append(palabra)
        #return row["traduccion"]

    return diccionario

def eliminar_palabra_base(palabra):
    conexion = engine.connect()
    sql = f"DELETE FROM diccionario where palabra ='{palabra}'"
    conexion.execute(sql)
