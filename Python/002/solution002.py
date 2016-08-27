sum, curr, prev1, prev2 = 2, 0, 1, 2
targetMax = 4000000

while curr <= targetMax:
	curr = prev1 + prev2
	if curr % 2 == 0:
		sum += curr
	prev1 = prev2
	prev2 = curr

print sum
