import time

# Number of ways to arrange n units into blocks of minimum length m units.
def f(m, n):
    if m > n:
        return 1

    total = 1

    for length in range(m, n+1):
        for start in range(n-length+1):
            if (m, n-(start+length)-1) in memoization:
                result = memoization[(m, n-(start+length)-1)]
            else:
                result = f(m, n-(start+length)-1)
                memoization[(m, n-(start+length)-1)] = result
            total += result
    return total

start = time.clock()
memoization = {}
n = 1

while True:
    if f(50, n) > 10**6:
        print (n)
        print (time.clock() - start)
        break
    n += 1
