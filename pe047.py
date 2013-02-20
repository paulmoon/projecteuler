import time
import sys

start = time.clock()
limit = 10**6
num_factors = [0]*limit

for i in range(2, int(limit**0.5)+1):
    if num_factors[i] == 0:
        for j in range(2*i, limit, i):
            num_factors[j] += 1

answer = [4]*4

for i in range(limit-3):
    if num_factors[i:i+4] == answer:
        print (i)
        print (time.clock() - start)
        break
