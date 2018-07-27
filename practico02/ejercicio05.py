import random
from datetime import datetime
from ejercicio04 import Estudiante

lista_estudiantes = []
def armar_lista():
	# cadena = "\n 1. Ingresar Estudiante\n 0. Salir\n"
	# print(cadena)
	# opc = int(input("Ingrese una opción: \t"))

	# while opc != 0:
	# 	dicc = { "nombre":"", "edad":"", "sexo":"", "peso":"", "altura":"", "carrera":"", "año_ingreso":"", "cant_materia":"", "aprobadas":"" }
	# 	for key in dicc:
	# 		plus = " [M / F]" if (key=="sexo") else ""
	# 		dicc[key] = input("Ingrese "+key.replace("_", " ")+plus+": ")

	# 	persona = Estudiante(dicc)
	# 	lista_estudiantes.append(persona)

	# 	print(cadena)
	# 	opc = int(input("Ingrese una opción: \t"))
	dicc1 = { "nombre":"Fulano", "edad":"25", "sexo":"Masculino", "peso":"70.5", "altura":"170", "carrera":"ISI", "año_ingreso":"2012", "cant_materia":"35", "aprobadas":"15" }
	dicc2 = { "nombre":"Fulana", "edad":"20", "sexo":"Femenino", "peso":"70.5", "altura":"170", "carrera":"IQ", "año_ingreso":"2012", "cant_materia":"37", "aprobadas":"10" }
	dicc3 = { "nombre":"Mengano", "edad":"19", "sexo":"Masculino", "peso":"70.5", "altura":"170", "carrera":"ISI", "año_ingreso":"2012", "cant_materia":"35", "aprobadas":"5" }
	persona = Estudiante(dicc1)
	lista_estudiantes.append(persona)
	persona = Estudiante(dicc2)
	lista_estudiantes.append(persona)
	persona = Estudiante(dicc3)
	lista_estudiantes.append(persona)

def armar_diccionario(lista):
	dicc = {}
	for obj in lista:
		if obj.carrera in dicc:
			dicc[obj.carrera] += 1
		else:
			dicc[obj.carrera] = 1
	return dicc


armar_lista()
dicc_carreras = armar_diccionario(lista_estudiantes)
for k, v in dicc_carreras.items():
	print(k, ": ", v)


assert( dicc_carreras == {'ISI': 2, 'IQ': 1})