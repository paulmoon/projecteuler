def factorial(n):
    total = 1
    while n > 1:
        total *= n
        n -= 1
    return total

print(sum([int(i) for i in str(factorial(100))]))