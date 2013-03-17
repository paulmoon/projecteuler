import time

# After trying sample calculations for small numbers, it seems to be the case
# that when n = multiple of 2500, f(n) = f(n * (5^k)) for k >= 0
# E.g. f(2500) = 92864 = f(2500*5) = f(2500*25) ...
# Therefore we only need to calculate f(2560000) since 2560000 is the smallest
# number so that 2560000 is divible by 2500, and 2560000*(5^n) = 10**12 for some n.
start = time.clock()
limit = 2560000
solution = 1

while limit > 0:
    solution = solution * limit
    while solution % 10 == 0:
        solution = solution // 10
    solution = solution % 10**6
    limit -= 1

print (solution % 10**5)
print (time.clock() - start)
