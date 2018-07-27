from tkinter import *
from tkinter import ttk, font
import debug

'''
	Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones
		para los dígitos 0 al 9 y las operaciones + - / * = , que al apretar cada botón vaya agregando al
		valor que muestra en el entry el carácter que le corresponde ( como se ve imagen ) y cuando
		se aprieta en = pone el resultado de evaluar la cadena entrada .
'''

class Calculadora():
	def __init__(self):
		self.root = Tk()
		self.root.geometry('400x400')
		self.root.resizable(0,0)
		self.root.title("Calculadora ej2")
		self.root.protocol("WM_DELETE_WINDOW", self.cerrar)
		# Fuente
		self.fuente = font.Font(weight='bold', size=20)
		self.visor()
		self.botonera()

		self.root.mainloop()


	def visor(self):
		# MARCOS GRAL
		frame = Frame(self.root, borderwidth=2, relief="raised")
		frame.pack(side = TOP, fill=BOTH, expand=True)
		#Inputs
		self.entrada = StringVar()
		self.entrada.set('')
		entrada = Entry(frame, textvariable=self.entrada, font=self.fuente, state='disabled')
		entrada.bind('<Button-1>', self.reiniciar)
		# Gestor PACK
		entrada.pack(side=TOP, fill=BOTH, expand=True)

	def botonera(self):
		# MARCOS GRAL
		frame = Frame(self.root, borderwidth=0, relief="raised")
		frame.pack(side = TOP, fill=BOTH, expand=True)
		fila1 = Frame(frame, borderwidth=0, relief="raised")
		fila1.pack(side = TOP, fill=BOTH, expand=True)
		fila2 = Frame(frame, borderwidth=0, relief="raised")
		fila2.pack(side = TOP, fill=BOTH, expand=True)
		fila3 = Frame(frame, borderwidth=0, relief="raised")
		fila3.pack(side = TOP, fill=BOTH, expand=True)
		fila4 = Frame(frame, borderwidth=0, relief="raised")
		fila4.pack(side = TOP, fill=BOTH, expand=True)
		
		#Botones
		btn_suma = Button(fila1, text="+", width=6, command= lambda: self.insertar("+"))
		btn_resta = Button(fila2, text="-", width=6, command= lambda: self.insertar("-"))
		btn_div = Button(fila3, text="/", width=6, command= lambda: self.insertar("/"))
		btn_prod = Button(fila4, text="*", width=6, command= lambda: self.insertar("*"))
		btn_igual = Button(fila4, text="=", width=18, bg='lightgray', command=self.calcular)

		btn_0 = Button(fila4, text="0", width=6, command= lambda: self.insertar("0"))
		btn_1 = Button(fila3, text="1", width=6, command= lambda: self.insertar("1"))
		btn_2 = Button(fila3, text="2", width=6, command= lambda: self.insertar("2"))
		btn_3 = Button(fila3, text="3", width=6, command= lambda: self.insertar("3"))
		btn_4 = Button(fila2, text="4", width=6, command= lambda: self.insertar("4"))
		btn_5 = Button(fila2, text="5", width=6, command= lambda: self.insertar("5"))
		btn_6 = Button(fila2, text="6", width=6, command= lambda: self.insertar("6"))
		btn_7 = Button(fila1, text="7", width=6, command= lambda: self.insertar("7"))
		btn_8 = Button(fila1, text="8", width=6, command= lambda: self.insertar("8"))
		btn_9 = Button(fila1, text="9", width=6, command= lambda: self.insertar("9"))

		# Gestor PACK
		btn_suma.pack(side=LEFT, fill=BOTH, expand=True)
		btn_resta.pack(side=LEFT, fill=BOTH, expand=True)
		btn_prod.pack(side=LEFT, fill=BOTH, expand=True)
		btn_div.pack(side=LEFT, fill=BOTH, expand=True)
		btn_0.pack(side=LEFT, fill=BOTH, expand=True)
		btn_1.pack(side=LEFT, fill=BOTH, expand=True)
		btn_2.pack(side=LEFT, fill=BOTH, expand=True)
		btn_3.pack(side=LEFT, fill=BOTH, expand=True)
		btn_4.pack(side=LEFT, fill=BOTH, expand=True)
		btn_5.pack(side=LEFT, fill=BOTH, expand=True)
		btn_6.pack(side=LEFT, fill=BOTH, expand=True)
		btn_7.pack(side=LEFT, fill=BOTH, expand=True)
		btn_8.pack(side=LEFT, fill=BOTH, expand=True)
		btn_9.pack(side=LEFT, fill=BOTH, expand=True)
		btn_igual.pack(side=LEFT, fill=BOTH, expand=True)
		# debug.getPropiedades(btn_9)

	def reiniciar(self, *args):
		self.entrada.set('')


	def insertar(self, caracter):
		# print(caracter)
		cadena = self.entrada.get()
		cadena = cadena+caracter
		self.entrada.set(cadena)

	def calcular(self):
		try:
			entrada = self.entrada.get()
			self.entrada.set(eval(entrada))
		except ZeroDivisionError as e:
			self.entrada.set("Error: División por cero.")
		except Exception as e:
			self.entrada.set("Error")

	def cerrar(self):
		self.root.destroy()
		self.root.quit()

if __name__ == '__main__':
	Calculadora()

