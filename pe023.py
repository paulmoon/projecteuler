import time

start = time.clock()
limit = 28123

abudant_numbers = []

for i in range(2, limit+1):
    temp = 1
    j = 2
    i_sqrt = int(i**0.5)
    while j <= i_sqrt:
        if j * j == i:
            temp += j
        elif i % j == 0:
            temp += (j + i//j)
        j += 1
    if temp > i:
        abudant_numbers.append(i)

sum_of_abudant_numbers = [False]*(limit+1)

for a in abudant_numbers:
    for b in abudant_numbers[abudant_numbers.index(a):]:
        if a+b > limit:
            break
        else:
            sum_of_abudant_numbers[a+b] = True

solution = 0

for i in range(len(sum_of_abudant_numbers)):
    if sum_of_abudant_numbers[i] == False:
        solution += i

print (solution)
print (time.clock() - start)
