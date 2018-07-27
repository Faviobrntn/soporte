from Conexion import *

base=Conexion()
base.conectar()

cursor=base.conn.cursor()

cursor.execute("Select * from persona where dni=%s",(38541538))
for row in cursor.fetchone():
    print(row)

#otra forma
#print(cursor.fetchall())

base.conn.commit()

cursor.close()

base.conn.close()
