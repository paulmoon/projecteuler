from math import sqrt 

def factor(n):
    # From stackoverflow.com
    return set(reduce(list.__add__, 
            ([i, n/i] for i in range(1, int(sqrt(n)+1)) if n % i == 0)))

i = 1
n = 1

while True:
    if len(factor(n)) >= 500:
        print n
        break
    i += 1
    n += i