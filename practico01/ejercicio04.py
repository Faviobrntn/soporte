def esVocal(a):
    return(a[:1].lower() in 'aeiou')

assert (esVocal("hola") == False)
assert (esVocal("COMO") == False)
assert (esVocal("AndAs") == True)
assert (esVocal("abecedario") == True)
assert (esVocal("o") == True)
assert (esVocal("b") == False)
