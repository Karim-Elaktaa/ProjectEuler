N = 10001 
totalPrime = 0
x = 2
while totalPrime < N:
	isPrime = True
	for i in range(2, x):
		if x % i == 0:
			isPrime = False
			break
	if isPrime:
		totalPrime += 1
		print "totalPrime ", totalPrime 
	print "For x = ", x, " isPrime = ", isPrime
	x = x + 1
