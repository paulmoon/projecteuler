import time

def coin_sums(n, denom=200):
    next_denom = 0

    if denom == 200:
        next_denom = 100
    elif denom == 100:
        next_denom = 50
    elif denom == 50:
        next_denom = 20
    elif denom == 20:
        next_denom = 10
    elif denom == 10:
        next_denom = 5
    elif denom == 5:
        next_denom = 2
    elif denom == 2:
        next_denom = 1
    elif denom == 1:
        return 1

    solution = 0
    i = 0
    while i * denom <= n:
        solution += coin_sums(n - denom*i, next_denom)
        i += 1
    return solution

start = time.clock()
print (coin_sums(200, 200))
print (time.clock() - start)
