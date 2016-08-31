MAX = 28124
data = [0] * MAX
#getting proper divisors for each number from 1 to MAX
for x in range(1, MAX):
	for y in range(x * 2, MAX, x):
		data[y] += x

#filtering abundant numbers
abundantNumbers = set([x for x in range(2, MAX) if x < data[x]])

#summing each couple of abundant numbers
sumOfTwoAbundantNumbers= set([])
for x in abundantNumbers:
	for y in abundantNumbers:
		if x + y > MAX:
			break
		else:
			sumOfTwoAbundantNumbers.add(x+y)

print sum(set(range(MAX)) - sumOfTwoAbundantNumbers)
