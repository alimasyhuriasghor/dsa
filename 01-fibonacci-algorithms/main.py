# 1. Fibonacci numbers
# Fibonacci numbers are sequence of numbers where each number is the sum of the two previous numbers.

# There are two ways to generate fibonacci numbers: using for loop and recursion

# Generate fibonacci numbers using for loop
def fib1(num: int) -> list:
    """
    Generate a list of Fibonacci numbers.

    Parameter:
        num (int): The integer number to generate fibonacci numbers. Must be a non-negative integer.

    Returns:
        list: A list of Fibonacci numbers.

    Time complexity:
        O(N): Linear in terms of how many numbers are produced.

    Space complexity:
        O(N): The space to store the fibonacci numbers have linear time complexity, since they're stored in a list which can grow dynamically.

    Examples:
        >>> fib(10)
        [0, 1, 1, 2, 3, 5, 8]

        >>> fib(5)
        [0, 1, 1, 2, 3]
    """
    result = []
    a, b = 0, 1
    while a < num:
        result.append(a)
        a, b = b, b + a
    return result

result = fib1(5)
print(result)

# Generate Fibonacci numbers using recursion
def fib2(num: int) -> int:
    if num <= 1:
        return num
    return fib2(num - 1) + fib2(num - 2)

result = fib2(19)
print(result)