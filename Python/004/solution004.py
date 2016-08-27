def isPanlindrome(x):
	s1 = str(x)
	s2 = s1[::-1]
	for i in range (0, len(s1)):
		if s1[i] != s2[i]:
			return False
	return True
res = 0
for x in range(100, 999):
	for y in range (100, 999):
		if isPanlindrome(x*y):
			if x * y > res:
				res = x * y
print res 
