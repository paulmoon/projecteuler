def collats(n):
    count = 1
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        count += 1
    return count

solution = 0
max_count = 0

for i in range(1, 1000000):
    num = collats(i)
    if num > max_count:
        max_count = num
        solution = i

print solution