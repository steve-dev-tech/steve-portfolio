import json

FILE_NAME = "vault.json"


# Load data from JSON
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"accounts": []}


# Save data to JSON
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# Add account
def add_account():
    
    data = load_data()

    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    account = {
        "website": website,
        "username": username,
        "password": password
    }

    data["accounts"].append(account)

    save_data(data)

    print("Account saved successfully.")


# View accounts
def view_accounts():
    
    data = load_data()

    print("\n----- ACCOUNTS -----")

    for index, account in enumerate(data["accounts"], start=1):

        print(
            f'{index}. Website: {account["website"]} | '
            f'Username: {account["username"]} | '
            f'Password: {account["password"]}'
        )

# Search account
def search_account():
    
    data = load_data()

    search = input("Enter website name: ")

    found = False

    for account in data["accounts"]:

        if account["website"].lower() == search.lower():

            print(
                f'Website: {account["website"]} | '
                f'Username: {account["username"]} | '
                f'Password: {account["password"]}'
            )

            found = True

    if not found:
        print("Account not found.")

# Delete account
def delete_account():
    
    data = load_data()

    print("\n----- ACCOUNTS -----")

    for index, account in enumerate(data["accounts"], start=1):

        print(
            f'{index}. Website: {account["website"]} | '
            f'Username: {account["username"]}'
        )

    try:

        choice = int(input("Enter account number to delete: "))

        if 1 <= choice <= len(data["accounts"]):

            deleted = data["accounts"].pop(choice - 1)

            save_data(data)

            print("Deleted:", deleted["website"])

        else:
            print("Invalid account number.")

    except ValueError:
        print("Please enter a valid number.")

# Main menu
def menu():
    while True:
        print("\n--- Password Vault ---")
        print("1. Add Account")
        print("2. View Accounts")
        print("3. Search Account")
        print("4. Delete Account")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_account()

        elif choice == "2":
            view_accounts()

        elif choice == "3":
            search_account()

        elif choice == "4":
            delete_account()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


menu()