import json

FILE_NAME = "tasks.json"


# -----------------------
# Data Functions
# -----------------------

def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        data = {"tasks": []}
        save_data(data)
        return data


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# -----------------------
# Core Functions
# -----------------------

def add_task():
    
    data = load_data()

    task_name = input("Enter task: ")

    task = {
        "task": task_name,
        "completed": False
    }

    data["tasks"].append(task)

    save_data(data)

    print("Task added successfully")


def view_tasks():
    
    data = load_data()

    print("\n----- TASKS -----")

    for index, task in enumerate(data["tasks"], start=1):

        status = "Done" if task["completed"] else "Pending"

        print(f'{index}. {task["task"]} [{status}]')


def complete_task():
    
    data = load_data()

    print("\n----- TASKS -----")

    for index, task in enumerate(data["tasks"], start=1):

        status = "Done" if task["completed"] else "Pending"

        print(f'{index}. {task["task"]} [{status}]')

    try:

        choice = int(input("Enter task number to complete: "))

        if 1 <= choice <= len(data["tasks"]):

            data["tasks"][choice - 1]["completed"] = True

            save_data(data)

            print("Task marked as completed.")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    
    data = load_data()

    print("\n----- TASKS -----")

    for index, task in enumerate(data["tasks"], start=1):

        status = "Done" if task["completed"] else "Pending"

        print(f'{index}. {task["task"]} [{status}]')

    try:

        choice = int(input("Enter task number to delete: "))

        if 1 <= choice <= len(data["tasks"]):

            deleted = data["tasks"].pop(choice - 1)

            save_data(data)

            print("Deleted:", deleted["task"])

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# -----------------------
# Menu
# -----------------------

def menu():

    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    menu()