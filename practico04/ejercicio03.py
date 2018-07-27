from tkinter import *
from tkinter import ttk, font
import debug

'''
	Crear un Formulario que usando el control Treeview muestre la una lista con los
	nombre de Ciudades Argentinas y su código postal (por lo menos 5 ciudades). 
'''

class Listado():
	def __init__(self):
		self.root = Tk()
		# self.root.geometry('500x200')
		self.root.title("Listado ejercicio 3")
		self.root.protocol("WM_DELETE_WINDOW", self.cerrar)
		self.listado()

		self.root.mainloop()


	def listado(self):
		# Fuente
		fuente = font.Font(weight='bold')

		# MARCOS GRAL
		frame = Frame(self.root, pady=20, borderwidth=0, relief="raised")
		frame.pack(side = TOP, fill=BOTH, expand=True)

		tree = ttk.Treeview(frame, columns=("one"))
		tree.heading("one", text="Cod. postal")

		grupo = tree.insert("" , 0, text="La Plata", values=(""))
		tree.insert("" , 0, text="Villa Gdor. Galvez", values=("2124"))
		tree.insert("" , 0, text="Villa Constitución", values=("2919"))
		tree.insert("" , 0, text="Rosario", values=("2000"))
		tree.insert("" , 0, text="Clorinda", values=("3610"))
		#Grupo de la plata
		tree.insert(grupo , 0, text="", values=("1900"))
		tree.insert(grupo , 0, text="", values=("1902"))
		tree.insert(grupo , 0, text="", values=("1904"))
		tree.insert(grupo , 0, text="", values=("1906"))
		tree.insert(grupo , 0, text="", values=("1912"))

		tree.pack(side = TOP, fill=BOTH, expand=True)


	def cerrar(self):
		self.root.destroy()
		self.root.quit()

if __name__ == '__main__':
	Listado()

