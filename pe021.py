import time

def d(n):
    factors = []
    for i in range(1, (n//2)+1):
        if n % i == 0:
            factors.append(i)
    return factors

start = time.clock()
solution = []

for a in range(1, 10000):
    temp = sum(d(a))
    b = sum(d(temp))
    if a == b and a != temp:
        solution.append(a)

print (sum(solution))
print (time.clock() - start)
