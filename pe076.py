import time

start = time.clock()
# Partition function. p(n)
p = {0: 1, 1: 1}

# g(k) is the kth pentagonal number
def g(k):
    return (k*(3*k-1))//2

def sign(k):
    if k % 2 == 0:
        return -1
    return 1

# http://en.wikipedia.org/wiki/Pentagonal_number_theorem
for n in range(1, 101):
    k = 1
    summation = 0
    while g(k) <= n:
        summation += sign(k)*p[n-g(k)]
        if (n-g(-k)) >= 0:
            summation += sign(-k)*p[n-g(-k)]
        k += 1
    p[n] = summation

print (p[100]-1)
print (time.clock() - start)
