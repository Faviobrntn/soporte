from Conexion import *

base=Conexion()
base.conectar()
cur=base.conn.cursor()
cur.execute("INSERT INTO persona (nombre,nacimiento,dni,altura) VALUES (%s,%s,%s,%s)",("ricardo","1993-05-03",38424487,1.25))
base.conn.commit()
base.conn.close()



