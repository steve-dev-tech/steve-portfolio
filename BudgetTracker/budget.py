import json

FILE_NAME = "budget.json"


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return {
            "income": [],
            "expenses": []
        }


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_income():
    
    data = load_data()

    source = input("Enter income source: ")
    amount = float(input("Enter amount: "))

    income = {
        "source": source,
        "amount": amount
    }

    data["income"].append(income)

    save_data(data)

    print("Income added successfully.")


def add_expense():
    
    data = load_data()

    title = input("Enter expense title: ")
    amount = float(input("Enter amount: "))

    expense = {
        "title": title,
        "amount": amount
    }

    data["expenses"].append(expense)

    save_data(data)

    print("Expense added successfully.")


def view_summary():
    
    data = load_data()

    total_income = 0
    total_expenses = 0

    for income in data["income"]:
        total_income += income["amount"]

    for expense in data["expenses"]:
        total_expenses += expense["amount"]

    balance = total_income - total_expenses

    print("\n----- BUDGET SUMMARY -----")
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Current Balance: {balance}")


def delete_income():
    
    data = load_data()

    if not data["income"]:
        print("No income records found.")
        return

    print("\n----- INCOME -----")

    for index, income in enumerate(data["income"], start=1):
        print(f"{index}. {income['source']} - {income['amount']}")

    choice = int(input("Enter income number to delete: "))

    deleted = data["income"].pop(choice - 1)

    save_data(data)

    print(f"Deleted: {deleted['source']}")


def delete_expense():
    
    data = load_data()

    if not data["expenses"]:
        print("No expense records found.")
        return

    print("\n----- EXPENSES -----")

    for index, expense in enumerate(data["expenses"], start=1):
        print(f"{index}. {expense['title']} - {expense['amount']}")

    choice = int(input("Enter expense number to delete: "))

    deleted = data["expenses"].pop(choice - 1)

    save_data(data)

    print(f"Deleted: {deleted['title']}")


def menu():

    while True:

        print("\n===== BUDGET TRACKER =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Delete Income")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_income()

        elif choice == "2":
            add_expense()

        elif choice == "3":
            view_summary()

        elif choice == "4":
            delete_income()

        elif choice == "5":
            delete_expense()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


menu()