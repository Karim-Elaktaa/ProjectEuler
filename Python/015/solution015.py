def facto(n):
	if n == 1:
		return n
	else:
		return facto(n - 1) * n

print facto(40)/(facto(20)**2) #combinaison 40 choose 20
