with open("data", "r") as file:
	data = file.read()
print data
print "Length data : ", len(data)
max = 0
for i in range (0, len(data) - 13):
	tot = 1
	for j in range (0, 13):
		tot = tot * int(data[i + j])
	if tot > max:
		max = tot
print max
