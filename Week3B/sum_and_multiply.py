__author__ = 'KoicsD'


# Defining two functions named 'sum' and 'multiply'
# which adds and multiplies respectively
# the elements of the given list.


def sum(numbers: list):
    if not all([type(n) == int or type(n) == float for n in numbers]):
        return None
    res = 0
    for n in numbers:
        res += n
    return res


def multiply(numbers: list):
    if not all([type(n) == int or type(n) == float for n in numbers]):
        return None
    res = 1
    for n in numbers:
        res *= n
    return res
