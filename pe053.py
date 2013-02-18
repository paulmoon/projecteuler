import time

start = time.clock()

pascal_t = {}
for x in range(101):
    pascal_t[(x, x)] = 1
    pascal_t[(x, 0)] = 1

solution = 0

# Todo: Further optimize using symmetry of Pascal's triangle
for n in range(1, 101):
    for r in range(1, n):
        if (n, r) not in pascal_t:
            pascal_t[(n, r)] = pascal_t[(n - 1, r - 1,)] + pascal_t[(n - 1, r)]
        if pascal_t[(n, r)] > 10**6:
            solution += 1

print (solution)
print (time.clock() - start)
