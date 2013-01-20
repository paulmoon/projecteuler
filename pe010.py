def sieve_of_eratosthenes(n):
    for i in range(2, len(n)):
        if n[i] == 1:
            for j in range(2*i, len(n), i):
                n[j] = 0

primes = [1]*2000000
sieve_of_eratosthenes(primes)
solution = 0

for x in range(2, len(primes)):
    if primes[x] == 1:
        solution += x

print solution