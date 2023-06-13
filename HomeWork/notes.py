# Програма заметки
# Словарь для записи заметок
notes_users = {

}


# Основная функция для меню
def menu():
    while True:
        user_question = input(
            'Вы в програме "Заметки", доступные команды: \nДобавить заметку = add\nУдалить заметку = delete \nСортировать заметки = sort\nПосмотреть заметки = show\nНажмите Enter что бы выйти\n> ').lower()
        try:
            if user_question == "add":
                add_notes()
            if user_question == "delete":
                delete_notes()
            if user_question == "show":
                show_notes()
            if user_question == "sort":
                menu_sort()
            if user_question == "":
                exit()



        except Exception:
            pass


# Функция для меню sort
def menu_sort():
    while True:
        user_question_sort = input(
            "Как вы хотите сортировать заметки?\nОд новой до старой = earlist\nОд старой до новой = latest\nОт самой короткой до длинной = shortest\nОт самой длинной до короткой = longtest\nНажмите Enter что бы выйти из меню сортировки\n> ").lower()
        if user_question_sort == "earlist":
            show_notes()
        if user_question_sort == "latest":
            latest()
        if user_question_sort == "shortest":
            shortest()
        if user_question_sort == "longtest":
            longtest()
        if user_question_sort == "":
            break
        else:
            pass


# Функция с "menu", для добавления заметок
def add_notes():
    i = 1
    while True:
        y = input('Введите заметку: ')
        notes_users[i] = y
        i += 1
        print("Заметка добавлена!")
        add = input("Хотите добавить ещё заметку? (да/нет): ").lower()
        if add != "нет":
            continue
        else:
            break


# Функция с "menu", для удаления заметок
def delete_notes():
    show_notes()
    notes_delete = input("Введите номер заметки чтобы удалить её: ")
    notes_delete = int(notes_delete)
    if notes_delete in notes_users:
        del notes_users[notes_delete]
        print(f"Заметка под номером {notes_delete} удалена")
    else:
        print("Заметка не найдена")


# Функция с "menu_sort", для сортировки заметок, выводит сохраненные заметки в хронологическом порядке - от позднейшей до самой ранней
def latest():
    x = dict(reversed(notes_users.items()))
    for num, note in x.items():
        print(f"{num}. {note}")


# Функция с "menu_sort", для сортировки заметок, выводит сохраненные заметки в порядке от самой короткой до самой длинной

def shortest():
    sort_long_notes = sorted(notes_users.keys(), key=lambda x: len(notes_users[x]), reverse=False)
    for num in sort_long_notes:
        print(f'{num}: {notes_users[num]}')


# Функция с "menu_sort", для сортировки заметок, выводит сохраненные заметки в порядке от самой длинной до самой короткой
def longtest():
    sorted_notes = sorted(notes_users.keys(), key=lambda x: len(notes_users[x]), reverse=True)
    for num in sorted_notes:
        print(f'{num}: {notes_users[num]}')


# Функция с "menu" для показа заметок, так же служит случаем сортировки earlist, от самой ранней до самой поздней
def show_notes():
    for num, note in notes_users.items():
        print(f"{num}. {note}")


if __name__ == '__main__':
    # Вызов програмы
    menu()
