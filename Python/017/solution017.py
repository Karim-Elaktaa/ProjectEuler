data = {
1:"one",
2:"two",
3:"three",
4:"four",
5:"five",
6:"six",
7:"seven",
8:"eight",
9:"nine",
10:"ten",
11:"eleven",
12:"twelve",
13:"thirteen",
14:"fourteen",
15:"fifteen",
16:"sixteen",
17:"seventeen",
18:"eighteen",
19:"nineteen",
20:"twenty",
30:"thirty",
40:"forty",
50:"fifty",
60:"sixty",
70:"seventy",
80:"eighty",
90:"ninety",
100:"hundred",
1000:"thousand"
}

def numberToWord(x):
	res = ""
	if x / 1000 > 0:
		res+=data[x/1000] + data[1000]
		x = x % 1000
	if x / 100 > 0:
		res+= data[x/100] + data[100]
		x = x % 100
		if x > 0:
			res+= "and"
	if x / 10 > 1:
		res+= data[x/10*10]
		x = x % 10
	elif x / 10 == 1:
		res+= data[x]
		x = 0
	if x > 0:
		res+= data[x]
	return res

print sum(len(numberToWord(x)) for x in range(1, 1001)) 
