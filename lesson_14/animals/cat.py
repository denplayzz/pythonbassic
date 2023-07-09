from .animal import Animal


class Cat(Animal):
    def __init__(
            self,
            name: str,
            age: int,
            say_word='Мяу-мяу!'
    ):
        """
        Класс отвечает за симуляцию животного кошка
        """
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={'рыба', 'мясо', 'молоко'}


        )
        self.animal_type = 'Кошка'

    def treat(self, hours: int) -> str:
        """
        Ухаживая за кошкой должное количество времени, мы получаем хорошее настроение
        :param hours: сколько часов ухаживаем
        :return: ничего или хорошее настроение
        """
        if hours > 2:
            print(f'Вы гуляете с {self} {hours} часов и у вас повышается настроение')
            return 'Хорошее настроение'
        print(f'Вы гуляете с {self} {hours} часов.')
        return ''
