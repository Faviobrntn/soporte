import math
class Circulo:
	"""docstring for Circulo"""


	def __init__(self, radio):
		self.radio = radio

	def area(self):
		return self.radio **2 * math.pi

	def perimetro(self):
		return 2 * math.pi * self.radio


# radio = float(input("Ingrese el radio del circulo: "))
# circulo = Circulo(radio)
# print("El area del círculo es: ", (circulo.area()))
# print("El perimetro del círculo es: ", (circulo.perimetro()))

assert( (Circulo(2)).area() == math.pi*4)
assert( (Circulo(2)).perimetro() == math.pi*4)