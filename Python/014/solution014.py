memory = {1:1}

def compute(n):
	if n in memory.keys():
		return memory[n]
	elif n % 2 == 0: #even
		return compute(n/2) + 1
	else: #odd
		return compute(3 * n + 1) + 1

maxStartWith = 0
maxCount = 0
for x in range(2, 1000000):
	if compute(x) > maxCount:
		maxCount = compute(x)
		maxStartWith = x
print maxCount
print maxStartWith
