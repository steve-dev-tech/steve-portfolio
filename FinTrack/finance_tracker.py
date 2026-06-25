import json
import os
from datetime import date

DATA_FILE = "finance_data.json"

# Load data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    return {
        "income": [],
        "expenses": []
    }

# Save data
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add income
def add_income(data):
    try:
        amount = float(input("Enter income amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    source = input("Enter income source: ")

    income = {
    "amount": amount,
    "source": source,
    "date": str(date.today())
    }

    data["income"].append(income)

    save_data(data)

    print("Income added successfully")

# Add expense
def add_expense(data):

    try:
        amount = float(input("Enter expense amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    category = input("Enter expense category: ")

    expense = {
    "amount": amount,
    "category": category,
    "date": str(date.today())
}
    data["expenses"].append(expense)

    save_data(data)

    print("Expense added successfully")

# View summary
def view_summary(data):
    total_income = sum(item["amount"] for item in data["income"])

    total_expenses = sum(item["amount"] for item in data["expenses"])

    balance = total_income - total_expenses

    print("\n----- FINANCIAL SUMMARY -----")
    print("Total Income:", total_income)
    print("Total Expenses:", total_expenses)
    print("Balance:", balance)


    # View all transactions
def view_transactions(data):

    print("\n----- INCOME -----")

    for item in data["income"]:
        print(f'{item["source"]}: {item["amount"]} ({item["date"]})')

    print("\n----- EXPENSES -----")

    for item in data["expenses"]:
        print(f'{item["category"]}: {item["amount"]} ({item["date"]})')
        
def reset_data(data):
    
        data["income"] = []
        data["expenses"] = []

        save_data(data)

        print("All data has been cleared.")
    
def search_transactions(data):
    search = input("Enter search term: ")
    found = False

    print("\nMatching Transactions:")

    # Search income
    for transaction in data["income"]:
        if transaction["source"].lower() == search.lower():
            print(f'{transaction["source"]}: {transaction["amount"]} ({transaction["date"]})')
            found = True

    # Search expenses
    for transaction in data["expenses"]:
        if transaction["category"].lower() == search.lower():
            print(f'{transaction["category"]}: {transaction["amount"]} ({transaction["date"]})')
            found = True

    if not found:
        print("No transactions found.")
        
        
def delete_transaction(data):
    
    print("\n----- EXPENSES -----")

    for index, item in enumerate(data["expenses"], start=1):
        print(f'{index}. {item["category"]}: {item["amount"]}')

    try:
        choice = int(input("Enter expense number to delete: "))

        if 1 <= choice <= len(data["expenses"]):

            deleted = data["expenses"].pop(choice - 1)

            save_data(data)

            print("Deleted:", deleted["category"])

        else:
            print("Invalid number")

    except ValueError:
        print("Please enter a valid number")
        
    
    
        
        
# Main menu
def menu():
    data = load_data()

    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. View Transactions")
        print("5: Reset Data")
        print("6: Search Transaction")
        print("7: Delete Transaction")
        print("8. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_income(data)

        elif choice == "2":
            add_expense(data)

        elif choice == "3":
            view_summary(data)
        
        elif choice == "4":
            view_transactions(data) 
        
        elif choice == "5":
            reset_data(data)
        
        elif choice == "6":
            search_transactions(data)
        
        elif choice == "7":
            delete_transaction(data)
            
        elif choice == "8":
            print("Goodbye")
            break

        else:
            print("Invalid option")

menu()