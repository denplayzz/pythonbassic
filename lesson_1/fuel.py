    # Програма що рахує витрати на паливо
    # Росхід палива на 100км
fuel_100 = float(input("Введите росход топлива на 100км: "))
    # Ціна палива
fuel_price = float(input("Введите цену за топливо: "))
    # Відстань яку ви хочете проїхати
distance = float(input("Введите растояние которое хотите проехать: "))


fuel_distance = round(fuel_100 / 100 * distance, 2)
price_distance = round(fuel_distance * fuel_price, 2)
print(f"Вы потратите {fuel_distance} литров топлива")
print(f"Стоимость топлива будет {price_distance}")

input()