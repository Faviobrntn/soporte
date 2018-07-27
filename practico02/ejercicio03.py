import random

class Persona:
	def __init__(self, datos):
		self.nombre = datos["nombre"]
		self.edad 	= int(datos["edad"])
		self.sexo 	= datos["sexo"]
		self.peso 	= datos["peso"]
		self.altura = datos["altura"]
		self.dni 	= self.generar_dni()

	def es_mayor_edad(self):
		return (self.edad) >= 18

	def print_data(self):
		cadena = "\n Nombre:{0}\n Edad:{1}\n Sexo:{2}\n Peso:{3}\n Altura:{4}\n Dni:{5}\n".format(self.nombre, self.edad, self.sexo, self.peso, self.altura, self.dni)
		# print(cadena)
		return cadena

	def generar_dni(self):
		dni = random.randint(10000000, 99999999)
		return dni



if __name__ == '__main__':
	# dicc = { "nombre":"", "edad":"", "sexo":"", "peso":"", "altura":"" }
	# for key in dicc:
	# 	plus = " [M / F]" if (key=="sexo") else ""
	# 	dicc[key] = input("Ingrese "+key.replace("_", " ")+plus+": ")

	# persona = Persona(dicc)
	# persona.print_data()
	# print("¿Es mayor de edad? ", persona.es_mayor_edad())

	dicc = { "nombre":"Fulano", "edad":"25", "sexo":"Masculino", "peso":"70.5", "altura":"170" }
	persona = Persona(dicc)
	cadena = "\n Nombre:{0}\n Edad:{1}\n Sexo:{2}\n Peso:{3}\n Altura:{4}\n Dni:{5}\n".format(dicc["nombre"], int(dicc["edad"]), dicc["sexo"], dicc["peso"], dicc["altura"], persona.dni)

	print(persona.print_data())
	print("¿Es mayor de edad? ", persona.es_mayor_edad())
	assert( persona.print_data() == cadena)
	assert( persona.es_mayor_edad() == True)