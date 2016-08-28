import math

def nbFactors(n):
	s = [i for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0]
	s += [n/i for i in s if i > 1]
	return len(s)

found = False
acc = 0
it = 1 
while not(found):
	acc += it
	if nbFactors(acc) >= 500:
		found = True
	it += 1
print acc 
