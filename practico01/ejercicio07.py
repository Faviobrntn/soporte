def esPalindromo(a):
    return(a==a[::-1])

assert ( esPalindromo("neuquen") == True)
assert ( esPalindromo("hola") == False)