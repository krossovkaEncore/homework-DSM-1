tasks = []


def show_menu():
    print("\n=== Менеджер задач ===")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Редактировать задачу")
    print("4. Удалить задачу")
    print("0. Выход")


def show_tasks():
    if not tasks:
        print("Список задач пуст.")
        return

    print("\nСписок задач:")

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def add_task():
    task = input("Введите название задачи: ")

    if task.strip():
        tasks.append(task)
        print("Задача добавлена.")
    else:
        print("Название задачи не может быть пустым.")


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
                print("Задача изменена.")
            else:
                print("Название не может быть пустым.")
        else:
            print("Такой задачи нет.")

    except ValueError:
        print("Введите число.")


def delete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("Введите номер задачи: ")) - 1

        if 0 <= number < len(tasks):
            deleted_task = tasks.pop(number)
            print(f"Задача «{deleted_task}» удалена.")
        else:
            print("Такой задачи нет.")

    except ValueError:
        print("Введите число.")


def main():
    while True:
        show_menu()

        choice = input("Выберите действие: ")

        if choice == "1":
            show_tasks()

        elif choice == "2":
            add_task()

        elif choice == "3":
            edit_task()

        elif choice == "4":
            delete_task()

        elif choice == "0":
            print("Выход из программы...")
            break

        else:
            print("Неизвестная команда.")


if __name__ == "__main__":
    main()
