import itertools
import time

start = time.clock()
permutations = itertools.permutations(range(10))
print (list(permutations)[10**6-1])
print (time.clock() - start)
