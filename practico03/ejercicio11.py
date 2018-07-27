def Divide(x,y):
    try:
        print( x/y )
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    except TypeError:
        print("No se pueden dividir cosas que no sean numeros")
    except Exception as f:
        print("No se pduo realizar la division"+str(f))

Divide(2,False)
