import datetime
import time

start_time = time.clock()

start = datetime.date(1901, 1, 1)
end = datetime.date(2000, 12, 31)
solution = 0

while start <= end:
    if start.day == 1 and start.isoweekday() == 7:
        solution += 1
    start += datetime.timedelta(days=1)

print (solution)
print (time.clock() - start_time)
