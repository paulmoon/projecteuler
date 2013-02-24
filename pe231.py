import math
import time

def num_factors(n, factor):
    """ Calculates the number of times 'factor' divides n!.
        e.g. num_factors(30, 2).
        30//2 = 15 (count of numbers less than 30 which have a factor of 2)
        15//2 = 7 (count of numbers with two factors of 2 i.e. divisible by 4)
        7//2 = 3 (count of numbers with three factors of 2 i.e. divisible by 8)
        3//2 = 1 (count of numbers with four factors of 2 i.e. divisible by 16)
        And so the power of 2 in the prime factorization of 30! is
        15 + 7 + 3 + 1 = 26. """
    num = 0
    while n > 0:
        n //= factor
        num += n
    return num

def primes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i] == True:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i] == True]

start = time.clock()
n = 20000000
k = 15000000
primes = primes(n)
solution = 0

for prime in primes:
    # n choose k = n! / (k! * (n-k)!)
    solution += prime * (num_factors(n, prime) - num_factors(k, prime) - num_factors(n - k, prime))

print (solution)
print (time.clock() - start)
