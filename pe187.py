import math
import time

def primes(n):
    sieve = [True]*n
    for i in range(3, int(limit**0.5)+1, 2):
        if sieve[i] == True:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i] == True]

start = time.clock()
limit = 10**8
solution, count = 0, 0
prime_library = primes(limit)

num_primes = []
prev_prime = 0
count = 0
for prime in prime_library:
    for j in range(prev_prime, prime):
        num_primes.append(count)
    prev_prime = prime
    count += 1

# http://mathworld.wolfram.com/Semiprime.html
for k in range(1, int(num_primes[int(math.sqrt(limit))])+1):
    solution += (num_primes[limit//prime_library[k-1]]) - k + 1

print (solution)
print (time.clock() - start)
