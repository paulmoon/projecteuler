# This question can easily be done with combinatorics.
# To get to the bottom right from top left, there must be n number of 
# each Rs and Ds where R = Right and D = Down (only possible operations).
# Then each path is a string of length 2n, with a unique ordering of 
# Rs and Ds. Now choose n spots from 2n available spots where Rs will go
# (no need to choose spots for Ds since there is only one choice for
# Ds, given spots for Rs). This represents the number of paths. 
# Answer = 40 choose 20 = 40!/(20!)(20!) = 137846528820

def factorial(n):
    total = 1
    while n > 1:
        total *= n
        n -= 1
    return total

def choose(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))

print choose(40, 20)