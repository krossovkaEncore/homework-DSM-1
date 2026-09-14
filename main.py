is_runing = True
tasks = []

def areYouSerious():
    confirm = input("Вы уверенны в этом? Да/Нет : ").startswith("")
    for i in ["n", "not", "нет", "н", "no"]:
        if confirm == i:
            return True
    else:
        return False

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
            if not areYouSerious():
            	deleted_task = tasks.pop(number)
            	print(f"Задача «{deleted_task}» удалена.")
        else:
            print("Такой задачи нет.")

    except ValueError:
        print("Введите число.")

while is_runing:
    
    print()
    print("=== Менеджер задач ===")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Редактировать задачу")
    print("4. Удалить задачу")
    print("5. Выход")

	match int(input("Выберите действие: ")):
    	case 1:
    		show_tasks()
		case 2:
        	add_task()
    	case 3:
        	edit_task()
    	case 4:
        	delete_task()
    	case 5:
    		confirm = input("Вы действительно хотите выйти? Да/Нет : ")
            if not areYouSerious():
    			is_runing = False
		case _:
			print("Неизвестная команда.")