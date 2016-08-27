#gcd : greatest common divisor
def gcd(n, m):
	t=0
	while m != 0:
		t = m
		m = n % m
		n = t
	return n

#lcm : least common multiple
def lcm(n, m):
	return n * m / gcd(n,m)

res = 1
for x in range(1, 21):
	res = lcm(res, x)

print res 
