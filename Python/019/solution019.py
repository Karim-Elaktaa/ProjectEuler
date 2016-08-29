import datetime

start = datetime.date(1901, 1, 1)
end = datetime.date(2000, 12, 31)
delta = end - start
print sum(1 for x in range(delta.days + 1) if (start + datetime.timedelta(x)).weekday() == 6 and (start + datetime.timedelta(x)).day == 1)
print sum(1 for y in range(1901, 2001) for m in range (1, 13) if datetime.date(y, m, 1).weekday() == 6)
