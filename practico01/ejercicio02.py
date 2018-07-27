def max(a,b,c):
    if (a>=b and a>=c):
        return(a)
    elif (b>=a and b>=c):
        return(b)
    elif (c>=a and c>=b):
        return(c)

assert (max(2, 5, 0) == 5)
assert (max(2, 5.9, 0.2) == 5.9)
assert (max(0, -3, 1) == 1)

# num1=int(input("numero 1"))
# num2=int(input("numero 2"))
# num3=int(input("numero 3"))
# max(num1,num2, num3)

