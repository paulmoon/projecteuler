import math
import time

start = time.clock()
limit = 10**7
num_divisors = [2]*limit

for i in range(2, limit//2):
    for j in range(2*i, limit, i):
        num_divisors[j] += 1

solution = 0

for i in range(2, limit-1):
    if num_divisors[i] == num_divisors[i+1]:
        solution += 1

print (solution)
print (time.clock() - start)
