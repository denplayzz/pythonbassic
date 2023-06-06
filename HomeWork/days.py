# Програма для конвертації секунд в хвилини, години, дні


# Функція для перетворення
def function(seconds) -> int:
    # Програмна логіка
    minutes, seconds = divmod(seconds, 60)
    hour, minutes = divmod(minutes, 60)
    days, hour = divmod(hour, 24)
    # Створення словника для результату
    result = {
        "days": days,
        "hour": hour,
        "minutes": minutes,
        "seconds": seconds
    }
    return result


if __name__ == '__main__':
    # Запрос до користувача, і запрос до функції
    while True:
        try:
            seconds = int(input("Введіть секунди для конвертації: "))
            # Виведення результату
            print(function(seconds))
            exit()
        except Exception:
            print("Введено не число: ")
