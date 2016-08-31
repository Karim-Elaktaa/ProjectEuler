f = open("p022_names.txt")
listWords = f.read().replace('"','')
l = listWords.split(",")
l.sort()
total = 0
for i in l:
	total += (l.index(i) + 1) * sum(ord(x) -ord('A') + 1 for x in i)
print total

