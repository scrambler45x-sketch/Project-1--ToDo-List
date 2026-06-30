# Simple To-Do List Application

FILE_NAME = "tasks.txt"

def load_tasks():
    tasks = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
    return tasks


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks):
    print("\n========== YOUR TASKS ==========")

    if len(tasks) == 0:
        print("No tasks found.")

    else:
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

    print("===============================\n")


def add_task(tasks):
    task = input("Enter new task: ").strip()

    if task == "":
        print("Task cannot be empty.\n")
        return

    tasks.append("[ ] " + task)
    save_tasks(tasks)

    print("Task added successfully.\n")


def remove_task(tasks):

    if len(tasks) == 0:
        print("No tasks to remove.\n")
        return

    view_tasks(tasks)

    try:
        number = int(input("Enter task number to remove: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.\n")
            return

        removed = tasks.pop(number - 1)

        save_tasks(tasks)

        print("Removed:", removed)
        print()

    except ValueError:
        print("Please enter a valid number.\n")


def complete_task(tasks):

    if len(tasks) == 0:
        print("No tasks available.\n")
        return

    view_tasks(tasks)

    try:
        number = int(input("Enter completed task number: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.\n")
            return

        if tasks[number - 1].startswith("[✓]"):
            print("Task already completed.\n")

        else:
            tasks[number - 1] = tasks[number - 1].replace("[ ]", "[✓]", 1)

            save_tasks(tasks)

            print("Task marked as completed.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def main():

    tasks = load_tasks()

    while True:

        print("===================================")
        print("      SIMPLE TO-DO LIST")
        print("===================================")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task Complete")
        print("5. Exit")
        print("===================================")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            remove_task(tasks)

        elif choice == "4":
            complete_task(tasks)

        elif choice == "5":
            print("\nSaving tasks...")
            save_tasks(tasks)
            print("Thank you for using the To-Do List App!")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()