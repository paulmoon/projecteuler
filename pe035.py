def rotate(l, n):
    return l[n:] + l[:n]

primes = [1]*1000000
solution = []

# Sieve of Eratosthenes
for i in range(2, 1000000):
    if primes[i] == 1:
        for j in range(2*i, 1000000, i):
            primes[j] = 0

for i in range(2, 1000000):
    is_circular = True
    for j in range(len(str(i))):
        temp = ''.join(rotate(list(str(i)), j))
        if primes[int(temp)] == 0:
            is_circular = False
    if is_circular:
        solution.append(i)

print len(solution)