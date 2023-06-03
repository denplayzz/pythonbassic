# Програма що перевіряє чи є введена строка дзеркальною (паліндромом)
while True:
    x = input("Введите строку: ").lower()
    # Змінна для видалення знаків пунктуації
    punctuation = ",.!?-+\"—«»"
    # Цикл "for"для видалення знаків пунктуації
    for punctuation_symbol in punctuation:
        x = x.replace(punctuation_symbol, "")
    x = x.replace(" ", "").replace("	", "").strip(punctuation)
    print(x)
    # Умови для перевірки чи є слово паліндромом
    x1 = x[::-1]
    if x == x1:
        print("Ваше слово паліндром!")
    else:
        print("Ваше слово неє паліндромом")
    # Умова для повторення програми
    choice = input("Хочите провірити ще якесь слово? (Так/Ні): ")
    if choice.lower() != "так":
        break
