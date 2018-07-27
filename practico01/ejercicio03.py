def calclong(s):
	contador = 0
	for x in s:
		contador += 1;
	return contador

assert (calclong("asdfghlo") == 8)
assert (calclong([0,2,5,4]) == 4)