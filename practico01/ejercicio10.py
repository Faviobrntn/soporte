def masLarga(b):
    palLarga=''
    for palabra in b:
        if len(palabra)>len(palLarga):
            palLarga=palabra
    return(palLarga)

a=["hola","cabaña","oso","dinosaurio"]
assert( masLarga(a) == "dinosaurio")