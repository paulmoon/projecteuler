import math
import time

def count_n(a, b):
    n = 0
    while True:
        number = formula(n, a, b)
        if number < 2: return n-1
        if prime_library[number] == False: return n-1
        n += 1
    return 0

def formula(n, a, b):
    return n*n + a*n + b

def sieve_of_eratosthenes(n):
    sieve = {x: True for x in range(n)}
    sieve[0] = sieve[1] = False 
    for i in range(2, int(math.sqrt(n)+1)):
        if sieve[i] == True:
            for j in range(2*i, n, i):
                sieve[j] = False
    return sieve

start = time.clock()
prime_library = sieve_of_eratosthenes(1000000)

temp = sieve_of_eratosthenes(1000)
primes = []

# Not including -b since negative numbers aren't primes!
for key in temp.keys():
    if temp[key] == True:
        primes.append(key)

a_list = []

# Notice that if we use even numbers for a,
# n = x: n^2 + a*n + b
# n = 0: odd (only b, and it must be a prime -> odd)
# n = 1: odd + even + odd = even != prime
# Therefore we only use odd numbers for a.
for i in range(1, 1000, 2):
    a_list.append(i)
    a_list.append(-i)

solution = 0
max_number = 0

for b in primes:
    for a in a_list:
        n = count_n(a, b)
        if n > max_number:
            max_number = n
            solution = a*b

print (solution)
print (time.clock() - start)
