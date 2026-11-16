def digit_sum(n):
    if n == 1 or n == 0:
        return n
    return digit_sum(n-1) + n


print(digit_sum(5))