import datetime
import time

def increment_month(dt_object):
    month = dt_object.month % 12 + 1
    year = dt_object.year + (month // 12)
    return datetime.date(year, month, dt_object.day)

start_time = time.clock()

start = datetime.date(1901, 1, 1)
end = datetime.date(2000, 12, 31)
solution = 0

while start <= end:
    if start.day == 1 and start.isoweekday() == 7:
        solution += 1
    start = increment_month(start)

print (solution)
print (time.clock() - start_time)
