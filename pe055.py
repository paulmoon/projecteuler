import time

def check_lychrel(n):
    for iteration in range(50):
        n += int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return 0
    return 1

start = time.clock()
print (sum(check_lychrel(n) for n in range(10000)))
print (time.clock() - start)
