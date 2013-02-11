from math import sqrt 

def factor(n):
    factors = []
    for i in range(1, int(sqrt(n)+1)):
        if n % i == 0:
            factors.append(i)
            factors.append(n//i)
    return factors

i, n = 1, 1

while True:
    if len(factor(n)) >= 500:
        print (n)
        break
    i += 1
    n += i