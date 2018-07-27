from tkinter import *

def getPropiedades(element):
	prop = element.config()
	for x in prop:
		print(x)