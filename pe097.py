import time

start = time.clock()
print ((28433 * (2 ** 7830457) + 1) % (10**10))
print (time.clock() - start)
