import time

def check_conjecture(n):
    square = 1
    increment = 3
    while 2*square < n:
        if prime_library[n-2*square] == True:
            return False
        square += increment
        increment += 2
    return True

def primes(n):
    sieve = {x: True for x in range(2, n)}
    for i in range(2,int(n**0.5)+1):
        if sieve[i] == True:
            for j in range(2*i, len(sieve), i):
                sieve[j] = False
    return sieve

start = time.clock()
prime_library = primes(10000)
m = 35

while True:
    if prime_library[m] == False:
        if check_conjecture(m):
            print (m)
            print (time.clock() - start)
            break
    m += 2
