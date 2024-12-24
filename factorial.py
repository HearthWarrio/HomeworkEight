def calculate_factorial(n):
    """
    Вычисляет факториал числа n.
    :param n: Неотрицательное целое число
    :return: Факториал числа n
    :raises ValueError: Если n отрицательное
    """
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел.")
    elif n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial
