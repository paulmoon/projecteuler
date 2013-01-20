primes = [1]*10000000
primes[0] = primes[1] = 0
solution = []


# Sieve of Eratosthenes
for i in range(2, 10000000):
    if primes[i] == 1:
        for j in range(2*i, 10000000, i):
            primes[j] = 0

for i in range(11, 10000000):
    is_truncatable = True
    temp = str(i)
    for j in range(len(temp)):
        left = ''.join(list(temp)[:j+1])
        right = ''.join(list(temp)[j:])

        if primes[int(left)] == 0 or primes[int(right)] == 0:
            is_truncatable = False
    if is_truncatable:
        solution.append(i)
        if len(solution) == 11:
            break

print sum(solution)