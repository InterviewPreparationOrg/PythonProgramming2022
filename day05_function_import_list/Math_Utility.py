def addition(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


def squaqre(n):
    return multiplication(n, n)


def cube(n):
    return squaqre(n) * n


def is_odd(n):
    return n % 2 != 0


def is_even(n):
    return n % 2 == 0
