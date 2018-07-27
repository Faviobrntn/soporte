from tkinter import *
from tkinter import ttk, font
import debug

'''
	Hacer un formulario tkinter que es una calculadora, 
		* tiene 2 entry para ingresar losvalores V1 y V2. Y 
		* 4 botones de operaciones para las operaciones respectivas + , - , * , /.
		* Al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 . 
'''

class Calculadora():
	def __init__(self):
		self.root = Tk()
		# self.root.geometry('500x200')
		self.root.title("Calculadora ejercicio 1")
		self.root.protocol("WM_DELETE_WINDOW", self.cerrar)
		self.formulario()
		# btn = Button(self.root, text="Apretame", command=ventana1)

		# debug.getPropiedades(label)
		self.root.mainloop()


	def formulario(self):
		# Fuente
		fuente = font.Font(weight='bold')
		self.resultado = StringVar()
		#RESULTADOS
		frame_res = Frame(self.root, borderwidth=2, relief="raised")
		frame_res.pack(side = TOP, fill=BOTH, expand=True)
		label = Label(frame_res, text="RESULTADO: ", font=fuente)
		ver_resu = Entry(frame_res, textvariable=self.resultado)
		label.pack(side=LEFT)
		ver_resu.pack(side = LEFT, fill=BOTH, expand=True)

		# MARCOS GRAL
		frame = Frame(self.root, pady=20, borderwidth=2, relief="raised")
		frame.pack(side = TOP, fill=BOTH, expand=True)
		## MARCO DE FORMULARIO
		frame1 = Frame(frame, padx=20, pady=20)
		frame1.pack(side = LEFT, fill=BOTH, expand=True)
		frame2 = Frame(frame, padx=20, pady=20)
		frame2.pack(side = LEFT, fill=BOTH, expand=True)
		#MARCO DE BOTONES
		btnFrame = Frame(self.root, pady=10)
		btnFrame.pack( side = BOTTOM, fill=BOTH, expand=True )

		#Etiquetas
		label1 = Label(frame1, text="Primer operando", font=fuente)
		label2 = Label(frame2, text="Segundo operando", font=fuente)
		
		#Inputs
		self.op1 = DoubleVar()
		self.op1.set('')
		self.op2 = DoubleVar()
		self.op2.set('')
		entrada1 = Entry(frame1, textvariable=self.op1)
		entrada2 = Entry(frame2, textvariable=self.op2)

		#Botones
		btn_suma = Button(btnFrame, text=" + ", width=9, command=self.sumar)
		btn_resta = Button(btnFrame, text=" - ", width=9, command=self.restar)
		btn_prod = Button(btnFrame, text=" * ", width=9, command=self.multiplicar)
		btn_div = Button(btnFrame, text=" / ", width=9, command=self.dividir)


		# Gestor PACK
		label1.pack(side=TOP, fill=BOTH, expand=True)
		entrada1.pack(side=TOP)
		label2.pack(side=TOP, fill=BOTH, expand=True)
		entrada2.pack(side=TOP)

		btn_suma.pack(side=LEFT)
		btn_resta.pack(side=LEFT)
		btn_prod.pack(side=LEFT)
		btn_div.pack(side=LEFT)

	def sumar(self):
		res = self.op1.get() + self.op2.get()
		self.resultado.set(res)
		self.op1.set('')
		self.op2.set('')
		pass
	def restar(self):
		res = self.op1.get() - self.op2.get()
		self.resultado.set(res)
		self.op1.set('')
		self.op2.set('')
		pass
	def multiplicar(self):
		res = self.op1.get() * self.op2.get()
		self.resultado.set(res)
		self.op1.set('')
		self.op2.set('')
		pass
	def dividir(self):
		try:
			res = self.op1.get() / self.op2.get()
			self.resultado.set(res)
			self.op1.set('')
			self.op2.set('')
		except ZeroDivisionError as e:
			self.resultado.set("ERROR: División por cero.")
			print("Esta dividiendo por 0")

	def cerrar(self):
		self.root.destroy()
		self.root.quit()

if __name__ == '__main__':
	Calculadora()

