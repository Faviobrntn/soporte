from Conexion import *

base=Conexion()
base.conectar()
cur=base.conn.cursor()

'''Crear una tabla Persona con los datos de 
	IdPersona Int(), Nombre Char(30) , FechaNacimiento Date() , DNI Numeric(13) , Altura Int() . '''

cur.execute("""CREATE TABLE IF NOT EXISTS persona(
		idpersona INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
		nombre VARCHAR(30),
		nacimiento DATE,
		dni INT(13),
		altura INT(5)
	)"""
)

cur.execute("SELECT * FROM persona")
for idpersona, nombre, nacimiento, dni, altura in cur.fetchall():
    print(idpersona,nombre,nacimiento,dni,altura)

base.conn.close()
