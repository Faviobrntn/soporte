def cantDigitos(a):
    c=0
    for numero in a:
        if (numero in '0123456789'):
            c+=1
    return(c)

assert( cantDigitos("hoy es 19 de abril") == 2 )