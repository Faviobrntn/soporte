class Rectangulo():
	"""docstring for Rectangulo"""
	def __init__(self, base, altura):
		self.base = base
		self.altura = altura
	
	def area(self):
		return self.base * self.altura

# base = int(input("Ingrese la base del rectangulo: "))
# alt  = int(input("Ingrese la altura del rectangulo: "))

# rectangulo = Rectangulo(base, alt)
# print("El area del rectangulo es: ", (rectangulo.area()))

assert( (Rectangulo(2, 4)).area() == 8)