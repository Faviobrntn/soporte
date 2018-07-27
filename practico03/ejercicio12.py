'''
Ejercicio 12
	Con Alchemy usando SQLite  cree un modelo persona  con los campos del ejercicio 1 . 
	Hacer un programa que muestre la opción 1 Alta , 2 Listar ,  3 Baja . 
	La Opcion 1 Alta => ingresa una persona a la tabla . 
	La Opcion 2 Listar =>  muestra la el listado de las persona. 
	La Opcion 3 Baja => se ingresa idpersona para borrarla borra .
'''
from datetime import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



# Se indica motor a emplear, nombre del archivo y modo de mostrar resultados:

## Ejemplos con mysql
### engine = create_engine('mysql://scott:tiger@localhost/foo')  #Default
### engine = create_engine('mysql+pymysql://root:1234@localhost/soporte') # MySQL-python

## Ejemplo con SQLite
### engine = create_engine('sqlite://') #Para usar SQLite en memoria, especificar una dirección vacía:
### engine = create_engine('sqlite:///C:\\path\\to\\foo.db')  #Para PATH absoluto
### engine = create_engine('sqlite:///foo.db')  # Para PATH relativo


Base = declarative_base()

class Persona(Base):
	__tablename__ = 'persona' #--- indispensable.
	idpersona = Column(Integer, primary_key=True) #--- indispensable.
	nombre = Column(String)
	nacimiento = Column(Date)
	dni = Column(Integer)
	altura = Column(Integer)


engine = create_engine('sqlite:///')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def creaTabla():
 	# Crea todas las tablas definidas en los metadatos
 	Base.metadata.create_all(engine)



def listar():
 	personas = session.query(Persona).all() #--- lista
 	if(len(personas) == 0):
 		print("\n La tabla esta vacia.\n")
 	else:
	 	print('\nLista de personas:')
	 	print("=================================\n")
	 	for p in personas:
	 		print('Persona: ', p.nombre)
	 		print("ID: ", p.idpersona)
	 		print("Fecha de nacimiento: ", p.nacimiento)
	 		print("DNI: ", p.dni)
	 		print("Altura: ", p.altura)
	 		print("\n---------------------------------\n")


def alta(datos):
	try:
	 	pers = Persona()
	 	pers.nombre = datos['nombre']
	 	pers.nacimiento = datetime.strptime(datos['nacimiento'], '%d-%m-%Y')
	 	pers.dni = datos['dni']
	 	pers.altura = datos['altura']
	 	
	 	session.add(pers)
		
	 	session.commit()	
	except Exception as e:
		print("No se pudo dar de alta el registro: "+e)
		session.rollback()


def actualizar(idpersona, datos):
	try:
	 	pers = session.query(Persona).filter(Persona.idpersona == idpersona).first()
	 	# pers = Persona()
	 	pers.nombre = datos['nombre']
	 	pers.nacimiento = datetime.strptime(datos['nacimiento'], '%d-%m-%Y')
	 	pers.dni = datos['dni']
	 	pers.altura = datos['altura']
	 	
	 	session.add(pers)
		
	 	session.commit()	
	except Exception as e:
		print("No se pudo dar de alta el registro: "+e)
		session.rollback()


def baja(idpersona):
	try:
	 	sq = session.query(Persona).filter(Persona.idpersona == idpersona).first()
	 	session.delete(sq)
	 	session.commit()
	except Exception as e:
		session.rollback()




def menu():
	try:
		opc = ''
		datos = {'nombre':'', 'nacimiento':'', 'dni':0, 'altura':0}
		template_menu = '''\nSeleccione la opción que desee:
	1. Alta
	2. Listar
	3. Baja
	4. Actualizar
	0. Salir'''

		while opc != 0:
			print(template_menu)
			opc = int(input("Ingrese el numero deseado: "))

			if opc == 1:
				for key in datos:
					plus = " [dd-mm-YYYY]" if (key=="nacimiento") else ""
					datos[key] = input("Ingrese "+key+plus+": ")
				alta(datos)
			elif opc == 2:
				listar()
			elif opc == 3:
				clave = input("Ingrese el ID de la persona que desea dar de baja: ")
				baja(clave)
			elif opc == 4:
				clave = input("Ingrese el ID de la persona que desea actualizar: ")
				for key in datos:
					plus = " [dd-mm-YYYY]" if (key=="nacimiento") else ""
					datos[key] = input("Ingrese "+key+plus+": ")
				actualizar(key, datos)
			elif opc == 0:
				print("Hasta Pronto!! :-)")
			else:
				print(opc, " No es una opción correcta. Por favor, seleccione una opción correcta..")

	except Exception as e:
		print("Algo salió mal! ", e)

if __name__ == '__main__':

 	creaTabla()
 	menu()
 	# persona1 = {'nombre':'Juan Carlos', 'nacimiento':'03-12-1991', 'dni':37999012, 'altura':172}
 	# alta(persona1)
 	# persona2 = {'nombre':'Moni Argento', 'nacimiento':'17-02-1949', 'dni':11123456, 'altura':160}
 	# alta(persona2)
 	# listar()

 	# actualizar(1, persona2)
 	# listar()
 	# baja(1)
 	# listar()