import math
import time

def check_prime(n):
    for i in range(3, int(math.sqrt(n)+1), 2):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    start = time.clock()
    number = 600851475143
    curr = int(math.sqrt(number)+1)
    if curr % 2 == 0:
        curr += 1

    while curr > 0:
        if number % curr == 0 and check_prime(curr):
            print (curr)
            print (time.clock() - start)
            break
        curr -= 2
