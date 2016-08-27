def sumOfTheSquares(x):
	res = 0
	for i in range(0, x + 1):
		res += i * i
	return res

def squareOfTheSum(x):
	res = 0	
	for i in range(0, x + 1):
		res += i
	return res * res	

print squareOfTheSum(100) - sumOfTheSquares(100)
