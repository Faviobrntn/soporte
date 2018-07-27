from datetime import *
from Conexion import *

base=Conexion()
base.conectar()
cur=base.conn.cursor()


perId=input("Ingrese el id de la persona: ")
f='%Y-%m-%d'
fecha=datetime.strptime((input("Ingrese la fecha ('YYYY-mm-dd'): ")),f)
peso=input("Ingrese el peso: ")
bandera=False

cur.execute("SELECT * FROM persona WHERE idpersona=%s",perId)

if len(cur.fetchall())!=0:
    cur.execute("SELECT * FROM personapeso WHERE idpersona=%s",perId)
    for row in cur.fetchall():
        if(datetime.strptime(str(row[1]),f)>fecha):
            bandera=True

if bandera==False:
    cur.execute("INSERT INTO personapeso (idpersona, fecha, peso) VALUES (%s,%s,%s)",(perId,fecha,peso))
    print("Agregado a la bd")
    base.conn.commit()

base.conn.close()
