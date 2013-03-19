import time

def f(n):
    if 2 > n:
        return 1
    total = 1
    for length in range(2, 5):
        for start in range(n-length+1):
            if n-(start+length) in memoization:
                result = memoization[n-(start+length)]
            else:
                result = f(n-(start+length))
                memoization[n-(start+length)] = result
            total += result
    return total

start = time.clock()
memoization = {}

print (f(50))
print (time.clock() - start)
