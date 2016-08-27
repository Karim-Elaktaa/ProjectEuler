v = 600851475143
i = 2
while i * i < v:
    while v % i == 0:
        v = v / i
    i = i + 1

print v

