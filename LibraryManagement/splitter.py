import json

FILE_NAME = "expenses.json"


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return {"expenses": []}


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_expenses():
    data = load_data()
    
    title = input("Enter title:")
    amount = float(input("Enter amount:"))
    quantity = int(input("Enter quantity:"))
    
    expenses = {
        "title": title, 
        "amount": amount, 
        "quantity": quantity,
    }
    
    data["expenses"].append(expenses)
    save_data(data)
    
    print("Expenses added successful")
    

    
def view_expenses():
    
    data = load_data()

    if len(data["expenses"]) == 0:
        print("No expenses found.")
        return

    print("\n----- EXPENSES -----")

    for index, expense in enumerate(data["expenses"], start=1):

        print(
            f"{index}. "
            f"Title: {expense['title']} | "
            f"Amount: {expense['amount']} | "
            f"Quantity: {expense['quantity']}"
        )

def split_expense():
    
    data = load_data()

    if len(data["expenses"]) == 0:
        print("No expenses found.")
        return

    print("\n----- EXPENSES -----")

    for index, expense in enumerate(data["expenses"], start=1):

        print(
            f"{index}. "
            f"Title: {expense['title']} | "
            f"Amount: {expense['amount']} | "
            f"Quantity: {expense['quantity']}"
        )

    try:

        choice = int(input("Choose expense number: "))

        expense = data["expenses"][choice - 1]

        split_amount = expense["amount"] / expense["quantity"]

        print(f"Each person pays: {split_amount:.2f}")

    except (ValueError, IndexError):

        print("Invalid selection.")
        

def delete_expense():
    
    data = load_data()

    if len(data["expenses"]) == 0:
        print("No expenses found.")
        return

    print("\n----- EXPENSES -----")

    for index, expense in enumerate(data["expenses"], start=1):

        print(
            f"{index}. "
            f"Title: {expense['title']} | "
            f"Amount: {expense['amount']} | "
            f"Quantity: {expense['quantity']}"
        )

    try:

        choice = int(input("Enter expense number to delete: "))

        deleted_expense = data["expenses"].pop(choice - 1)

        save_data(data)

        print(f"Deleted: {deleted_expense['title']}")

    except (ValueError, IndexError):

        print("Invalid selection.")


def menu():

    while True:

        print("\n===== EXPENSE SPLITTER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Split Expense")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expenses()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            split_expense()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


menu()