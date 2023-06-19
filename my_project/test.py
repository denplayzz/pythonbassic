import json

def load_notes():
    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            notes_content = file.readlines()
            notes_users = {}
            for line in notes_content:
                header, note = line.strip().split(":")
                notes_users[header.strip()] = note.strip()
            return notes_users
    except FileNotFoundError:
        return {}

def menu(notes_users={}):
    while True:
        user_question = input(
            'Вы в программе "Заметки", доступные команды:\nДобавить заметку = add\nУдалить заметку = delete\nСортировать заметки = sort\nПосмотреть заметки = show\nСохранить заметки в файл = save\nИмпортировать имеющиеся заметку в програму = load\nНажмите Enter, чтобы выйти\n> ').lower()
        try:
            if user_question == "add":
                add_notes(notes_users)
            if user_question == "enumerate":
                enumerate_notes(notes_users)
            if user_question == "delete":
                delete_notes(notes_users)
            if user_question == "show":
                show_notes(notes_users)
            if user_question == "sort":
                menu_sort(notes_users)
            if user_question == "save":
                save_notes(notes_users)
            if user_question == "load":
                load_notes(notes_users)
            if user_question == "":
                break
        except Exception:
            pass

    return notes_users

def add_notes(notes_users):
    while True:
        header = input("Введите заголовок заметки\n>")
        note = input("Введите заметку\n>")
        notes_users[header] = note
        x = input("Заметка добавлена!\nХотите добавить ещё заметку? (да/нет): ")
        if x.lower() != "да":
            break
        else:
            continue

def save_notes(notes_users):
    with open("notes.txt", "a", encoding="utf-8") as file:
        for header, note in notes_users.items():
            file.write(f"{header}: {note}\n")
    print("Заметки сохранены в файл.")

def delete_notes(notes_users):
    show_notes(notes_users)
    notes_delete = input("Введите номер заметки, чтобы удалить её: ")
    notes_delete = int(notes_delete)
    index = 1
    for key in notes_users.keys():
        if index == notes_delete:
            del notes_users[key]
            print(f"Заметка под номером {notes_delete} удалена")
            break
        index += 1
    else:
        print("Заметка не найдена")

def menu_sort(notes_users):
    while True:
        user_question_sort = input(
            "Как вы хотите сортировать заметки?\nОт новой до старой = earliest\nОт старой до новой = latest\nОт самой короткой до длинной = shortest\nОт самой длинной до короткой = longest\nНажмите Enter, чтобы выйти из меню сортировки\n> ").lower()
        if user_question_sort == "earliest":
            show_notes(notes_users)
        if user_question_sort == "latest":
            latest(notes_users)
        if user_question_sort == "shortest":
            shortest(notes_users)
        if user_question_sort == "longest":
            longest(notes_users)
        if user_question_sort == "":
            break
        else:
            pass

    return notes_users

def enumerate_notes(notes_users):
    for index, (key, value) in enumerate(notes_users.items(), start=1):
        print(f"{index}. {key}: {value}")

def latest(notes_users):
    for num, note in sorted(notes_users.items(), reverse=True):
        print(f"{num}. {note}")

def shortest(notes_users):
    for num, note in sorted(notes_users.items(), key=lambda x: len(x[1])):
        print(f'{num}: {note}')

def longest(notes_users):
    for num, note in sorted(notes_users.items(), key=lambda x: len(x[1]), reverse=True):
        print(f'{num}: {note}')

def show_notes(notes_users):
    for index, (key, value) in enumerate(notes_users.items(), start=1):
        print(f"{index}. {key}: {value}")

if __name__ == '__main__':
    menu(notes_users=load_notes())
