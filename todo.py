tasks = []

def save_tasks():
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
load_tasks()

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
save_tasks()
print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

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

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")