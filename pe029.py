import time

start = time.clock()
solution_set = []

for a in range(2, 101):
    for b in range(2, 101):
        solution_set.append(a**b)

print (len(set(solution_set)))
print (time.clock() - start)
