import math

def is_prime(n):
    if n <= 0:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

primes = []
curr = 1

while len(primes) <= 10000:
    if is_prime(curr):
        primes.append(curr)
    curr += 2

print primes[-1]