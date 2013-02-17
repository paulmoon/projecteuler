import math
import itertools
import time
import sys

def is_prime(num):
    for prime in prime_library:
        if num % prime == 0:
            return False
    return True

def rwh_primes(n):
    # Obtained from stackoverflow. I did not write this.
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

start = time.clock()
prime_library = rwh_primes(int(math.sqrt(987654321)))

# If the digits add up to a multiple of 3, it is not a prime.
possible_digits = [x for x in range(9, 0, -1) if (x*(x+1))//2 % 3 != 0]

for n in possible_digits:
    pandigital = itertools.permutations(range(n, 0, -1))

    for pan in pandigital:
        # Preliminary checking
        if pan[-1] % 2 == 0:
            continue
        int_i = int(''.join(str(i) for i in pan))
        if is_prime(int_i):
            print (int_i)
            print (time.clock() - start)
            sys.exit()
