import time

start = time.clock()
# After analyzing the first few maximum remainders, it seems that
# when n is odd, r_max = n*n - n = n * (n-1) and
# when n is even, r_max = n*n - 2n = n * (n-2)
# For a given a, (a-1)//2 * 2 = a-1 for odd a's and a-2 for even a's
print (sum((a-1)//2*a*2 for a in range(3, 1001)))
print (time.clock() - start)
