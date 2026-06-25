import json

FILE_NAME = "employees.json"


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return {"employees": []}


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_employee():
    
    data = load_data()

    name = input("Enter employee name: ")
    position = input("Enter position: ")
    salary = float(input("Enter salary: "))

    employee = {
        "name": name,
        "position": position,
        "salary": salary
    }

    data["employees"].append(employee)

    save_data(data)

    print("Employee added successfully.")


def view_employees():
    
    data = load_data()

    if len(data["employees"]) == 0:
        print("No employees found.")
        return

    print("\n----- EMPLOYEES -----")

    for index, employee in enumerate(data["employees"], start=1):

        print(
            f"{index}. "
            f"Name: {employee['name']} | "
            f"Position: {employee['position']} | "
            f"Salary: {employee['salary']}"
        )


def search_employee():
    
    data = load_data()

    employee_name = input("Enter employee name: ")

    for employee in data["employees"]:

        if employee["name"].lower() == employee_name.lower():

            print(
                f"Name: {employee['name']} | "
                f"Position: {employee['position']} | "
                f"Salary: {employee['salary']}"
            )

            return

    print("Employee not found.")


def update_salary():
    
    data = load_data()

    employee_name = input("Enter employee name: ")

    for employee in data["employees"]:

        if employee["name"].lower() == employee_name.lower():

            new_salary = float(input("Enter new salary: "))

            employee["salary"] = new_salary

            save_data(data)

            print("Salary updated successfully.")

            return

    print("Employee not found.")


def delete_employee():
    
    data = load_data()

    if len(data["employees"]) == 0:
        print("No employees found.")
        return

    print("\n----- EMPLOYEES -----")

    for index, employee in enumerate(data["employees"], start=1):

        print(
            f"{index}. "
            f"Name: {employee['name']} | "
            f"Position: {employee['position']} | "
            f"Salary: {employee['salary']}"
        )

    try:

        choice = int(input("Enter employee number to delete: "))

        deleted_employee = data["employees"].pop(choice - 1)

        save_data(data)

        print(f"Deleted: {deleted_employee['name']}")

    except (ValueError, IndexError):

        print("Invalid selection.")


def menu():

    while True:

        print("\n===== EMPLOYEE MANAGEMENT =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Salary")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_salary()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


menu()