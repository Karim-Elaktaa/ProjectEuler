from itertools import permutations

data = "0123456789"
permuts = [''.join(x) for x in permutations(data)]
permuts.sort()
print permuts[1000000 - 1]
