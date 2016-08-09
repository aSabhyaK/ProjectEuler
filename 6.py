upper_limit = 100;

sum_of_squares = (upper_limit * (upper_limit + 1) * (2 * upper_limit + 1)) / 6;
square_of_sum = ((upper_limit * (upper_limit + 1)) / 2) ** 2;

print(int(square_of_sum - sum_of_squares));