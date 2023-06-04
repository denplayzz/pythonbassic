# Програма для розрахування податка
# Функція програми
def calculate_tax(tax, salary):
    tax_salary = float(salary * tax) / 100
    net_income = float(salary - tax_salary)
    # Повернення значень які вишли після формули для розрахунку
    return net_income, tax_salary


if __name__ == '__main__':
    # Цикл для помилки
    while True:
        try:
            # Основний цикл
            salary = float(input("Введіть розмір вашої зарплати: "))
            tax = float(input("Введіть відсоток вашого податку: "))
            net_income, tax_salary = calculate_tax(tax, salary)
            print(f"Ваш чистий прибуток: {net_income}\nПодаток який треба заплатити: {tax_salary}")
            exit()
        except Exception:
            print("Некоректне введеня. (not int) введіть число")
