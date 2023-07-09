def fibonacci_generator(n):
    """
    :param n: Количество сколько чисел хочет сгенерировать пользователь
    :return: Генерирует по формуле каждый елемент Фибаначи
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    fibonacci = fibonacci_generator(10)

    for i in fibonacci:
        print(i)
