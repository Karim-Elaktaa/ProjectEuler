num, den, acc = 3, 2, 0
for iter in xrange(0, 1000):
	num, den = num + den + den, num + den
	if len(str(num)) > len(str(den)):
		acc += 1
print acc
