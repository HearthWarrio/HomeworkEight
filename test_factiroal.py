from factorial import calculate_factorial


def test_calculate_factorial():
    assert calculate_factorial(0) == 1, "Ошибка: факториал 0 должен быть равен 1."
    assert calculate_factorial(5) == 120, "Ошибка: факториал 5 должен быть равен 120."
    try:
        calculate_factorial(-3)
        assert False, "Ошибка: должно быть выброшено исключение для отрицательного числа."
    except ValueError:
        pass

# Запуск тестов
test_calculate_factorial()
print("Все тесты пройдены успешно!")
