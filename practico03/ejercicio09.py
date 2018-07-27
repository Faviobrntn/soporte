from Conexion import *

base=Conexion()
base.conectar()
cur=base.conn.cursor()

dni=input("ingrese el dni de la persona: ")

cur.execute("SELECT * FROM persona WHERE dni=%s",dni)
for row in cur.fetchone():
    print(row)

cur.execute("SELECT fecha,peso FROM persona INNER JOIN personapeso on persona.idpersona=personapeso.idpersona WHERE dni=%s;",dni)

for row in cur.fetchall():
    print(row)

