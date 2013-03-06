import time

start = time.clock()
limit = 2*(10**6)
smallest_difference = limit
solution = (0, 0)

for m in range(1, 100):
    for n in range(1, m):
        num = ((m+1)*m*(n+1)*n)//4
        difference = abs(limit - num)
        if difference < smallest_difference:
            smallest_difference = difference
            solution = (m, n)

print (solution[0]*solution[1])
print (time.clock() - start)
