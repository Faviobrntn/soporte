from Conexion import *

base=Conexion()
base.conectar()

cur=base.conn.cursor()

'''Crear un tabla relacionada con Persona para guardar su peso corporal en una fecha.
	PersonaPeso IdPersona Int() , Fecha Date() , Peso Int. '''

cur.execute("""CREATE TABLE IF NOT EXISTS personapeso(
		id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
		idpersona INTEGER NOT NULL,
		fecha DATE, 
		peso INT(10),
		FOREIGN KEY (idpersona) REFERENCES persona(idpersona)
	)""")

base.conn.close()