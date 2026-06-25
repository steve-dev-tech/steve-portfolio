import json

FILE_NAME = "students.json"


# Load data
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        data = {"students": []}
        save_data(data)
        return data


# Save data
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# Add student
def add_student():
    
    data = load_data()

    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    data["students"].append(student)

    save_data(data)

    print("Student added successfully.")

# View students
def view_students():
    
    data = load_data()

    if len(data["students"]) == 0:
        print("No students found.")
        return

    print("\n----- STUDENTS -----")

    for index, student in enumerate(data["students"], start=1):

        print(
            f"{index}. Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Course: {student['course']}"
        )


# Search student
def search_student():
    
    data = load_data()

    search_name = input("Enter student name: ")

    found = False

    for student in data["students"]:

        if student["name"].lower() == search_name.lower():

            print(
                f"Name: {student['name']} | "
                f"Age: {student['age']} | "
                f"Course: {student['course']}"
            )

            found = True

    if not found:
        print("Student not found.")


# Delete student
def delete_student():
    
    data = load_data()

    if len(data["students"]) == 0:
        print("No students found.")
        return

    print("\n----- STUDENTS -----")

    for index, student in enumerate(data["students"], start=1):

        print(
            f"{index}. Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Course: {student['course']}"
        )

    try:
        choice = int(input("Enter student number to delete: "))

        deleted_student = data["students"].pop(choice - 1)

        save_data(data)

        print(f"Deleted: {deleted_student['name']}")

    except (ValueError, IndexError):
        print("Invalid selection.")


# Menu
def menu():

    while True:

        print("\n===== STUDENT RECORD SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    menu()