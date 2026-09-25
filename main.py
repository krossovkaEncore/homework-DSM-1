is_runing = True
tasks = []


def show_message(message):
    print(f"\n{message}")


def show_collection(collection):
    if not collection:
        show_message("Список задач пуст.")
        return

    print("\nСписок задач:")

    for number, item in enumerate(collection, start=1):
        print(f"{number}. {item}")


def areYouSerious():
    confirm = input("Вы уверены в этом? Да/Нет: ").lower().strip()

    match confirm:
        case "да" | "д" | "yes" | "y":
            return True
        case "нет" | "н" | "no" | "n":
            return False
        case _:
            return False


def show_tasks():
    show_collection(tasks)


def add_task():
    task = input("Введите название задачи: ")

    if task.strip():
        tasks.append(task)
        show_message("Задача добавлена.")
    else:
        show_message("Название задачи не может быть пустым.")


def edit_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("Введите номер задачи: ")) - 1

        if 0 <= number < len(tasks):
            new_name = input("Введите новое название: ")

            if new_name.strip():
                tasks[number] = new_name
                show_message("Задача изменена.")
            else:
                show_message("Название не может быть пустым.")
        else:
            show_message("Такой задачи нет.")

    except ValueError:
        show_message("Введите число.")


def delete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("Введите номер задачи: ")) - 1

        if 0 <= number < len(tasks):
            if areYouSerious():
                deleted_task = tasks.pop(number)
                show_message(f"Задача «{deleted_task}» удалена.")
            else:
                show_message("Удаление отменено.")
        else:
            show_message("Такой задачи нет.")

    except ValueError:
        show_message("Введите число.")


while is_runing:
    print()
    print("=== Менеджер задач ===")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Редактировать задачу")
    print("4. Удалить задачу")
    print("5. Выход")

    try:
        choice = int(input("Выберите действие: "))

        match choice:
            case 1:
                show_tasks()
            case 2:
                add_task()
            case 3:
                edit_task()
            case 4:
                delete_task()
            case 5:
                if areYouSerious():
                    is_runing = False
                    show_message("Выход из программы.")
                else:
                    show_message("Выход отменен.")
            case _:
                show_message("Неизвестная команда.")

    except ValueError:
        show_message("Введите число.")
