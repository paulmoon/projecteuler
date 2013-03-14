import time

# Number of ways to arrange n units into blocks of length m units.
def f(m, n):
    if m > n:
        return 1

    total = 1

    for start in range(n-m+1):
        if (m, n-start-m) in memoization:
            result = memoization[(m, n-start-m)]
        else:
            result = f(m, n-start-m)
            memoization[(m, n-start-m)] = result
        total += result
    return total

start = time.clock()
memoization = {}
solution = 0

for i in range(2, 5):
    solution += f(i, 50) - 1

print (solution)
print (time.clock() - start)
