import time

start = time.clock()
matrix = [[int(x) for x in line.strip().split(",")] for line in open("matrix.txt", "r")]

def build_matrix(x, y):
    if x == 0 and y == 0:
        return
    elif x == 0:
        matrix[x][y] += matrix[x][y-1]
    elif y == 0:
        matrix[x][y] += matrix[x-1][y]
    else:
        matrix[x][y] += min(matrix[x][y-1], matrix[x-1][y])

for i in range(len(matrix)):
    for j in range(len(matrix)):
        build_matrix(i, j)

print (matrix[-1][-1])
print (time.clock() - start)
