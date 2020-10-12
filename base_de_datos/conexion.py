print("Iniciando la conexión")

from sqlalchemy import create_engine

engine = create_engine("mysql://root:root@localhost:3306/palabras_db")
connection = engine.connect()

result = connection.execute("SELECT palabra, traduccion FROM diccionario")
print(type(result))

for row in result:
    print( row , type(row))
    print("palabra: ", row["palabra"] , " traduccion:", row["traduccion"])

connection.execute("INSERT INTO diccionario (palabra, traduccion) VALUES ('perro', 'dog')")