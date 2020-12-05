def sum_digits(n: int) -> int:
    """Returns the sum of the digits of non-negative integer n."""
    assert not n < 0, "Non-negative integer n only."
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

# extracts the last digit, then the second to last, etc and sums them


def power(x: int, y: int) -> int:
    """Returns x to the power of non-negative integer y."""
    assert not y < 0, "Non-negative integer y only."
    if y == 0:
        return 1
    return x * power(x, y - 1)

# power(2, 2) evaluates to 2 * 2 * 1


def gcd(x: int, y: int) -> int:
    """Returns the largest positive integer that divides non-zero integers x and y."""
    assert x != 0 and y != 0 and type(x) == int and type(y) == int, "Non-zero integers only."
    if x < 0:
        x *= -1
    if y < 0:
        y *= -1
    # Euclid's algorithm
    # assign the larger number to x, so can do larger % smaller
    if y > x:
        x, y = y, x
    remainder = x % y
    if not remainder:
        return y
    return gcd(y, remainder)

# doesn't return anything until remainder == 0 - at which point, returns the divisor that yielded it




print("here for debugging purposes only")