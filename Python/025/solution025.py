fibo = [1,1]
i = 1
finished = False
while not(finished):
	i += 1
	fibo.append(fibo[i-2] + fibo[i-1])
	if len(str(fibo[i])) == 1000:
		finished = True
print i + 1 # +1 because i fibo starts at 0
