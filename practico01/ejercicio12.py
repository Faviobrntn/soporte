def sumaN(n):
    total=0
    for num in range(1,n+1):
        total=total+num
    print(total)
    return(total)

assert (sumaN(5) == 15)
