    #Програма, що рахує абонплату

    #Попередній місяць
ago_month = float(input("Введите данные за прошлый месяц: "))

    #Теперішній місяць
this_month = float(input("Введите данные за это-т месяц: "))

    #Тариф
tariff = float(input("Введите свой тариф: "))
x = (float((this_month - ago_month) * tariff , ))
print (round(x,2))
input()