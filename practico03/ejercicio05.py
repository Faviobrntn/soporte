from Conexion import *

base=Conexion()
base.conectar()

cursor=base.conn.cursor()
cursor.execute("Update persona set nombre=%s where dni=%s",("rogelioo",38541538))
base.conn.commit()

cursor.execute("Select * from persona where dni=%s",(38541538))
for row in cursor.fetchone():
    print(row)
base.conn.commit()


cursor.close()
base.conn.close()

