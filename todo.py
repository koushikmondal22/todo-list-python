tasks = []


def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass


def add_task():
    task = input("Enter a task: ")

    if task.strip() == "":
        print("Task cannot be empty.")
        return

    tasks.append(task)
    save_tasks()
    print("Task added successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")

        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def delete_task():
    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            save_tasks()
            print(f"Deleted: {deleted_task}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Invalid input! Please enter a number.")


load_tasks()

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")