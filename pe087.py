import time

def prime_sieve(n):
    sieve = [True]*n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i] == True:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [x for x in range(3, n, 2) if sieve[x] == True]

start = time.clock()
limit = 50000000
solution = set()

primes = prime_sieve(int(limit**0.5))
square = {x: x**2 for x in primes if x**2 < limit}
cube = {x: x**3 for x in primes if x**3 < limit}
quad = {x: x**4 for x in primes if x**4 < limit}

for q in sorted(quad.keys()):
    for c in sorted(cube.keys()):
        for s in sorted(square.keys()):
            total = quad[q] + cube[c] + square[s]
            if total > limit:
                break
            solution.add(total)

print (len(solution))
print (time.clock() - start)
