# Список для сумированых чисел
numbers = list()
# Цыкл для программы
while True:
    user_numbers = input("Введите число, либо \"sum\" что-бы суммировать числа: ")
    # Условие для "sum"
    try:
        if user_numbers.lower() == "sum":
            total = sum(numbers)
            print(f"Сумма ваших чисел: {total}")
            break
        sum_user = float(user_numbers)
        # Добавление числ в список
        numbers.append(sum_user)
    # Выведение ошибки для некоректного вволда
    except Exception:
        print("Введено не коректное значение")