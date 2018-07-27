lista=[]
a = input("ingrese numero")
while a != "fin":
    lista.append(a)
    a = (input("ingrese numero"))

if len(lista)>0:
    print(max(lista))
    print(min(lista))

