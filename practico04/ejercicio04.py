from tkinter import *
from tkinter import ttk, font
import debug

'''
	Crear un Formulario que usando el control Treeview muestre la una lista con los
	nombre de Ciudades Argentinas y su código postal (por lo menos 5 ciudades). 
'''

class ABM():
	def __init__(self):
		self.root = Tk()
		# self.root.geometry('500x200')
		self.root.title("ABM ejercicio 4")
		self.root.protocol("WM_DELETE_WINDOW", self.cerrar)
		# Fuente
		self.fuente = font.Font(weight='bold', size=15)
		self.listado()
		self.item_id = ""
		self.ciudad = StringVar()
		self.postal = StringVar()
		self.root.mainloop()


	def listado(self):
		# MARCOS GRAL
		frame = Frame(self.root, pady=20, borderwidth=0, relief="raised")
		frame.pack(side = TOP, fill=BOTH, expand=True)

		self.tree = ttk.Treeview(frame, columns=("one"))
		self.tree.heading("one", text="Cod. postal")

		btn_add = Button(frame, text="Agregar", height=2, command=self.abrirModal)
		btn_edit = Button(frame, text="Editar", height=2, command=self.editar)
		btn_delete = Button(frame, text="Eliminar", height=2, command=self.eliminar)

		self.tree.pack(side = TOP, fill=BOTH, expand=True)
		btn_add.pack(side = LEFT, fill=BOTH, expand=True)
		btn_edit.pack(side = LEFT, fill=BOTH, expand=True)
		btn_delete.pack(side = LEFT, fill=BOTH, expand=True)


	def agregar(self):
		if(self.item_id != ""):
			self.tree.item(self.item_id, text=self.ciudad.get(), values=(self.postal.get()))
		else:
			self.tree.insert("", 0, text=self.ciudad.get(), values=(self.postal.get()))
		self.cancelar()
		


	def editar(self):
		self.item_id = self.tree.focus()
		if(self.item_id != ''):
			item = self.tree.item(self.item_id)
			self.ciudad.set(item['text'])
			self.postal.set(item['values'][0])
			self.abrirModal()


	def eliminar(self):
		try:
			seleccionado = self.tree.selection()[0]
			self.tree.delete(seleccionado)
		except Exception as e:
			print("Debe seleccionar un item")


	def abrirModal(self):
		self.modal = Toplevel(self.root)
		self.modal.title("Nueva Ciudad")
		self.modal.geometry('500x200')
		self.modal.resizable(0,0)
		## MARCO DE FORMULARIO
		frame1 = Frame(self.modal, pady=10)
		frame1.pack(side = TOP, fill=BOTH, expand=True)
		frame2 = Frame(self.modal, pady=10)
		frame2.pack(side = TOP, fill=BOTH, expand=True)
		#MARCO DE BOTONES
		btnFrame = Frame(self.modal)
		btnFrame.pack( side = TOP, fill=BOTH, expand=True )

		#Etiquetas
		label1 = Label(frame1, text="Ciudad", font=self.fuente, width=5)
		label2 = Label(frame2, text="Cod. postal", font=self.fuente, width=5)
		#Inputs
		entrada1 = Entry(frame1, textvariable=self.ciudad, width=20, font=self.fuente)
		entrada2 = Entry(frame2, textvariable=self.postal, width=20, font=self.fuente)

		#Botones
		btn_aceptar = Button(btnFrame, text="Guardar", height=2, width=10, command=self.agregar)
		btn_cancelar = Button(btnFrame, text="Cancelar", height=2, width=10, command=self.cancelar)

		# Gestor PACK
		label1.pack(side=LEFT, fill=BOTH, expand=True)
		entrada1.pack(side=LEFT, fill=BOTH, expand=True)
		label2.pack(side=LEFT, fill=BOTH, expand=True)
		entrada2.pack(side=LEFT, fill=BOTH, expand=True)
		btn_aceptar.pack(side=RIGHT)
		btn_cancelar.pack(side=RIGHT)

	def cancelar(self):
		self.item_id = ""
		self.ciudad.set("")
		self.postal.set("")
		self.modal.destroy()

	def cerrar(self):
		self.root.destroy()
		self.root.quit()

if __name__ == '__main__':
	ABM()

