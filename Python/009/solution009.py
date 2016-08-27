for x in range(1, 1000):
	for y in range(x, 1000):
		for z in range(y, 1000):
			if x*x + y*y == z*z:
				if x + y + z == 1000:
					print "Success"
					print x, " + ", y, " = ", z
					print x * y * z
					break
