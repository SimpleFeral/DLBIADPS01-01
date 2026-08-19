def calc_sum_of_squares_rec(n):
    if n <= 0:
        return 0
    return (n*n) + calc_sum_of_squares_rec(n - 1)

def calc_sum_of_squares_itr(n):
    result = 0
    while n > 0:
        result += n*n
        n -= 1
    return result

print(calc_sum_of_squares_rec(4))
print(calc_sum_of_squares_itr(4))