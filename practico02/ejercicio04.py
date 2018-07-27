import random
from datetime import datetime
from ejercicio03 import Persona

class Estudiante(Persona):
	"""
		Atributos de la clase Estudiante
		* carrera;
		* año_ingreso;
		* cant_materia;
		* aprobadas;
	"""
	def __init__(self, datos):
		Persona.__init__(self, datos)
		#super(Estudiante, self).__init__()
		self.carrera 		= datos["carrera"]
		self.año_ingreso 	= int(datos["año_ingreso"])
		self.cant_materia 	= int(datos["cant_materia"])
		self.aprobadas 		= int(datos["aprobadas"])

	def avance(self):
		return round((self.aprobadas*100)/self.cant_materia, 2)

	def edad_ingreso(self):
		if(self.es_mayor_edad()):
			#datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			año_actual = int(datetime.now().strftime('%Y'))
			return self.edad - (año_actual - self.año_ingreso)
		else:
			return "Todavía no esta en la universidad, pues no es mayor de edad"



if __name__ == '__main__':
	# dicc = { "nombre":"", "edad":"", "sexo":"", "peso":"", "altura":"", "carrera":"", "año_ingreso":"", "cant_materia":"", "aprobadas":"" }
	# for key in dicc:
	# 	plus = " [M / F]" if (key=="sexo") else ""
	# 	dicc[key] = input("Ingrese "+key.replace("_", " ")+plus+": ")

	# persona = Estudiante(dicc)
	# persona.print_data()
	# print("Porcentaje de avance en la carrera: ", persona.avance())
	# print("Edad de ingreso: ", persona.edad_ingreso())

	dicc = { "nombre":"Fulano", "edad":"25", "sexo":"Masculino", "peso":"70.5", "altura":"170", "carrera":"ISI", "año_ingreso":"2012", "cant_materia":"30", "aprobadas":"10" }
	persona = Estudiante(dicc)
	cadena = "\n Nombre:{0}\n Edad:{1}\n Sexo:{2}\n Peso:{3}\n Altura:{4}\n Dni:{5}\n".format(dicc["nombre"], int(dicc["edad"]), dicc["sexo"], dicc["peso"], dicc["altura"], persona.dni)

	print(persona.print_data())
	print("Porcentaje de avance en la carrera: ", persona.avance())
	print("Edad de ingreso: ", persona.edad_ingreso())

	assert( persona.print_data() == cadena)
	assert( persona.avance() == 33.33)
	assert( persona.edad_ingreso() == 19)
