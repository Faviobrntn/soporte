#!/usr/bin/env python3
import sys
sys.path += ['..']
from tkinter import *
from tkinter import ttk, font, messagebox
from practico05.base import Socio
from practico06.ejercicio01 import NegocioSocio

'''
	Crear en Python usando Tkinter un formulario para gestionar los datos de Socios usando la
	Capa de Negocio de Socios. El Formulario principal tiene que mostrar todos los socios y tener
	botones para realizar Alta, Baja , Modificar 
'''

class Interfaz():
	def __init__(self):
		self.root = Tk()
		# self.root.geometry('500x200')
		self.root.title("ABM Socios")
		self.root.protocol("WM_DELETE_WINDOW", self.cerrar)

		self.capaNegocio = NegocioSocio()

		# Fuente
		self.fuente = font.Font(weight='bold', size=15)
		self.listado()
		self.item_id = ""
		self.id_socio = IntVar()
		self.nombre = StringVar()
		self.apellido = StringVar()
		self.dni = IntVar()
		self.root.mainloop()


	def listado(self):
		# MARCOS GRAL
		frame = Frame(self.root, pady=20, borderwidth=0, relief="raised")
		frame.pack(side = TOP, fill=BOTH, expand=True)

		self.tree = ttk.Treeview(frame, columns=("uno", "dos", "tres"))
		self.tree.heading("#0", text="ID")
		self.tree.heading("uno", text="Nombre")
		self.tree.heading("dos", text="Apellido")
		self.tree.heading("tres", text="DNI")

		btn_add = Button(frame, text="Agregar", height=2, command=self.abrirModal)
		btn_edit = Button(frame, text="Editar", height=2, command=self.editar)
		btn_delete = Button(frame, text="Eliminar", height=2, command=self.eliminar)

		self.tree.pack(side = TOP, fill=BOTH, expand=True)
		btn_add.pack(side = LEFT, fill=BOTH, expand=True)
		btn_edit.pack(side = LEFT, fill=BOTH, expand=True)
		btn_delete.pack(side = LEFT, fill=BOTH, expand=True)
		self.actualizar()


	def actualizar(self):
		self.tree.delete(*self.tree.get_children())
		socios = self.capaNegocio.todos()
		for i in socios:
			self.tree.insert("", i.id_socio, text=i.id_socio, values=(i.nombre, i.apellido, i.dni))



	def guardar(self):
		try:
			if(self.item_id != ""): #Modificar
				socio = self.capaNegocio.buscar(self.id_socio.get())
				socio.nombre = self.nombre.get()
				socio.apellido = self.apellido.get()
				socio.dni = self.dni.get()
				if(self.capaNegocio.modificacion(socio)):
					messagebox.showinfo("Información","Los cambios se guardaron con éxito.")
					self.actualizar()
				else:
					messagebox.showerror("Error","No se pudo guardar.")
				# self.tree.item(self.item_id, text=self.id_socio.get(), values=(self.nombre.get(), self.apellido.get(), self.dni.get()))
			else: #Guardar nuevo
				socio = Socio()
				socio.nombre = self.nombre.get()
				socio.apellido = self.apellido.get()
				socio.dni = self.dni.get()
				if(self.capaNegocio.alta(socio)):
					messagebox.showinfo("Información","Se agrego con éxito.")
					self.actualizar()
				else:
					messagebox.showerror("Error","No se pudo guardar.")
				# self.tree.insert("", 0, text=self.id_socio.get(), values=(self.nombre.get(), self.apellido.get(), self.dni.get()))
		except Exception as e:
			print(str(e))
			messagebox.showerror("Error", str(e))
		else:
			pass #Se ejecuta si no se disparo excepción
		finally: 
			#Se ejecuta siempre
			self.cancelar()
		


	def editar(self):
		try:
			self.item_id = self.tree.focus()
			if(len(self.item_id)!=0):
				item = self.tree.item(self.item_id)
				socio = self.capaNegocio.buscar(item['text'])
				if(socio):
					self.id_socio.set(socio.id_socio)
					self.nombre.set(socio.nombre)
					self.apellido.set(socio.apellido)
					self.dni.set(socio.dni)
				else:
					raise Exception("No se encontro el socio.")
			else:
				raise Exception("Debe seleccionar un socio.")
		except Exception as e:
			print(str(e))
			messagebox.showerror("Error", str(e))
		else:
			self.abrirModal()


	def eliminar(self):
		try:
			seleccionado = self.tree.selection()[0]
			c = messagebox.askyesno("Eliminar","¿Estas seguro de querer eliminar el registro?")
			if c is not False:
				self.item_id = self.tree.focus()
				if(self.item_id != ''):
					item = self.tree.item(self.item_id)
					if(self.capaNegocio.baja(item['text'])):
						self.tree.delete(seleccionado)
						messagebox.showinfo("Información", "Se eliminó con éxito el socio ID: "+str(item['text']))
					else:
						messagebox.showerror("Error", "No se pudo eliminar el socio con ID: "+str(item['text']))
		except Exception as e:
			print("Algo esta mal! "+str(e))
			messagebox.showerror("Error", "Debe seleccionar un socio.")


	def abrirModal(self):
		self.modal = Toplevel(self.root)
		self.modal.title("Nuevo Socio")
		self.modal.geometry('500x200')
		self.modal.resizable(0,0)
		## MARCO DE FORMULARIO
		frame1 = Frame(self.modal, pady=10)
		frame1.pack(side = TOP, fill=BOTH, expand=True)
		frame2 = Frame(self.modal, pady=10)
		frame2.pack(side = TOP, fill=BOTH, expand=True)
		frame3 = Frame(self.modal, pady=10)
		frame3.pack(side = TOP, fill=BOTH, expand=True)
		
		#MARCO DE BOTONES
		btnFrame = Frame(self.modal)
		btnFrame.pack( side = TOP, fill=BOTH, expand=True )

		#Etiquetas
		label1 = Label(frame1, text="Nombre", font=self.fuente, width=5)
		label2 = Label(frame2, text="Apellido", font=self.fuente, width=5)
		label3 = Label(frame3, text="DNI", font=self.fuente, width=5)
		#Inputs
		entrada1 = Entry(frame1, textvariable=self.nombre, width=20, font=self.fuente)
		entrada2 = Entry(frame2, textvariable=self.apellido, width=20, font=self.fuente)
		entrada3 = Entry(frame3, textvariable=self.dni, width=20, font=self.fuente)

		#Botones
		btn_aceptar = Button(btnFrame, text="Guardar", height=2, width=10, command=self.guardar)
		btn_cancelar = Button(btnFrame, text="Cancelar", height=2, width=10, command=self.cancelar)

		# Gestor PACK
		label1.pack(side=LEFT, fill=BOTH, expand=True)
		entrada1.pack(side=LEFT, fill=BOTH, expand=True)
		label2.pack(side=LEFT, fill=BOTH, expand=True)
		entrada2.pack(side=LEFT, fill=BOTH, expand=True)
		label3.pack(side=LEFT, fill=BOTH, expand=True)
		entrada3.pack(side=LEFT, fill=BOTH, expand=True)
		btn_aceptar.pack(side=RIGHT)
		btn_cancelar.pack(side=RIGHT)

	def cancelar(self):
		self.item_id = ""
		self.id_socio.set(0)
		self.nombre.set("")
		self.apellido.set("")
		self.dni.set(0)
		self.modal.destroy()

	def cerrar(self):
		self.root.destroy()
		self.root.quit()

if __name__ == '__main__':
	Interfaz()

