import math
import time

def primes(n):
    sieve = {x: True for x in range(2, n)}
    for i in range(2, int(math.sqrt(n)+1)):
        if sieve[i] == True:
            for j in range(2*i, n, i):
                sieve[j] = False
    return sieve

def check_digits(first, second):
    if len(set(first)) != len(set(second)):
        return False
    return sorted(first) == sorted(second)

start = time.clock()
prime_library = primes(10000)

for i in range(1000, 3340):
    first, second, third = i, i + 3330, i + 6660
    if prime_library[first] and prime_library[second] and prime_library[third]:
        first, second, third = str(first), str(second), str(third)
        if first != '1487' and check_digits(first, second) and check_digits(second, third):
            print (int(first + second + third))
            print (time.clock() - start)
            break
