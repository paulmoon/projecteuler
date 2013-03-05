import time

start = time.clock()
matrix = [[int(x) for x in line.strip().split(",")] for line in open("matrix.txt", "r")]
matrix = [list(i) for i in zip(*matrix)]
m = len(matrix)

for x in range(1, m):
    copy = matrix[x][:]

    for y in range(m):
        if y == 0: matrix[x][y] += matrix[x-1][y]
        else: matrix[x][y] += min(matrix[x-1][y], matrix[x][y-1])

    for y in range(m-2, -1, -1):
        matrix[x][y] = min(matrix[x][y], copy[y] + matrix[x][y+1])

print (min(matrix[-1]))
print (time.clock() - start)
