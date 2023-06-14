def run_notes_program():
    notes_users = {}

    def menu():
        while True:
            user_question = input(
                'Вы в программе "Заметки", доступные команды:\nДобавить заметку = add\nУдалить заметку = delete\nСортировать заметки = sort\nПосмотреть заметки = show\nНажмите Enter, чтобы выйти\n> ').lower()
            try:
                if user_question == "add":
                    add_notes()
                elif user_question == "delete":
                    delete_notes()
                elif user_question == "show":
                    show_notes()
                elif user_question == "sort":
                    menu_sort()
                elif user_question == "":
                    break
            except Exception:
                pass

    def menu_sort():
        while True:
            user_question_sort = input(
                "Как вы хотите сортировать заметки?\nОт новой до старой = earliest\nОт старой до новой = latest\nОт самой короткой до самой длинной = shortest\nОт самой длинной до самой короткой = longest\nНажмите Enter, чтобы выйти из меню сортировки\n> ").lower()
            if user_question_sort == "earliest":
                show_notes()
            elif user_question_sort == "latest":
                latest()
            elif user_question_sort == "shortest":
                shortest()
            elif user_question_sort == "longest":
                longest()
            elif user_question_sort == "":
                break
            else:
                pass

    def add_notes():
        i = 1
        while True:
            y = input('Введите заметку: ')
            notes_users[i] = y
            i += 1
            print("Заметка добавлена!")
            add = input("Хотите добавить ещё заметку? (да/нет): ").lower()
            if add != "да":
                break

    def delete_notes():
        show_notes()
        notes_delete = input("Введите номер заметки, чтобы удалить её: ")
        notes_delete = int(notes_delete)
        if notes_delete in notes_users:
            del notes_users[notes_delete]
            print(f"Заметка под номером {notes_delete} удалена")
        else:
            print("Заметка не найдена")

    def latest():
        x = dict(reversed(notes_users.items()))
        for num, note in x.items():
            print(f"{num}. {note}")

    def shortest():
        sort_long_notes = sorted(notes_users.keys(), key=lambda x: len(notes_users[x]), reverse=False)
        for num in sort_long_notes:
            print(f'{num}: {notes_users[num]}')

    def longest():
        sorted_notes = sorted(notes_users.keys(), key=lambda x: len(notes_users[x]), reverse=True)
        for num in sorted_notes:
            print(f'{num}: {notes_users[num]}')

    def show_notes():
        for num, note in notes_users.items():
            print(f"{num}. {note}")

    # Вызов функции меню
    menu()


if __name__ == '__main__':
    run_notes_program()
