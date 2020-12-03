def sum_digits(n):
    if n < 0:
        n = int((n ** 2) ** 0.5)
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


print(sum_digits(-1))
print(sum_digits(-11))
print(sum_digits(-3433))

# extract the last digit of n with % 10
# if n > 9, do the same operation on n // 10
# not sure if this is how best to handle negative inputs
# could of course just use abs()
# or an assertion
# or treat the first digit as negative and the rest positive
# or all as negative
# not that it really matters