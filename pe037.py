import math

limit = 750000
primes = {x: True for x in range(limit)}
primes[0] = primes[1] = False
solution = []

# Sieve of Eratosthenes
for i in range(2, int(math.sqrt(limit)+1)):
    if primes[i] == True:
        for j in range(2*i, limit, i):
            primes[j] = False

for i in range(11, limit):
    is_truncatable = True
    temp = str(i)
    for j in range(len(temp)):
        left = temp[:j+1]
        right = temp[j:]

        if primes[int(left)] == False or primes[int(right)] == False:
            is_truncatable = False
            break
    if is_truncatable:
        solution.append(i)
        if len(solution) == 11:
            break

print (sum(solution))
