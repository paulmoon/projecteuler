import math

def check_prime(n):
    if n <= 0:
        return False

    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False

    return True

if __name__ == '__main__':
    number = 600851475143
    curr = int(math.sqrt(number)+1)
    if curr % 2 == 0:
        curr += 1

    while curr > 0:
        if number % curr == 0 and check_prime(curr):
            print curr
            break
        curr -= 2
