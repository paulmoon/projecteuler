import math
import time

start = time.clock()
inputFile = open("base_exp.txt", "r")

largest = 0
solution = 0
line_num = 1

for line in inputFile:
    (base, exp) = [int(x) for x in line.strip().split(",")]
    challenger = exp*math.log(base, 10)
    if challenger > largest:
        largest = challenger
        solution = line_num
    line_num += 1

print (solution)
print (time.clock() - start)
