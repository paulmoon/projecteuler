import time

def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

start = time.clock()
solution = []

for a in range(2, 100):
    for power in range(2, 15):
        if sum_digits(a**power) == a:
            solution.append(a**power)

solution.sort()
print (solution[29])
print (time.clock() - start)
