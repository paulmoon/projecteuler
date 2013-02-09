f = open("triangle.txt", "r")
tree = [[int(x) for x in line.split()] for line in f]

level = len(tree)-1
solution = tree[-1]

while level > 0:
    # Reduce current row
    solution = [max(solution[index:index+2]) for index in range(len(solution)-1)]
    level -= 1
    # Merge with upper row
    solution = map(lambda (a,b): a+b, zip(tree[level], solution))

print (solution[0])
