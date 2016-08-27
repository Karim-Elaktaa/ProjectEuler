import math

targetNumber = 2000000 
tab = [True] * targetNumber

def markNotPrimeNumbers(t, x):
	for i in xrange(x + x, len(tab), x):
		t[i] = False	

for x in xrange(2, int(math.sqrt(len(tab))) + 1):
	if tab[x]: markNotPrimeNumbers(tab, x)

print sum(i for i in xrange(2, len(tab)) if tab[i])
