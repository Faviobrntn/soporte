from Conexion import *
import json

base=Conexion()
base.conectar()
cursor=base.conn.cursor()

cursor.execute("SELECT * FROM persona")
array = []
for row in cursor.fetchall():
    #print(row[0],row[1],row[2],row[3],row[4])
	data = {}
	data['id'] = row[0]
	data['nombre'] = row[1]
	data['nacimiento'] = str(row[2])
	data['dni'] = row[3]
	data['altura'] = row[4]
	array.append(data)

elJson = json.dumps(array)
print(elJson)

cursor.close()
base.conn.close()
