def multList(a):
    res=1
    for num in a:
        res=res*num
    return(res)

assert (multList([2, 2, "a"]) == "aaaa")
assert (multList([2, 2, 1]) == 4)
assert (multList([2, 2, -5]) == -20)
assert (multList([-1, -8]) == 8)
assert (multList([-2, -1, -3]) == -6)
assert (multList([2, 2, 0]) == 0)
