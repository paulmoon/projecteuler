sum_of_squares = sum(range(1, 101))**2
square_of_sum = sum([x**2 for x in range(1, 101)])

print(sum_of_squares - square_of_sum)