def esPrimo(c):
    for i in range(2,c):
        if c%i==0:
            return False
    return True

assert( esPrimo(3) == True )
assert( esPrimo(21) == False )
