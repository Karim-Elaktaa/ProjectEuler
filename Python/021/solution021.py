memory = {key:sum([value for value in range(1, key/2 + 1) if key % value == 0]) for key in range(1, 10001)}
print sum([key for key, value in memory.iteritems() for key2, value2 in memory.iteritems() if (key != key2 and key == value2 and key2 == value)])
