def superposicion(a,b):
    for letter1 in a:
        for letter2 in b:
            if letter1==letter2:
                return True
    return False

assert ( superposicion("uiooo i", "cadena 2") == True)
assert ( superposicion("uioooi", "cadena2") == False)
