import time

def sieve(n):
    sieve = [True]*n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i] == True:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i] == True]

def main():
    start = time.clock()
    limit = 10**6
    primes = sieve(limit)

    primes_sum = sum(primes)
    n = length = len(primes)

    while primes_sum > limit:
        n -= 1
        primes_sum -= primes[n]

    while n > 0:
        primes_sum = sum(primes[:n])
        head, tail = 0, n

        while tail < length and primes_sum not in primes and primes_sum < limit:
            primes_sum -= primes[head]
            primes_sum += primes[tail]
            head += 1
            tail += 1

        if primes_sum in primes:
            print (primes_sum)
            print (time.clock() - start)
            break
        n -= 1

if __name__ == '__main__':
    main()
