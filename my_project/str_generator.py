def elements_in_str(user_str):
    """
    :param user_str: Входная строка пользователя
    :return: Генерирует каждое слово (i) из строки пользователя (user_str)
    """
    for i in user_str.split():
        yield i


if __name__ == '__main__':
    user_str = "i am generating words from text"
    element = elements_in_str(user_str)
    for i in element:
        print(i)
