import math
import time

def calculate_score(word):
    score = 0
    for char in word:
        score += ord(char) - 64
    return score

start = time.clock()
inputFile = open("words.txt", "r")
solution = 0

for line in inputFile:
    for word in line.replace('"', '').strip().split(','):
        score = calculate_score(word)
        # If n is the mth triangle number, then n = m*(m+1)/2
        # Solve using quadratic formula, and we get m = (sqrt(8*n+1)-1)/2
        # Since sqrt(8*n + 1) must be an integer, we test if 8*n + 1 is
        # a square number.
        if math.sqrt(8*score + 1) % 1 == 0:
            solution += 1

print (solution)
print (time.clock() - start)
