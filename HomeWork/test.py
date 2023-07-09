from random import choice, choices, randint


class Cat:
    def __init__(self, name: str, age: int, food: set):
        self.name = name
        self.age = age
        self.food = food
        self.hungry = True

    def __str__(self):
        if self.age == 1:
            ages = str(self.age) + " год"
        elif 2 <= self.age <= 4:
            ages = str(self.age) + " года"
        else:
            ages = str(self.age) + " лет"
        return f"Имя: {self.name}, Возраст: {ages}, Любимая еда: {self.food}"

    def eat(self):
        foods = ["Рыба", "Молоко", "Каша", "Рис", "Тортик", "Мышь", "Тунец", "Консервы", "Сухой корм", "Вискас",
                 "Курица", "Молоко"]
        if self.hungry:
            random_foods = choices(foods, k=6)
            for food in random_foods:
                if food in self.food:
                    string_eat = f"Вы предложили {self.name} {random_foods}\n{self.name} кушает {food}"
                    self.hungry = False
                    return string_eat
            string_eat = f"Вы предложили {self.name} {random_foods}\n{self.name} не может есть {', '.join(random_foods)}"
            return string_eat

    def hungry_cat(self):
        if self.hungry:
            hungry_str = "Проголодалась"
        else:
            hungry_str = "Сыт(а)"
        return hungry_str

    def walk(self):
        if self.hungry:
            walk_str = f"Кошка {self.name}, {self.hungry_cat()}, и потому пойдет гулять сама"
            walk_hours = randint(4, 10)
            walk_hours_str = f"\nНагуляла {walk_hours} часов"
            walk_str += walk_hours_str
            return walk_str

        else:
            walk_str = f"Кошка {self.name}, {self.hungry_cat()}, и идет гулять с Хозяином"
            walk_hours = randint(1, 3)
            walk_hours_str = f"\nНагуляла {walk_hours} часов"
            walk_str += walk_hours_str
            return walk_str

    def meow(self):
        return f"{self.name}: Мяу!"


if __name__ == '__main__':
    x = "=" * 10
    cat1 = Cat("Дуся", 1, {"Рыба", "Молоко"})
    cat2 = Cat("Мурка", 3, {"Каша", "Рис"})
    cat3 = Cat("Гав", 10, {"Рыба", "Каша"})
    cat4 = Cat("Барсик", 2, {"Сухой корм", "Вискас"})
    cat5 = Cat("Вася", 5, {"Курица", "Молоко"})
    cat6 = Cat("Макс", 7, {"Тунец", "Консервы"})

    cats = (cat1, cat2, cat3, cat4, cat5, cat6)
    cat_names = [cat.name for cat in cats]
    print(f"Созданы объекты класса Cat: {', '.join(cat_names)}")
    for cat in cats:
        print(f"{cat}\n{cat.eat()}\n{cat.hungry_cat()}\n{cat.walk()}")
        print(f"{cat.meow()}")
        print(x)
        print(f"Итог: {cat.name}, статус Еды: {cat.hungry_cat()}")
        print(f"Гуляла: {cat.walk().split()[9]} часов")
        print(x)
