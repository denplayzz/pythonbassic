    # Програма для розрахунку податка від заробітньої плати

    # Заробітня плата
salary = float(input("Введите свою зарплату: "))
    # Відсоток податка
tax = float(input("Введите процент налога: "))
x = float((salary * tax) / 100 )
x1 = float(salary - x)
print(f"Чистий прубуток {round(x1,2)}" + "$")
print(f"Податок який треба сплатити {round(x,2)}" + "$")

input()