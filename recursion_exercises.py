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


def convert_to_binary(x: int) -> str:
    """Convert a base-ten integer into its binary equivalent."""
    # divide x by 2
    # the remainder is the last binary digit
    # divide the quotient of x // 2 by 2
    # the remainder is the second-to-last binary digit
    # repeat until quotient == 0
    def inner(x):
        if x // 2 == 0:
            return str(x % 2)
        return convert_to_binary(x // 2) + str(x % 2)

    assert type(x) == int, "Integers only."
    if x < 0:
        x *= -1
        return "-" + inner(x)
    return inner(x)

# convert_to_binary(2) -> convert_to_binary(1) + "0" -> "1" + "0"
# 3 -> convert_to_binary(1) + "1"
# 4 -> convert_to_binary(2) + "0" -> convert_to_binary(1) + "0" + "0" -> "1" + "0" + "0"


def multiply_list_elements(l):
    """Returns the product of all the elements in a list."""
    # not sure how to do type hints for lists containing different data types, returning who knows what data type
    if not l:
        return 1
    return l[0] * multiply_list_elements(l[1:])


def sum_range(num: int) -> int:
    """Returns the sum of range(num + 1) using recursion."""
    assert type(num) == int, "Non-negative integers only."
    if num == 0:
        return 0
    return num + sum_range(num - 1)


def reverse_string(s: str) -> str:
    """Returns s, reversed using recursion."""
    assert type(s) == str, "Strings only."
    if not s:
        return ""
    return s[-1] + reverse_string(s[:-1])





print("here for debugging purposes only")
