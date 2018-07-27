from Conexion import *

base=Conexion()
base.conectar()
cursor=base.conn.cursor()
cursor.execute("Delete from persona where idpersona=%s",(3))

base.conn.commit()
cursor.close()
base.conn.close()
